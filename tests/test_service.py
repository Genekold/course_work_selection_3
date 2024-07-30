from src.services import investment_bank
from src.working_file import get_data_from_file


def test_investment_bank():
    df_data = get_data_from_file("operations.xls")
    assert investment_bank("2019-11", df_data, 50) == 3689.05

    df_data = get_data_from_file("test.xls")
    assert investment_bank("2019-11", df_data, 10) == 0