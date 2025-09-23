import pytest
from src.task3 import check_number, first_ten_primes, sum_1_to_100

@pytest.mark.parametrize("num, expected", [(7, "positive"), (-7, "negative"), (0, "zero")])
def test_check_number(num, expected):
    assert check_number(num) == expected

def test_first_ten_primes():
    assert first_ten_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_1_to_100():
    assert sum_1_to_100() == 5050
