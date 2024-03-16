import allure

from pages.base.base_page import BasePage
from pages.landing.components.helpers.calculator import *
from utils.constants.features import Tariff
from utils.webdriver.driver.page import Page


class Calculator(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Проверка: Тариф 'Мега старт'")
    def check_mega_start(self) -> None:
        iterate_through_requested_money_or_period_list(
            self,
            requested_money_or_period_list=Tariff.MEGA_START.amount_range,
            expected_tariff=Tariff.MEGA_START,
        )
        self.page.reload()

    @allure.step("Проверка: Тариф 'Практик'")
    def check_praktik(self) -> None:
        iterate_through_requested_money_or_period_list(
            self,
            requested_money_or_period_list=Tariff.PRAKTIK.amount_range,
            expected_tariff=Tariff.PRAKTIK,
        )

    @allure.step("Проверка: Тариф 'Профи'")
    def check_profi(self) -> None:
        iterate_through_requested_money_or_period_list(
            self,
            requested_money_or_period_list=list(range(40000, 101000, 20000)),
            expected_tariff=Tariff.PROFI,
        )

    @allure.step("Проверка: Переход из 'Профи' в 'Практик'")
    def check_profi_to_praktik(self) -> None:
        iterate_through_requested_money_or_period_list(
            self,
            requested_money_or_period_list=list(reversed(Tariff.PROFI.amount_range)),
            expected_tariff=Tariff.PROFI,
        )
        iterate_through_requested_money_or_period_list(
            self,
            requested_money_or_period_list=[24000],
            expected_tariff=Tariff.PRAKTIK,
        )

    @allure.step("Проверка: Переход из 'Практик' в 'Мега старт'")
    def check_praktik_to_mega_start(self) -> None:
        iterate_through_requested_money_or_period_list(
            self,
            requested_money_or_period_list=[11000],
            expected_tariff=Tariff.PRAKTIK,
        )
        iterate_through_requested_money_or_period_list(
            self,
            requested_money_or_period_list=[10000],
            expected_tariff=Tariff.MEGA_START,
        )

    @allure.step("Проверка: Переход тарифов '30 дней в 10 недель' и обратно")
    def check_from_30_days_to_10_weeks_with_reverse(self) -> None:
        self.page.reload()

        iterate_through_requested_money_or_period_list(
            self,
            [30],
            handler="period",
            expected_tariff=Tariff.MEGA_START,
        )
        iterate_through_requested_money_or_period_list(
            self,
            [30],
            handler="period",
            final_move="step_forward",
            expected_tariff=Tariff.PROFI,
        )
        # check_current_tariff_name(self, expected_tariff=Tariff.PROFI.name)

        iterate_through_requested_money_or_period_list(
            self,
            [10],
            handler="period",
            final_move="step_back",
            expected_tariff=Tariff.PRAKTIK,
        )
        # check_current_tariff_name(self, expected_tariff=Tariff.PRAKTIK.name)
