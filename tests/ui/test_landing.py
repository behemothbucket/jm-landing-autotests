import allure
import pytest

from pages.landing.components.burger_menu import BurgerMenu
from pages.landing.components.calculator import Calculator
from pages.landing.components.faq import Faq
from pages.landing.components.feedback import Feedback
from pages.landing.components.footer import Footer
from pages.landing.components.how_to import HowTo
from pages.landing.components.lk_button import LKButton
from pages.landing.components.nav_menu import NavMenu
from pages.landing.components.popular_services import PopularServices
from pages.landing.components.slider import Slider
from pages.landing.components.tariff_cards import TariffCards
from utils.constants.features import Feature
from utils.constants.suites import Suite


@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("UI")
@allure.suite(Suite.SMOKE)
@allure.sub_suite("Лендинг")
@allure.feature(Feature.CLIENTS)
class TestLandingPage:
    @pytest.mark.burger_menu
    @allure.title("Бургер меню")
    def test_burger_menu(self, burger_menu: BurgerMenu):
        """Проверка бургер-меню, ссылок внутри меню. Блок промо."""
        burger_menu.open_burger_menu()
        burger_menu.check_menu_items()
        burger_menu.check_burger_menu_promo()

    @pytest.mark.nav_menu
    @allure.title("Меню навигации")
    def test_navigation_menu(self, nav_menu: NavMenu):
        """Проверка меню навигации"""
        nav_menu.click_on_every_menu_item()

    @pytest.mark.lk_button
    @allure.title('Кнопка "Личный кабинет"')
    def test_lk_button(self, lk_button: LKButton):
        """
        <2023-12-13 Ср> Ссылки ведут на продовый URL

        Проверка кнопки Личный кабинет
        """
        lk_button.click_on_lk_button()

    @pytest.mark.slider
    @allure.title("Слайдер")
    def test_slider(self, slider: Slider):
        slider.click_on_every_slide()

    @pytest.mark.calculator
    @allure.title("Калькулятор")
    def test_calculator(self, calculator: Calculator):
        """Во время этих тестов не нужно водить мышкой по экрану,
        иначе значения на калькуляторе собьются
        Это особенность работы драйвера в браузере, а не тестов
        Так же здесь установлен строгий порядок вызова методов.
        Это сделано для того чтобы сэкономить время."""
        calculator.check_mega_start()
        calculator.check_praktik()
        calculator.check_profi()
        calculator.check_profi_to_praktik()
        calculator.check_praktik_to_mega_start()
        calculator.check_from_30_days_to_10_weeks_with_reverse()

    @pytest.mark.how_to
    @allure.title('Раздел "Просто получить и оплатить займ"')
    def test_how_to(self, how_to: HowTo):
        """Проверка раздела Просто получить деньги и оплатить займ"""
        how_to.check_how_to_text()

    @pytest.mark.tariff_cards
    @allure.title('Раздел "Карточки тарифов"')
    def test_tariff_cards(self, tariff_cards: TariffCards):
        """
        <2023-12-13 Ср> Ссылки ведут на продовый URL

        Проверка раздела Карточки тароифов
        """
        tariff_cards.check_promotion_tab()
        tariff_cards.check_products_tab()

    @pytest.mark.popular_services
    @allure.title('Раздел "Популярные сервисы Joymoney"')
    def test_popular_services(self, popular_services: PopularServices):
        """
        <2023-12-13 Ср> Ссылки ведут на продовый URL

        Проверка раздела Популярные сервисы JoyMoney
        """
        popular_services.check_video_button()
        popular_services.check_more_button()
        popular_services.check_get_money_button()

    @pytest.mark.faq
    @allure.title('Раздел "Часто задаваемые вопросы"')
    def test_faq(self, faq: Faq):
        """Проверка раздела Часто задаваемые вопросы"""
        faq.check_all_questions()
        faq.check_more_details_button()

    @pytest.mark.feedback
    @allure.title('Раздел "Оставить отзыв"')
    def test_feedback(self, feedback: Feedback):
        """Проверка раздела Оставить отзыв"""
        feedback.check_feedback_button()

    @pytest.mark.footer
    @allure.title("Подвал страницы")
    def test_footer(self, footer: Footer):
        """
        <2023-12-13 Ср> Ссылки ведут на продовый URL

        Проверка подвала страницы
        """
        footer.check_lk_button()
