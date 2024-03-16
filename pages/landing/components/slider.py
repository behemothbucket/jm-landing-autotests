import allure

from pages.base.base_page import BasePage
from utils.webdriver.driver.page import Page
from utils.webdriver.logger import logger


class Slider(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Кликнуть по каждому слайду")
    def click_on_every_slide(self) -> None:
        slider_buttons = self.locators.slider_buttons.get_elements()._list

        for i, slide in enumerate(slider_buttons, 1):
            with allure.step(f"Открыть {i} слайд"):
                logger.info(f"Открыть {i} слайд")

                slide.click()
                self.locators.slider_current_detail_button.check_link()
