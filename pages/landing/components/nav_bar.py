import allure

from pages.base.base_page import BasePage
from utils.webdriver.driver.page import Page


class NavBar(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Кликнуть по каждому элементу меню")
    def click_on_every_menu_item(self) -> None:
        navigation_menu_items = self.locators.navigation_menu_links.get_elements()
        self.locators.navigation_menu_links.check_link(
            elements=navigation_menu_items._list
        )
