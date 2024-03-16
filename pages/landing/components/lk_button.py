import allure

from pages.base.base_page import BasePage
from utils.constants.routes import Routes
from utils.webdriver.driver.page import Page


class LKButton(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Кликнуть по кнопке 'Личный кабинет'")
    def click_on_lk_button(self) -> None:
        self.locators.lk_button.should_be_clickable()
        self.locators.lk_button.click()
        self.page.wait_for_correct_current_url(expected_url=Routes.LOGIN_PREPROD)
