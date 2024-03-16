import allure

from pages.base.base_page import BasePage
from utils.webdriver.driver.page import Page


class Footer(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Кнопка 'Оставить отзыв'")
    def check_lk_button(self) -> None:
        self.locators.footer_lk_button.check_link()
