from src.reports import spending_by_category
from src.working_file import get_data_from_file


def test_spending_by_category():
    test_data = "2021-12-31"
    test_df = get_data_from_file("test.xls")
    test_category = "Каршеринг"

    result = spending_by_category(test_df, test_category, test_data)
    assert len(result) == 2

def test_spending_by_category_none_date():
    test_df = get_data_from_file("test.xls")
    test_category = "Каршеринг"

    result = spending_by_category(test_df, test_category)
    assert len(result) == 0