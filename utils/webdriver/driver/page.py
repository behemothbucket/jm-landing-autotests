from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.exceptions import MaxRetryError
from typing import List

from config import HEADLESS, UIConfig
from utils.webdriver.logger import logger
from utils.types.webdriver.driver.page import PageInterface
from utils.webdriver.driver.element import Element
from utils.webdriver.driver.elements import Elements
from utils.webdriver.driver.page_wait import PageWait
from utils.webdriver.factory.factory import build_from_config


class Page(PageInterface):
    """
    Page interface that representing interactions with page
    like finding locators, opening url etc.
    """

    def __init__(self, config: UIConfig):
        self.config = config

        self._webdriver = None
        self._wait = None

    def init_webdriver(self) -> WebDriver:
        """Initialize WebDriver using the UIConfig"""
        self._webdriver = build_from_config(self.config)

        self._wait = PageWait(
            self, self._webdriver, self.config.driver.wait_time, ignored_exceptions=None
        )

        if self.config.driver.page_load_wait_time:
            self.set_page_load_timeout(self.config.driver.page_load_wait_time)

        logger.info(f"Режим headless: {self.config.driver.headless}")

        if not self.config.driver.headless:
            if self.config.viewport.maximize:
                self.maximize_window()
            else:
                self.viewport(
                    self.config.viewport.width,
                    self.config.viewport.height,
                    self.config.viewport.orientation,
                )

        return self._webdriver

    @property
    def webdriver(self) -> WebDriver:
        """The current instance of Selenium's `WebDriver` API."""
        return self.init_webdriver() if self._webdriver is None else self._webdriver

    def url(self) -> str:
        """Get the current page's URL"""
        return self.webdriver.current_url

    def wait_for_correct_current_url(
        self,
        expected_url: str,
        timeout: int = 8,
    ) -> None:
        """Wait for the page to load and check actual and expected url..."""
        try:
            self.wait(timeout).until(
                lambda _: self.url() == expected_url,
            )
            logger.info(f"Текущий URL: {self.url()}")
        except TimeoutException:
            raise TimeoutException(
                f"Фактический URL: [{self.webdriver.current_url}] != Ожидаемый: [{expected_url}]",
            )

    def visit(self, url: str = "", base: bool = False) -> "Page":
        """Navigate to the given URL"""

        if base:
            url = self.config.base_url
        else:
            url = url if url.startswith("http") else (self.config.base_url + url)

        logger.info("Page.visit() - Открыть URL: `%s`", url)

        self.webdriver.get(url)

        return self

    def reload(self) -> "Page":
        """Reload (aka refresh) the current window"""
        logger.info("Page.reload() - Перезагрузка страницы")

        self.webdriver.refresh()
        return self

    def wait_until_stable(self) -> WebDriver:
        """Waits until webdriver will be stable"""
        logger.info("Page.wait_until_stable() - Ожидание стабилизации браузера ")

        try:
            return self.webdriver
        except MaxRetryError:
            sleep(0.5)
            self.wait_until_stable()

    def get_xpath(self, xpath: str, timeout: int = None) -> Element:
        """
        Finds the DOM element that match the XPATH selector.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.
        """
        logger.info("Page.get_xpath() - Найти элемент с XPath: `%s`", xpath)

        by = By.XPATH

        if timeout == 0:
            element = self.webdriver.find_element(by, xpath)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(by, xpath),
                f"Не найден элемент с XPath: `{xpath}`",
            )

        return Element(self, element, locator=(by, xpath))

    def find_xpath(self, xpath: str, timeout: int = None) -> Elements:
        """
        Finds the DOM elements that match the XPATH selector.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.
        """
        by = By.XPATH
        elements: list[WebElement] = []

        logger.info("Page.find_xpath() - Найти элементы с XPath: `%s`", xpath)

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, xpath)
            else:
                #         WebDriverWait(self.webdriver, timeout).until(
                #             lambda _: self.webdriver.find_elements(by, xpath),
                #             f"Could not find an element with xpath: `{xpath}`",
                #         )
                elements = self.wait(timeout).until(
                    lambda driver: driver.find_elements(by, xpath),
                    f"Не найдены элементы с XPath: `{xpath}`",
                )
        except TimeoutException:
            pass

        return Elements(self, elements, locator=(by, xpath))

    def wait(
        self,
        timeout: int = None,
        use_self: bool = False,
        ignored_exceptions: list = None,
    ) -> WebDriverWait | PageWait:
        """The Wait object with the given timeout in seconds"""
        if timeout:
            return self._wait.build(timeout, use_self, ignored_exceptions)

        return self._wait.build(
            self.config.driver.wait_time, use_self, ignored_exceptions
        )

    def quit(self):
        """Quits the driver"""
        logger.info("Page.quit() - Закрыть страницу и все окна текущей сессии браузера")

        self.webdriver.quit()

    def screenshot(self, filename: str) -> str:
        """Take a screenshot of the current Window"""
        logger.info("Page.screenshot() - Сохранить скриншот как: `%s`", filename)

        self.webdriver.save_screenshot(filename)
        return filename

    def maximize_window(self) -> "Page":
        """Maximizes the current Window"""
        logger.info("Page.maximize_window() - Максимально развернуть окно браузера")

        self.webdriver.maximize_window()
        return self

    def move_to_bottom_of_page(self) -> "Page":
        """Move to bottom of page"""
        logger.info(
            "Element.move_to_bottom_of_page() - Перевести фокус в конец страницы"
        )

        self.webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        return self

    def execute_script(self, script: str, *args) -> "Page":
        """Executes javascript in the current window or frame"""
        logger.info(
            "Page.execute_script() - Исполнить JavaScript `%s` в браузере", script
        )

        self.webdriver.execute_script(script, *args)
        return self

    def set_page_load_timeout(self, timeout: int) -> "Page":
        """Set the amount of time to wait for a page load to complete before throwing an error"""
        logger.info(
            "Page.set_page_load_timeout() - Установить допустимое время загрузки страницы: `%s`",
            timeout,
        )

        self.webdriver.set_page_load_timeout(timeout)
        return self

    def viewport(self, width: int, height: int, orientation: str) -> "Page":
        """Control the size and orientation of the current context's browser window"""
        logger.info(
            "Page.viewport() - Установить видимую область с шириной: `%s`, высотой: `%s`, ориентацией: `%s`",
            width,
            height,
            orientation,
        )

        if orientation == "portrait":
            self.webdriver.set_window_size(width, height)
        elif orientation == "landscape":
            self.webdriver.set_window_size(height, width)
        else:
            raise ValueError(
                "Ориентация экрана должна быть `портретной` или `альбомной`."
            )
        return self

    def open_new_tab_via_js(self, url: str) -> None:
        """Open url via JavaScript...")"""
        logger.info(f"Открыть ссылку {url} в новой вкладке")
        self.webdriver.execute_script(f"window.open('{url}')")

    def get_tabs(self) -> List[str]:
        """Getting all tabs..."""
        return self.webdriver.window_handles

    def switch_to_tab(self, tab) -> None:
        """Switching to required tab..."""
        return self.webdriver.switch_to.window(tab)

    def close_current_tab(self):
        """Close focused tab..."""
        self.webdriver.close()

    def switch_to_tab_action_close_tab(self, url: str, callback, **kwargs) -> None:
        """Open tabs do action and close"""
        tabs = self.get_tabs()

        if len(tabs) < 2:
            raise Exception("Недостаточно вкладок для выполнения операции")

        previous_tab, next_tab = tabs[:2]

        self.switch_to_tab(next_tab)

        self.wait_for_correct_current_url(url)

        if callback:
            logger.info(f"Выполнение callback...")
            callback(self, **kwargs)

        self.close_current_tab()
        self.switch_to_tab(previous_tab)
