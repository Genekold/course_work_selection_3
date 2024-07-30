import os

from config import TESTS_DIR, DATA_DIR
from src.working_file import get_data_from_file
from unittest.mock import patch, mock_open

abs_path = os.path.join(DATA_DIR, "operations.xls")
tests_path = os.path.join(DATA_DIR, "test.xl")


@patch('pandas.read_excel')
def test_get_data_from_file(mock_read_xls):
    mock_read_xls.return_value = [{
        'Дата платежа': '31.12.2021',
        'Статус': 1}]
    assert get_data_from_file(abs_path) == [{
        'Дата платежа': '31.12.2021',
        'Статус': 1}]
    mock_read_xls.assert_called()


@patch('pandas.read_excel')
def test_get_data_from_file_error(mock_read_xls):
    mock_read_xls.side_effect = Exception
    assert get_data_from_file(abs_path) == None
    mock_read_xls.assert_called()


@patch('pandas.read_excel')
def test_get_data_from_not_file(mock_read_xls):
    mock_read_xls.return_value = [{
        'Дата платежа': '31.12.2021',
        'Статус': 1,
    }]
    assert get_data_from_file("test.xlsx") == "Файл test.xlsx не найден"




@patch('pandas.read_excel')
def test_get_data_from_not_xlsx(mock_read_xls):
    mock_read_xls.return_value = [{
        'Дата платежа': '31.12.2021',
        'Статус': 1,
    }]
    assert get_data_from_file(tests_path) == None
