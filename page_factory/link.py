import allure
from selenium.common import ElementNotInteractableException

from page_factory.component import Component
from utils.constants.routes import Routes
from utils.webdriver.driver.element import Element
from utils.webdriver.logger import logger


class Link(Component):
    @property
    def type_of(self) -> str:
        return "link"

    def check_link(
        self,
        callback=None,
        **kwargs,
    ) -> None:
        """Открыть ссылку в новой вкладке и проверить что url соответствует ожидаемому.

        Аргументы:

        callback -- ссылка на функцию
        **kwargs -- передача параметра в качестве аргумента (для callback)


        """
        logger.info("Link.check_link() - Проверка ссылки в элементе")

        elements: list[Element] = self.get_elements()._list

        with allure.step(
            "Нажать на каждую ссылку и проверить ожидаемый и фактический URL"
        ):
            problem_element: Element | None = elements[0]
            try:
                for element in elements:
                    problem_element = element

                    url = self.get_normalized_element_url(element.get_attribute("href"))

                    if Routes.ANCHOR.value in url:
                        logger.info(f"Ссылка-якорь: {url}")
                        continue

                    with allure.step(
                        f'Проверка: открыть URL элемента "{self.name}" и проверить фактический URL'
                    ):
                        logger.info(
                            f'Проверка: открыть URL элемента "{self.name}" и проверить фактический URL'
                        )

                    self._page.open_new_tab_via_js(url)

                    self._page.switch_to_tab_action_close_tab(url, callback, **kwargs)

            except ElementNotInteractableException:
                raise Exception(
                    f'Элемент "{problem_element.text}" не кликабелен или не явлется ссылкой'
                )

    def get_normalized_element_url(self, url: str) -> str:
        normalized_url = url
        if Routes.LOGIN_PROD_NO_PATH.value in url:
            normalized_url = Routes.LOGIN_PROD.value

        if "vk" in url:
            normalized_url = Routes.REDIRECT_VK.value

        return normalized_url
