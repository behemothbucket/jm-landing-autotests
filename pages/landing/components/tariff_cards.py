import re

import allure

from pages.base.base_page import BasePage
from utils.constants.features import LandingText
from utils.webdriver.driver.element import Element
from utils.webdriver.driver.page import Page
from utils.webdriver.logger import logger


class TariffCards(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Вкладка 'Акции'")
    def check_promotion_tab(self) -> None:
        promotions_tab_button = self.locators.tariff_cards_tab_promotions.get_element()
        promotions_tab_button.move_to_element_center_view()
        promotions_tab_button.click()
        self.locators.promotions_buttons_links.check_link()

    @allure.step("Проверка: Вкладка 'Продукты'")
    def check_products_tab(self) -> None:
        products_tab_button = self.locators.tariff_cards_tab_products.get_element()
        products_tab_button.move_to_element_center_view()
        products_tab_button.click()

        tariff_cards = self.locators.tariff_cards_div.get_elements()._list

        for i in range(len(tariff_cards)):
            card_name = self.__get_card_name(tariff_cards[i].text)
            with allure.step(f"Проверить описание карточки {card_name}"):
                logger.info(f"Проверить описание карточки {card_name}")

                self.__check_card_description(card_description=tariff_cards[i])

        self.locators.tariff_cards_get_money_links.check_link()

    @classmethod
    def __get_card_name(cls, card_raw: str) -> str:
        card_name = ""
        regex = re.search("(Мега Старт|Практик|Профи)", card_raw)
        if regex is not None:
            card_name = regex.group(0)
        return card_name

    def __check_card_description(self, card_description: Element) -> None:
        with allure.step(f"Проверка описания карточки {card_description}"):
            logger.info(f"Проверка описания карточки {card_description}")

            card_description.should().be_visible()
            card_description.should().have_text_in(
                LandingText.TARIFF_CARDS_DESCRIPTIONS_TEXT.value
            )
