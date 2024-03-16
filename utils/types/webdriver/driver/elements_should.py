from abc import ABC, abstractmethod
from typing import Union

from selenium.webdriver.support.wait import WebDriverWait


from utils.types.webdriver.driver.elements import ElementsInterface
from utils.types.webdriver.driver.page import PageInterface
from utils.types.webdriver.driver.page_wait import PageWaitInterface


class ElementsShouldInterface(ABC):
    _page: "PageInterface"
    _wait: Union[WebDriverWait, "PageWaitInterface"]
    _elements: "ElementsInterface"

    @abstractmethod
    def __init__(
        self,
        page: "PageInterface",
        elements: "ElementsInterface",
        timeout: int,
        ignored_exceptions: tuple | None = None,
    ):
        ...

    @abstractmethod
    def have_length(self, length: int) -> bool:
        ...

    @abstractmethod
    def not_be_empty(self) -> "ElementsInterface":
        ...
