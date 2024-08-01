import logging
import os
from datetime import datetime, timedelta

import pandas as pd

from config import LOGS_DIR
from src.working_file import get_data_from_file

logger = logging.getLogger("reports")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "reports.log"), encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
    logger.debug(f"Дата запроса в формате {date}")

    start_date = date - timedelta(days=90)
    logger.debug(f"Дата начала периода поиска {start_date}")

    filtred_df = transactions.loc[(pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y").
                                   between(start_date, date))]
    logger.debug(f"Отсартирован по дате {filtred_df.shape}")
    filtred_df = filtred_df.loc[transactions["Категория"] == category]
    logger.debug(f"Отсартирован по категории {filtred_df.shape}")

    return filtred_df


if __name__ == '__main__':
    df = get_data_from_file("operations.xls")
    print(spending_by_category(df, "Бонусы", "2021-05-12"))
