import pandas as pd
import pytest


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


@pytest.fixture
def group_df_test():
    return [{'card_number': '*1234', 'sum_opertation': -4100, 'cashback': 41},
            {'card_number': '*4556', 'sum_opertation': -1000, 'cashback': 10},
            {'card_number': '*5091', 'sum_opertation': -1500, 'cashback': 15},
            {'card_number': '*7197', 'sum_opertation': -600, 'cashback': 6}]


@pytest.fixture
def top_tr_test():
    return [{'date': '24.11.2021', 'amount': -2000, 'category': 'Ж/д билеты', 'description': 'РЖД'},
            {'date': '22.10.2021', 'amount': -2000, 'category': 'Ж/д билеты', 'description': 'РЖД'},
            {'date': '24.11.2021', 'amount': -1000, 'category': 'Каршеринг', 'description': 'Ситидрайв'},
            {'date': '31.12.2021', 'amount': -600, 'category': 'Переводы', 'description': 'Константин Л.'},
            {'date': '31.12.2021', 'amount': -500, 'category': 'Различные товары', 'description': 'Ozon.ru'}]
