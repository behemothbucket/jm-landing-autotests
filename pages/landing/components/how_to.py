import allure

from pages.base.base_page import BasePage
from utils.constants.features import LandingText
from utils.webdriver.driver.page import Page


class HowTo(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Текст в разделе 'Просто получить и оплатить займ'")
    def check_how_to_text(self) -> None:
        self.locators.get_loan_steps_div.should_have_text(
            text=LandingText.GET_LOAN_STEPS_TEXT.value
        )

        take_loan_tab_button = self.locators.how_to_take_loan_tab_button.get_element()
        pay_loan_tab_button = self.locators.how_to_pay_loan_tab_button.get_element()

        pay_loan_tab_button.click()

        self.locators.pay_loan_variants.should_have_text(
            text=LandingText.PAY_LOAN_VARIANTS_TEXT.value
        )

        take_loan_tab_button.click()

        self.locators.how_to_buttons.check_link()
