import allure

from pages.base.base_page import BasePage
from utils.constants.routes import Routes
from utils.webdriver.driver.page import Page


class PopularServices(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Кнопка 'Смотреть видео'")
    def check_video_button(self) -> None:
        video_button = self.locators.popular_services_video_link.get_element()
        video_button.move_to_element_center_view()
        video_button.click()

        self.explicit_wait(1)

        video_modal = self.locators.popular_services_video_modal.get_element()
        video_modal.is_displayed()

        video_iframe = self.locators.popular_services_video_iframe.get_element()
        src = video_iframe.get_attribute("src")

        assert (
            src == Routes.YOUTUBE.value
        ), f"Другая ссылка в модальном окне с видео (YouTube)\nФактическая:{src}"

        video_modal_close_button = (
            self.locators.popular_services_video_modal_close_span.get_element()
        )
        video_modal_close_button.click()

    @allure.step("Проверка: Кнопка 'Узнать больше'")
    def check_more_button(self) -> None:
        more_button = self.locators.popular_services_prolongation_link.get_element()
        more_button.move_to_element_center_view()

        self.locators.popular_services_prolongation_link.check_link(
            elements=[more_button]
        )

    @allure.step("Проверка: Кнопка 'Получить деньги'")
    def check_get_money_button(self) -> None:
        get_money_button = (
            self.locators.information_section_get_money_button.get_element()
        )
        get_money_button.move_to_element_center_view()

        self.locators.information_section_get_money_button.check_link(
            elements=[get_money_button]
        )
