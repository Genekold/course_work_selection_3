import pandas as pd

from src.working_file import get_data_from_file


def get_grouped_list_card(transaction: pd.DataFrame) -> list[dict]:
    """
    Функция возврщает сумму опреаций по картам и кэшбэк 1% от операции
    :param transaction: pd.DataFrame с операциями по картам
    :return: список словарей с суммой операций по карте и размерм кэшбэка
    """
    operstions = transaction[["Номер карты", "Сумма операции с округлением"]]
    list_transactions = []

    operstions_group = operstions.groupby(["Номер карты"]).agg({"Сумма операции с округлением": "sum"})
    card_group_dict = operstions_group.to_dict("index")

    for card_number, sum_opration in card_group_dict.items():
        cashback = round(abs(sum_opration["Сумма операции с округлением"]) / 100)

        list_transactions.append({
            "card_number": card_number,
            "sum_opertation": sum_opration["Сумма операции с округлением"],
            "cashback": cashback
        })
    return list_transactions


if __name__ == '__main__':
    list_operation = get_data_from_file("operations.xls")
    print(get_grouped_list_card(list_operation))
