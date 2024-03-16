import allure

from pages.base.base_page import BasePage
from utils.webdriver.driver.page import Page


class NavMenu(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Кликнуть по каждому элементу меню")
    def click_on_every_menu_item(self) -> None:
        self.locators.navigation_menu_links.check_link()
