import pytest
from src.cart_total import calculate_total

@pytest.mark.parametrize(
    ("unit_price_cents", "quantity", "expected_total"),
    [
        (1000, 3, 3000),  # $10.00 * 3 = $30.00
        (500, 2, 1000),   # $5.00 * 2 = $10.00
        (2000, 1, 2000),  # $20.00 * 1 = $20.00
    ]
)

def test_calculate_total_valid(unit_price_cents, quantity, expected_total):
    assert calculate_total(unit_price_cents, quantity) == expected_total

def test_calculate_total_zero_quantity():
    assert calculate_total(1000, 0) == 0  # zero quantity should return 0

def test_calculate_total_zero_price():
    assert calculate_total(0, 5) == 0  # zero price should return 0

def test_calculate_total_zero_price_and_quantity():
    assert calculate_total(0, 0) == 0  # zero price and quantity should return 0

@pytest.mark.parametrize(
    ("unit_price_cents", "quantity"),
    [
        (-1000, 3),  # negative price
        (1000, -3),  # negative quantity
        (-1000, -3), # both negative
    ]
)

def test_calculate_total_invalid(unit_price_cents, quantity):
    with pytest.raises(ValueError):
        calculate_total(unit_price_cents, quantity)