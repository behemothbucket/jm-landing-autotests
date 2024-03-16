import allure

from pages.base.base_page import BasePage
from utils.webdriver.driver.page import Page


class Feedback(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Кнопка 'Оставить отзыв'")
    def check_feedback_button(self) -> None:
        self.locators.feedback_section_leave_feedback_link.should_be_clickable()
        self.locators.feedback_section_leave_feedback_link.check_link()
