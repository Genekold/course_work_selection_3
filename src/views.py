import os.path

from src.utils import get_grouped_list_card,get_top_transactions
from src.working_file import get_data_from_file
from config import TESTS_DIR


trans = get_data_from_file(os.path.join(TESTS_DIR, "test.xls"))

print(get_top_transactions(trans))