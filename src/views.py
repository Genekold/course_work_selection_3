import json

from src.widget import get_hello_message_from_time
from src.utils import get_grouped_list_card, get_top_transactions
from src.exetrnal_api import get_course_currency, get_stock_price
from src.working_file import get_data_from_file


def data_for_web_page(date: str) -> json:
    """
    Функция собирает данные и формирует ответ в виде JSON-файла для главной веб страницы
    :return:JSON-файл с данными(приветствие, расходы по каждой карте, топ 5 танзакий, курс валют, стоимость акций.
    """

    path_file = "operations.xls"
    list_currency = ["CNY", "USD"]
    list_stock = ["TSLA", "GOOGL"]

    message = get_hello_message_from_time()  # получение сообщения по времени суток
    df_data = get_data_from_file(path_file)  # получение df по картам из файла
    cards = get_grouped_list_card(df_data)  # получение расходов по картам
    top_transaction = get_top_transactions(df_data)  # получение топ 5 транзакций
    currency_rates = get_course_currency(list_currency)  # получение курса валют
    stock_price = get_stock_price(list_stock)  # получение стоимости акций
    responce = {
        "greeting": message,
        "cards": cards,
        "top_transactions": top_transaction,
        "currency_rates": currency_rates,
        "stock_prices": stock_price
    }

    return json.dumps(responce, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    date = "2024-04-12 12:22:22"

    print(data_for_web_page(date))
