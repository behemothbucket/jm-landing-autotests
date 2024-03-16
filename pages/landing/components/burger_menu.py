import allure

from pages.base.base_page import BasePage
from utils.constants.features import LandingText
from utils.webdriver.driver.page import Page
from utils.webdriver.logger import logger


class BurgerMenu(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Открыть бургер-меню")
    def open_burger_menu(self) -> None:
        self.locators.burger_menu_button.should_be_clickable()
        self.locators.burger_menu_button.click()

    @allure.step("Проверка: Пункты меню и ссылки")
    def check_menu_items(self) -> None:
        self.locators.burger_menu_about_joymoney_button.should_be_clickable()
        self.locators.burger_menu_about_joymoney_button.click()

        about_joymoney_submenu_links = (
            self.locators.about_joymoney_submenu_links.get_elements()._list
        )

        for link in about_joymoney_submenu_links:
            with allure.step(
                f'Проверка: О Joymoney - "{link.text}" кликабельная ссылка'
            ):
                link.should().be_clickable()
                logger.info(f'О Joymoney - "{link.text}"')

        self.locators.burger_menu_links.check_link()

    @allure.step("Проверка: Промо-блок")
    def check_burger_menu_promo(self) -> None:
        self.locators.burger_menu_promo_div.should_be_visible()
        self.locators.burger_menu_promo_div.should_have_text(
            text=LandingText.BURGER_MENU_PROMO_TEXT.value
        )

        self.locators.burger_menu_promo_details_link.should_be_clickable()
        self.locators.burger_menu_promo_details_link.check_link()
