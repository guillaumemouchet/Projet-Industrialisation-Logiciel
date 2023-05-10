import pytest
from main import random_password

import re


def replace_datetime(log):
    # Datetime pattern https://stackoverflow.com/questions/51224/regular-expression-to-match-valid-dates and https://stackoverflow.com/questions/7536755/regular-expression-for-matching-hhmm-time-format
    datetime_pattern = r"(0?[1-9]|1[0-2]):[0-5][0-9] (0?[1-9]|[12]\d|30|31)\.(0?[1-9]|1[0-2])\.(\d{4}|\d{2})"

    match = re.search(datetime_pattern, log)

    if match:
        replacement_string = "hh:mm DD-MM-YYYY"
        modified_string = re.sub(datetime_pattern, replacement_string, log)
        return modified_string

    return log


def get_log():
    with open("./logger/log.txt", "r") as f:
        last_line = f.readlines()[-1]
    return replace_datetime(last_line)


def test_regression_log(data_regression):
    random_password(15, True)
    data_regression.check(get_log())
