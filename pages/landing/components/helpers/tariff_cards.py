import re

from utils.constants.features import Tariff
from utils.webdriver.logger import logger


def get_amount_period_from_url(url: str) -> tuple[int, int]:
    amount = 0
    period = 0

    amount_match = re.search(r"amount=(\d+)", url)
    period_match = re.search(r"days=(\d+)", url)

    if amount_match and period_match:
        amount = int(amount_match.group(1))
        period = Tariff.get_day_to_week_period(int(period_match.group(1)))
    else:
        logger.info("Нет суммы и срока займа (queries) в ссылке")

    return amount, period
