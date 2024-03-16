from abc import ABC, abstractmethod
from typing import Callable, Union

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from utils.types.webdriver.driver.page import PageInterface

WebDriverUntilMethod = Callable[[WebDriver], bool]
WebElementUntilMethod = Callable[[WebElement], bool]


class PageWaitInterface(ABC):
    _page: "PageInterface"
    _wait: WebDriverWait
    _webdriver: WebDriver

    @abstractmethod
    def __init__(
        self,
        page: "PageInterface",
        webdriver: WebDriver,
        timeout: int,
        ignored_exceptions: tuple | None = None,
    ):
        ...

    @abstractmethod
    def until(self, method: WebDriverUntilMethod, message=""):
        ...

    @abstractmethod
    def until_not(self, method: WebDriverUntilMethod, message=""):
        ...

    @abstractmethod
    def build(
        self, timeout: int, use_self=False, ignored_exceptions: tuple | None = None
    ) -> Union[WebDriverWait, "PageWaitInterface"]:
        ...
