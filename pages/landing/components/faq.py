import allure

from pages.base.base_page import BasePage
from utils.webdriver.driver.page import Page
from utils.webdriver.logger import logger


class Faq(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Отображение каждого вопроса")
    def check_all_questions(self) -> None:
        questions = self.locators.faq_questions.get_elements()._list

        for question in reversed(questions):
            question.click(force=True)

            question_menu_title_text = (
                self.locators.faq_section_active_question.get_element()
            ).text

            with allure.step(f'Выбранный пункт меню: "{question_menu_title_text}"'):
                logger.info(f'Выбранный пункт меню: "{question_menu_title_text}"')

            with allure.step(
                "Проверка: заголовок ответа соответствует выбранному вопросу"
            ):
                self.locators.faq_section_active_question_title.should_have_text(
                    text=question_menu_title_text
                )
                logger.info(
                    "Проверка: заголовок ответа соответствует выбранному вопросу"
                )

    @allure.step('Проверка: Кнопка "Узнать больше"')
    def check_more_details_button(self) -> None:
        self.locators.faq_section_more_details_link.check_link()
