import os.path

from src.utils import get_grouped_list_card, get_top_transactions
from src.working_file import get_data_from_file
from config import TESTS_DIR

transaction = get_data_from_file(os.path.join(TESTS_DIR, "test.xls"))


def test_get_grouped_list_card(group_df_test):
    assert get_grouped_list_card(transaction) == group_df_test


def test_get_top_transaction(top_tr_test):
    assert get_top_transactions(transaction) == top_tr_test
