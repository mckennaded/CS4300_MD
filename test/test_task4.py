import pytest
from src.task4 import calculatediscount

@pytest.mark.parametrize("price, discount, expected", [
    (100, 10, 90),
    (50.5, 20, 40.4),
    (200, 0, 200),
    (100, 100, 0)
])
def test_calculated_discount(price, discount, expected):
    assert pytest.approx(calculatediscount(price, discount), 0.01) == expected
