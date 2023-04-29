import pytest
from main import random_password, confusing_characters


@pytest.mark.parametrize(
    "input, output",
    [
        ([15, True], 15),
        ([15, False], 15),
        ([19, False], 19),
        ([20, True], 20),
    ],
)
def test_random_password_generation_len(input, output):
    pwd = random_password(input[0], input[1])
    assert len(pwd) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ([15, True], False),
        ([20, True], False),
    ],
)
def test_random_password_generation_chars(input, output):
    pwd = random_password(input[0], input[1])
    assert any([x in pwd for x in confusing_characters]) == output


def test_raises_exception_on_non_int_argument():
    with pytest.raises(TypeError):
        random_password("a", True)


def test_raises_exception_on_non_bool_argument():
    with pytest.raises(TypeError):
        random_password(15, "a")


def test_raises_exception_on_zero_input():
    with pytest.raises(ValueError):
        random_password(0, True)


def test_raises_exception_on_negative_input():
    with pytest.raises(ValueError):
        random_password(-15, True)
