import logging
import os

from config import DATA_DIR, LOGS_DIR

import pandas as pd

logger = logging.getLogger("working_file")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "working_file.log"), encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_data_from_file(file_path: str) -> pd.DataFrame:
    """
    Функция чтения XLSX файла с операциями:
    :param file_path: Путь до файла с данными
    :return: Список словарей с операциями
    """

    abs_file_path = os.path.join(DATA_DIR, file_path)

    if not os.path.exists(abs_file_path):
        logger.error(f"Файла с таким именем {abs_file_path} не существует в этой дииректории")
        return f"Файл {file_path} не найден"

    try:
        if file_path.endswith(".xls"):
            logger.debug(f"{file_path} это XLS-файл")
            df_data = pd.read_excel(abs_file_path)
            logger.info(f"Файл {file_path} прочитан")

            return df_data
        else:
            logger.debug(f"{file_path} это не XLSX-файл")
            return []

    except Exception as e:
        logger.error(f"Ошибка {e} при чтении {file_path} файла")
        return []


if __name__ == '__main__':
    print(get_data_from_file("operations.xls"))
