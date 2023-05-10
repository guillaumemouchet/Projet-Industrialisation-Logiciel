import pytest
from main import random_password


def test_log_generation():

    filename = "./logger/log.txt"
    with open(filename) as f:
        nb_lines_before = sum(1 for _ in f)

    random_password(15, True)

    with open(filename) as f:
        nb_lines_after = sum(1 for _ in f)

    assert nb_lines_before == (nb_lines_after - 1)

    with open(filename, "r") as f:
        log = f.readlines()[-1]

    params = "15 True"
    found = log.find(params)
    assert found != -1
