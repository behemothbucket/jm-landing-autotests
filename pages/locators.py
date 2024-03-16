from page_factory.div import Div
from page_factory.iframe import Iframe
from page_factory.input import Input
from page_factory.li import Li
from page_factory.link import Link
from page_factory.section import Section
from page_factory.span import Span
from page_factory.text import Text
from page_factory.title import Title
from page_factory.ul import Ul
from utils.webdriver.driver.page import Page


class Locators:
    def __init__(self, page: Page):
        self.burger_menu_button = Link(
            page,
            locator="//span[@class='burger burger--inactive']",
            name="Кнопка бургер-меню",
        )

        self.burger_menu_about_joymoney_button = Span(
            page,
            locator="//nav[@class='inline-menu']//span[contains(text(),'О Joymoney')]",
            name="Кнопка О Joymoney в бургер-меню",
        )

        self.burger_menu_promo_div = Div(
            page,
            locator="//div[@class='menu']//div[@class='promo__text']",
            name="Блок с описанием промо-акции в бергер-меню",
        )

        self.burger_menu_promo_details_link = Link(
            page,
            locator="//div[@class='menu']//div[@class='promo__text']//a[text()='Подробнее']",
            name="Кнопка Подробнее в промоблоке бургер-меню",
        )

        self.about_joymoney_submenu_links = Link(
            page,
            locator="//div[@class='menu']//nav[@class='inline-submenu']/a",
            name="Пункты меню в подменю О Joymoney",
        )

        self.burger_menu_links = Link(
            page,
            locator="//a[@class='inline-submenu__toggle inline-menu__head']",
            name="Ссылки в выпадающем бургер меню",
        )

        self.burger_submenu_links = Link(
            page, locator="//a[@class='pill']", name="Ссылки в подменю JoyMoney"
        )

        self.navigation_menu_links = Link(
            page,
            locator="//nav[@class='header-menu']//div//a",
            name="Ссылки в меню навигации",
        )

        self.lk_button = Link(
            page,
            locator="//nav[@class='header-menu']//a[text()='Личный кабинет']",
            name="Кнопка Личный кабинет",
        )

        self.phone_input = Input(
            page, locator="//input[@name='userPhone']", name="Поле номера телефон"
        )

        self.password_input = Input(
            page, locator="//input[@name='userPassword']", name="Поле пароля"
        )

        self.next_button = Link(
            page, locator="//button[text()='Далее']", name="Кнопка Далее"
        )

        self.slider_buttons = Link(
            page,
            locator="//ul[@class='slider-dots']//button",
            name="Кнопка переключения слайдера",
        )

        self.slider_current_detail_button = Link(
            page,
            locator="//section[@class='hero']//div[contains(@class, 'slick-active')]//a[@class='slide__link']",
            name="Кнопка Подробнее на текущем слайде",
        )

        self.vk_title = Title(
            page,
            locator="//title[contains(text(),'Senler - рассылки в сообществах')]",
            name="Заголовок Senler на странице VK",
        )

        self.calculator_tariff_name_text = Text(
            page,
            locator="//div[@class='calculator']//div[contains(@class,'js-changeTariff')]",
            name="Название тарифа (start|middle|end)",
        )

        self.calculator_get_money_button = Link(
            page,
            locator="//a[@id='calc-btn' and text()='Получить деньги']",
            name="Кнопка Получить деньги",
        )

        self.calculator_handlers_span = Span(
            page,
            locator="//span[contains(@class,'irs-handle')]",
            name="Хэндлеры на калькуляторе",
        )

        self.calculator_values = Span(
            page,
            locator="//span[@class='range__value']",
            name="Значения на калькуляторе (сумма, срок)",
        )

        self.section_how_to_cards_div = Div(
            page,
            locator="//section[@class='how-to']//div[contains(@class, 'tabs')]",
            name="Блок в разделе Просто получить и оплатить займ",
        )

        self.get_loan_steps_div = Div(
            page,
            locator="//div[contains(@class,'steps')]",
            name="Блок инструкции в разделе Просто получить и оплатить займ (Оформите заявку -> Дождитесь решения -> Получите деньги)",
        )

        self.how_to_take_loan_tab_button = Link(
            page,
            locator="//li[contains(@class,'tabs-panel__item') and text()='Получить займ']",
            name="Кнопка Получить займ в разделе Просто получить и оплатить займ",
        )

        self.how_to_pay_loan_tab_button = Link(
            page,
            locator="//li[contains(@class,'tabs-panel__item') and text()='Погасить займ']",
            name="Кнопка Погасить займ в разделе Просто получить и оплатить займ",
        )

        self.how_to_buttons = Link(
            page,
            locator="//section[@class='how-to']//a[contains(@class,'btn')]",
            name="Кнопки в разделе Просто получить и оплатить займ",
        )

        self.pay_loan_variants = Li(
            page,
            locator="//section[@class='how-to']//li[contains(@class, 'tabs-wrapper__item_expanded')]",
            name="Описание вариантов оплаты в разделе how-to",
        )

        self.tariff_cards_tab_products = Li(
            page,
            locator="//section[@id='products']//li[contains(text(),'Продукты')]",
            name="Вкладка Продукты",
        )

        self.tariff_cards_tab_promotions = Li(
            page,
            locator="//section[@id='products']//li[contains(text(),'Акции')]",
            name="Кнопка Акции",
        )

        self.tariff_cards_div = Div(
            page,
            locator="//section[@class='products']//div[contains(@class,'card')]",
            name="Карточки тарифов ('Мега старт', 'Практик', 'Профи')",
        )

        self.tariff_cards_titles_div = Div(
            page,
            locator="//section[@class='products']//div[contains(@class,'products__item-desc')]",
            name="Блоки с описанием тарифов ('0% первый займ Мега Старт', 'до 29000 руб. Практик', 'до 100000 руб. Профи')",
        )

        self.tariff_cards_get_money_links = Link(
            page,
            locator="//section[@class='products']//a[text()='Получить деньги']",
            name="Кнопки Получить деньги в карточках тарифов",
        )

        self.promotions_buttons_links = Link(
            page,
            locator="//section[@id='products']//div[@class='offers']//a[contains(@class, 'btn btn_cta')]",
            name="Кнопки Оставить отзыв, Получить скидку, Узнать больше",
        )

        self.tariff_details_links = Link(
            page,
            locator="//section[@class='products']//a[text()='Подробнее']",
            name="Кнопки Подробнее в карточках тарифов",
        )

        self.tariff_card_features_ul = Ul(
            page,
            locator="//section[@id='products']//ul[@class='products__item-features']",
            name="Детальное описание тарифов в карточках",
        )

        self.popular_services_section = Section(
            page,
            locator="//section[@class='services']",
            name="Секция Популярные сервисы",
        )

        self.popular_services_video_link = Link(
            page,
            locator="//section[@class='services']//a[contains(text(), 'Смотреть видео')]",
            name="Кнопка Смотреть видео",
        )

        self.popular_services_video_modal = Div(
            page, locator="//div[@id='joyMoneyVideo']", name="Модальное окно с видео"
        )

        self.popular_services_video_modal_close_span = Span(
            page,
            locator="//span[@class='close modal__close modal__close-video']",
            name="Кнопка Закрыть в модальном окне с видео",
        )

        self.popular_services_video_iframe = Iframe(
            page,
            locator="//iframe[@title='YouTube video player']",
            name="Iframe для Youtube видео",
        )

        self.popular_services_prolongation_link = Link(
            page,
            locator="//a[@href='prolongation/']",
            name="Кнопка Узнать больше (Продление займа)",
        )

        self.information_section = Section(
            page, locator="//section[@class='information']", name="Секция information"
        )

        self.information_section_get_money_button = Link(
            page,
            locator="//section[@class='information']//a[text()='Получить деньги']",
            name="Кнопка Получить деньги в разделе information",
        )

        self.faq_section = Section(
            page, locator="//section[@class='faq']", name="Секция FAQ"
        )

        self.faq_section_question_title = Title(
            page,
            locator="//section[@class='faq']//h4[@class='faq__title']",
            name="Заголовок H4 в вопросах разделе FAQ",
        )

        self.faq_questions = Li(
            page,
            locator="//section[@class='faq']//li[contains(@class,'accordeon__toggle')]",
            name="Все вопросы в разделе Часто задаваемые вопросы",
        )

        self.faq_section_active_question = Li(
            page,
            locator="//section[@class='faq']//li[@class='accordeon__toggle accordeon__toggle_active']",
            name="Текущий открытый вопрос в разделе FAQ",
        )

        self.faq_section_active_question_title = Title(
            page,
            locator="//section[@class='faq']//li[@class='accordeon__item accordeon__item_expanded']//h4",
            name="Заголовок у открытого вопроса в разделе FAQ",
        )

        self.faq_section_more_details_link = Link(
            page,
            locator="//a[@href='/support/all/']",
            name="Кнопка 'Узнать больше' в разделе разделе FAQ",
        )

        self.feedback_section = Section(
            page, locator="//section[@class='reviews-main']", name="Секция Отзывы"
        )

        self.feedback_section_leave_feedback_link = Link(
            page,
            locator="//section[@class='reviews-main']//a[text()='Оставить отзыв']",
            name="Кнопка Оставить отзыв в разделе Отзывы",
        )

        self.footer_lk_button = Link(
            page,
            locator="//footer//a//b[text()='Личный кабинет']/ancestor::a",
            name="Кнопка Личный кабинет",
        )

        self.close_cookie_modal_span = Span(
            page,
            locator="//span[@class='close cookie__close']",
            name="Кнопка Закрыть модальное окно с cookie's",
        )
