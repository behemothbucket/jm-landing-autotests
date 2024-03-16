from enum import Enum
from itertools import chain


class Feature(str, Enum):
    CLIENTS = "Clients"


class Account(str, Enum):
    PHONE = "*-*-*-*-*-*-"
    DEFAULT_PASSWORD = "*-*-*-*-*-*-"


class Tariff(Enum):
    MEGA_START = (
        "MEGA_START",
        "Мега-старт",
        "start",
        list(reversed(range(3000, 10500, 500))),
        list(range(10, 31)),
    )
    PRAKTIK = (
        "PRAKTIK",
        "Практик",
        "middle",
        list(range(11000, 31000, 1000)),
        list(range(10, 31)),
    )
    PROFI = (
        "PROFI",
        "Профи",
        "end",
        list(chain(range(25000, 31000, 1000), range(40000, 101000, 20000))),
        [10, 16, 20, 24],
    )

    def __new__(
        cls,
        value: str,
        ru_name: str,
        locator: str,
        amount_range: list,
        period_range: list,
    ) -> "Tariff":
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(
        self,
        value: str,
        ru_name: str,
        locator: str,
        amount_range: list,
        period_range: list,
    ) -> None:
        self.ru_name = ru_name
        self.locator = locator
        self.amount_range = amount_range
        self.period_range = period_range

    @staticmethod
    def get_by(predicate: str, ru: bool = False) -> str:
        return {
            "start": Tariff.MEGA_START.ru_name if ru else Tariff.MEGA_START.name,
            "middle": Tariff.PRAKTIK.ru_name if ru else Tariff.PRAKTIK.name,
            "end": Tariff.PROFI.ru_name if ru else Tariff.PROFI.name,
        }[predicate]

    @staticmethod
    def get_day_to_week_period(days: int) -> int:
        return {
            70: 10,
            112: 16,
            140: 20,
            168: 24,
        }[days]


class LandingText(Enum):
    GET_LOAN_STEPS_TEXT = (
        "Оформите заявку\nВремя оформления заявки менее 5 минут\n"
        + "Дождитесь решения\nСреднее время рассмотрения заявки составляет 2 минуты\n"
        + "Получите деньги\nВ течение нескольких минут получите деньги на банковскую карту"
    )

    PAY_LOAN_VARIANTS_TEXT = (
        "Быстрая оплата на сайте\nБанковской картой\nЭлектронный кошелек\nНаличными"
    )

    BURGER_MENU_PROMO_TEXT = (
        "Дарим промокод на новый заём под 0%\nЗимний скидкопад в Joymoney\nПОДРОБНЕЕ"
    )

    TARIFF_CARDS_DESCRIPTIONS_TEXT = [
        "Мега Старт0%* первый заём Сумма займадо 10 000 руб.Срок займадо 21 дняПродление срока "
        "займаДаСтавка0%**Ставка по займу 0% при условии погашения займа в срок до 21 дня, при погашении займа в срок "
        "от 22 дней ставка составит 0,8% в день за весь срок пользования займом. ПСК — от 0,000% до 292,"
        "000% годовыхПолучить деньги",
        "Практик до 29 000 руб. Сумма займадо 29 000 руб.Срок займа10-30 днейПродление срока займаДаСтавка0,"
        "8%/деньПСК — 292,000% годовыхПолучить деньги",
        "Профи до 100 000 руб. Сумма займадо 100 000 руб.Срок займа10-24 неделиСтавка0,6-0,8%/деньПСК — от 219,"
        "000% до 292,000% годовыхПолучить деньги",
    ]
