from datetime import datetime, timedelta

import pandas as pd

from src.working_file import get_data_from_file


def spending_by_category(transactions: pd.DataFrame, category: str, date: str = None) -> pd.DataFrame:
    """
    Функция возвращает траты по заданной категории за последние три месяца (от переданной даты).
    :param transactions: датафрейм с транзакциями,
    :param category: название категории.
    :param date: опционально дату, если дата не опеределена устанавливается текущая дата.
    :return:
    """

    if date:
        date = datetime.strptime(date, "%Y-%m-%d")
        print(date)
    else:
        date = datetime.now()
        print(date)
    start_date = date - timedelta(days=1100)

    filtred_df = transactions.loc[(pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y").
                                   between(start_date, date))]
    filtred_df = filtred_df.loc[transactions["Категория"] == category]

    return filtred_df.head()


if __name__ == '__main__':
    df = get_data_from_file("operations.xls")
    print(spending_by_category(df, "Бонусы"))
