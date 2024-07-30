import logging
import os

import pandas as pd

from config import LOGS_DIR
from src.working_file import get_data_from_file

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_grouped_list_card(transactions: pd.DataFrame) -> list[dict]:
    """
    Функция возврщает сумму опреаций по картам и кэшбэк 1% от операции
    :param transaction: pd.DataFrame с операциями по картам
    :return: список словарей с суммой операций по карте и размерм кэшбэка
    """
    operstions = transactions[(transactions["Номер карты"].notna()) & (transactions["Сумма операции"] < 0.0)]
    logger.debug(f"Создан новый df {operstions.shape}")
    list_transactions = []

    operstions_group = operstions.groupby(["Номер карты"]).agg({"Сумма операции": "sum"})
    logger.debug(f"Сгруппированый df по номерам карт \n{operstions_group.head()}")
    card_group_dict = operstions_group.to_dict("index")

    for card_number, sum_opration in card_group_dict.items():
        cashback = round(abs(sum_opration["Сумма операции"]) / 100)

        list_transactions.append(
            {"card_number": card_number, "sum_opertation": sum_opration["Сумма операции"], "cashback": cashback}
        )
    return list_transactions


def get_top_transactions(transaction: pd.DataFrame) -> list[dict]:
    """
    Функция которая озвращает список топ пять транзакций по сумме платежа
    :param transaction: pd.DataFrame с операциями по картам
    :return: список словарей из пяти самфх крупных операций
    """
    result = []
    sort_df = transaction.sort_values("Сумма операции")
    logger.debug(f"df отсортирован по сумме операции \n{sort_df.head(3)}")
    top_transaction = sort_df[:5].to_dict("records")
    for one_transaction in top_transaction:
        result.append(
            {
                "date": one_transaction["Дата платежа"],
                "amount": one_transaction["Сумма операции"],
                "category": one_transaction["Категория"],
                "description": one_transaction["Описание"],
            }
        )
    logger.info(f"{result[0]}")

    return result


def get_list_of_monthly_expenses(month: str, transactions: pd.DataFrame) -> list:
    """
    Функция возвращает список трат за месяц
    :param month: месяц, для которого выбирается список (строка в формате 'YYYY-MM')
    :param transaction: transaction: pd.DataFrame с операциями по картам
    :return: список трат за месяц содежит дату и сумму транзакции
    """
    format_date = f"{month[-2:]}.{month[:4]}"
    spending = transactions[transactions["Сумма платежа"] < 0]
    df = spending[["Дата операции", "Сумма платежа"]]
    dict_spending = df.to_dict("index")
    result = []
    for operation in dict_spending.values():
        if operation["Дата операции"][3:10] == format_date:
            result.append(operation["Сумма платежа"] * -1)

    return result


if __name__ == "__main__":
    list_ = get_data_from_file("test.xls")

    print(get_top_transactions(list_))
