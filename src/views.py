import datetime
import json
import logging
import os
from typing import Any

from config import LOGS_DIR
from src.exetrnal_api import get_course_currency, get_stock_price
from src.utils import get_grouped_list_card, get_top_transactions
from src.widget import get_hello_message_from_time
from src.working_file import get_data_from_file

logger = logging.getLogger("views")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "views.log"), encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def data_for_web_page(date: str = datetime.datetime.today()) -> Any:
    """
    Функция собирает данные и формирует ответ в виде JSON-файла для главной веб страницы
    :return:JSON-файл с данными(приветствие, расходы по каждой карте, топ 5 танзакий, курс валют, стоимость акций.
    """

    path_file = "operations.xls"
    list_currency = ["CNY", "USD"]
    list_stock = ["TSLA", "GOOGL"]

    message = get_hello_message_from_time(date)  # получение сообщения по времени суток
    logger.info(f"{message}")
    df_data = get_data_from_file(path_file)  # получение df по картам из файла
    cards = get_grouped_list_card(df_data)  # получение расходов по картам
    logger.info(f"Прочитан файл {path_file}")
    top_transaction = get_top_transactions(df_data)  # получение топ 5 транзакций
    logger.info(f"топ {top_transaction[0]}")
    currency_rates = get_course_currency(list_currency)  # получение курса валют
    stock_price = get_stock_price(list_stock)  # получение стоимости акций
    logger.debug(f"курс {currency_rates}, цена {stock_price}")
    responce = {
        "greeting": message,
        "cards": cards,
        "top_transactions": top_transaction,
        "currency_rates": currency_rates,
        "stock_prices": stock_price,
    }

    return json.dumps(responce, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # date = "2024-04-12 12:22:22"

    print(data_for_web_page())
