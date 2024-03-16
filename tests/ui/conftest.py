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
from utils.webdriver.driver.page import Page


@pytest.fixture(scope="function")
def burger_menu(page: Page) -> BurgerMenu:
    return BurgerMenu(page=page)


@pytest.fixture(scope="function")
def nav_menu(page: Page) -> NavMenu:
    return NavMenu(page=page)


@pytest.fixture(scope="function")
def lk_button(page: Page) -> LKButton:
    return LKButton(page=page)


@pytest.fixture(scope="function")
def slider(page: Page) -> Slider:
    return Slider(page=page)


@pytest.fixture(scope="function")
def calculator(page: Page) -> Calculator:
    return Calculator(page=page)


@pytest.fixture(scope="function")
def how_to(page: Page) -> HowTo:
    return HowTo(page=page)


@pytest.fixture(scope="function")
def tariff_cards(page: Page) -> TariffCards:
    return TariffCards(page=page)


@pytest.fixture(scope="function")
def popular_services(page: Page) -> PopularServices:
    return PopularServices(page=page)


@pytest.fixture(scope="function")
def faq(page: Page) -> Faq:
    return Faq(page=page)


@pytest.fixture(scope="function")
def feedback(page: Page) -> Feedback:
    return Feedback(page=page)


@pytest.fixture(scope="function")
def footer(page: Page) -> Footer:
    return Footer(page=page)
