from unittest.mock import patch

from src.exetrnal_api import get_course_currency, get_stock_price


@patch("requests.get")
def test_get_course_currency(mock_get):
    list_ = ["USD"]
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 100}
    assert get_course_currency(currency=list_) == {"USD": 100}
    mock_get.assert_called()


@patch("requests.get")
def test_get_course_currency_fail(mock_get):
    mock_get.return_value.status_code = 201
    mock_get.return_value.json.return_value = {'result': 100}
    assert get_course_currency() == "Неуспешный запрос"
    mock_get.assert_called()


@patch("requests.get")
def test_get_stock_price(mock_get):
    list_ = ["AMZN", "GOOGL"]
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'c': 183.13,}
    assert get_stock_price(list_) == {'AMZN': 183.13, 'GOOGL': 183.13}
    mock_get.assert_called()


@patch("requests.get")
def test_get_stock_price_fail(mock_get):
    list_ = ["AMZN"]
    mock_get.return_value.status_code = 201
    mock_get.return_value.json.return_value = {'c': 100}
    assert get_stock_price(list_) == "Неуспешный запрос"
    mock_get.assert_called()
