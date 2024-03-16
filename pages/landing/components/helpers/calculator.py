import re

import allure
from selenium.webdriver import ActionChains

from utils.constants.features import Tariff
from utils.webdriver.logger import logger


def get_tariff_name_on_calculator(self) -> str:
    element = self.locators.calculator_tariff_name_text.get_element()
    element_with_class_name = element.get_attribute("className")
    class_name = re.findall("(start|middle|end)", element_with_class_name)[0]
    tariff_name = Tariff.get_by(class_name)
    tariff_ru_name = Tariff.get_by(class_name, ru=True)

    with allure.step(f"Текущий тариф на калькуляторе {tariff_ru_name}"):
        logger.info(f"Текущий тариф на калькуляторе {tariff_ru_name}")

    return tariff_name


def get_amount_period_values(self) -> list[int]:
    calculator_values = self.locators.calculator_values.get_elements()._list
    return list(
        map(
            lambda x: int(re.findall(r"\d+", x.get_attribute("textContent"))[0]),
            calculator_values,
        )
    )


def iterate_through_requested_money_or_period_list(
    self,
    requested_money_or_period_list,
    expected_tariff: Tariff,
    handler="amount",
    final_move=None,
) -> None:
    for requested_money_or_period in requested_money_or_period_list:
        move_calculator_handlers(
            self, requested_money_or_period, handler=handler, final_move=final_move
        )
        if expected_tariff:
            check_current_tariff_name(self, expected_tariff.name)
            check_current_tariff_values(self, expected_tariff.name)


def check_current_tariff_name(self, expected_tariff: str) -> None:
    tariff_on_calculator = get_tariff_name_on_calculator(self)
    assert (
        tariff_on_calculator == expected_tariff
    ), f"Фактический тариф: '{tariff_on_calculator}' != ожидаемый '{expected_tariff}'"


def check_current_tariff_values(self, tariff_on_calculator) -> None:
    amount, period = get_amount_period_values(self)

    with allure.step(f"Значения на калькуляторе: [Сумма: {amount}, Срок: {period}]"):
        logger.info(f"Значения на калькуляторе: [Сумма: {amount}, Срок: {period}]")

    amount_range = Tariff[tariff_on_calculator].amount_range
    period_range = Tariff[tariff_on_calculator].period_range

    with allure.step(
        f"Параметры тарифа '{tariff_on_calculator}':\nСуммы: {amount_range}\nСроки: {period_range}"
    ):
        logger.info(
            f"Параметры тарифа '{tariff_on_calculator}':\nСуммы: {amount_range}\nСроки: {period_range}"
        )

    assert (amount in amount_range) and (
        period in period_range
    ), f"Некорретные условия тарифа на калькуляторе: [Сумма: {amount}, Срок: {period}, Тариф: {tariff_on_calculator}]"


def check_login_page_calculator_values(self, expected_amount, expected_period):
    amount, period = get_amount_period_values(self)

    with allure.step(f"Значения на калькуляторе: [Сумма: {amount}, Срок: {period}]"):
        logger.info(f"Значения на калькуляторе: [Сумма: {amount}, Срок: {period}]")

    assert amount == expected_amount and period == expected_period, (
        f"Значения на калькуляторе не совпадают:\n"
        + f"Фактическая и ожидаемая суммы: [{amount} != {expected_amount}]\n"
        + f"Фактический и ожидаемый сроки: [{period} != {expected_period}])"
    )


def move_calculator_handlers(
    self,
    requested_money_or_period,
    handler="amount",
    final_move=None,
) -> None:
    (
        amount_handler,
        period_handler,
    ) = self.locators.calculator_handlers_span.get_elements()._list

    amount, period = get_amount_period_values(self)

    main_handler, main_value, index = (
        (amount_handler, amount, 0)
        if handler == "amount"
        else (period_handler, period, 1)
    )

    step = -15 if requested_money_or_period < main_value else 15

    # Использовать реальные границы тарифов, потому что на фронте калькулятор жестко заточен под пороги, тоесть
    # CALCULATOR_REQUESTED_MONEY делать равным согласно шагам из тарифов:
    # от 3тыс до 10тыс минимальный шаг 500
    # от 10тыс до 30тыс минимальный шаг 1000
    # от 30тыс до 40тыс шаг 10тыс
    # от 40тыс до 100тыс шаг 20тыс
    # Исходя из этого и выбираются суммы. В противном случае калькулятор не поймет заданный шаг.

    # Лучше использовать шаг 15, потому что это универсальный шаг: 500, 1000, 10000, 20000

    error_flag = 0

    action = ActionChains(self.page.webdriver)
    while True:
        if error_flag == 50:
            raise Exception("Превышено количество сдвигов ползунка(50).Тест сломан")
        if requested_money_or_period == main_value:
            if final_move == "step_forward":
                action.click_and_hold(main_handler.web_element).move_by_offset(
                    15, 0
                ).release().perform()
            if final_move == "step_back":
                action.click_and_hold(main_handler.web_element).move_by_offset(
                    -15, 0
                ).release().perform()
            break
        else:
            action.click_and_hold(main_handler.web_element).move_by_offset(
                step, 0
            ).release().perform()
            main_value = get_amount_period_values(self)[index]
            error_flag += 1
        with allure.step(f"Сдвинуть ползунок на {step}px..."):
            logger.info(f"Сдвинуть ползунок на {step}px...")
