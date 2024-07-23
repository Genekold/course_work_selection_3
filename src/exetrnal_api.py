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


def get_course_currency( currency: list, amount: float = 1, to_currency: str = "RUB") -> dict|str:
    """
    Функция, котрая возрващает курс валюты по отношению к рублю
    :param amount: сумма по умолчанию 1
    :param currency: Опционально, валюта для получения курса по умолчанию currency = ["USD", "EUR"]
    :param to_currency: валюта по отншению к которой показан курс
    :return: курс валюты
    """
    load_dotenv()
    result = {}
    for currenc in currency:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        header = {"apikey": os.getenv("APILAYER_API_KEY")}
        params = {"amount": amount, "from": currenc, "to": to_currency}
        logger.debug(f"Данные запроса {header} - {params}")
        response = requests.get(url, headers=header, params=params)
        if response.status_code != 200:
            logger.debug(f"Неуспешный запрос {response.status_code}")
            return "Неуспешный запрос"
        data = response.json()
        logger.info(f"Ответ {data}")
        result[currenc] = round(data["result"], 4)

    return result


def get_stock_price(stock_list: list[str]) -> dict|str:
    """
    Функция, которая возвращает цены на указанные акции
    :param stock_list: лист с названиями акций.
    :return: словарь акция - цена
    """
    load_dotenv()
    result = {}
    url = "https://api.finnhub.io/api/v1/quote"
    for stock in stock_list:
        params = {"symbol": stock, "token": os.getenv("FINNHUB_API_KEY")}
        logger.debug(f"Параметры запроса {stock}, {os.getenv('FINNHUB_API_KEY')}")
        response = requests.get(url, params=params)
        if response.status_code != 200:
            logger.debug(f"Неуспешный запрос {response.status_code}")
            return "Неуспешный запрос"
        data = response.json()
        logger.info(f"Результат запроса {data}")
        result[stock] = data["c"]

    return result


if __name__ == '__main__':
    list_ = ["AMZN", "GOOGL"]
    print(get_stock_price(list_))
