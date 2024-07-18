import logging
import os

import requests
from dotenv import load_dotenv

from config import LOGS_DIR

logger = logging.getLogger("external_api")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "external_api"), encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_course_currency(amount: float = 1, currency: str = "USD", to_currency: str = "RUB") -> float:
    """
    Функция, котрая возрващает курс валюты по отношению к рублю
    :param amount: сумма по умолчанию 1 (
    :param currency: валюта для получения курса по умолчанию USD
    :param to_currency: валюта по отншению к которой показан курс
    :return: курс валюты
    """
    load_dotenv()
    url = "https://api.apilayer.com/exchangerates_data/convert"
    header = {"apikey": os.getenv("API_KEY_CURENCY")}
    params = {"amount": amount, "from": currency, "to": to_currency}
    logger.debug(f"Данные запроса {header} - {params}")
    response = requests.get(url, headers=header, params=params)
    if response.status_code != 200:
        logger.debug(f"Неуспешный запрос {response.status_code}")
        return "Неуспешный запрос"
    data = response.json()
    logger.info(f"Ответ {data}")
    exchange_rates = round(data["result"], 4)

    return exchange_rates


if __name__ == '__main__':
    print(get_course_currency(currency="EUR"))
