import pandas as pd

from src.utils import get_list_of_monthly_expenses
from src.working_file import get_data_from_file


def investment_bank(month: str, transactions: pd.DataFrame, limit: int) -> float:
    """
    Фукция ,которая возвращает сумму,  которую удалось бы отложить в «Инвесткопилку».
    :param month: месяц, для которого рассчитывается отложенная сумма (строка в формате 'YYYY-MM')
    :param transactions: pd.DataFrame, содержащий информаци юо транзакциях с датой операции и суммой операции
    :param limit:редел, до которого нужно округлять суммы операций (целое число).
    :return: сумма которую удалось бы отложить в в «Инвесткопилку».
    """

    list_spending = get_list_of_monthly_expenses(month, transactions)
    result = 0
    for spend in list_spending:
        division = spend // limit
        result += ((limit * division) + limit) - spend

    return round(result, 2)


if __name__ == "__main__":
    path_file = "operations.xls"
    df_data = get_data_from_file(path_file)
    print(investment_bank("2019-11", df_data, 50))
