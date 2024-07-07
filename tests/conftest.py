import json
import os

import pandas as pd
import pytest

from config import ROOT_DIR, DATA_DIR


@pytest.fixture
def excel_operations_from_file():
    return (
        pd.DataFrame(
            {
                'Дата операции': ['31.12.2021 16:44:00'],
                'Дата платежа': ['31.12.2021'],
                'Номер карты': '*7197',
                'Статус': 'OK'
            }
        )
        .to_dict("records")
    )