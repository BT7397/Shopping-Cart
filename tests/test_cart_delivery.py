import pytest

from src.cart_delivery import qualifies_free_delivery

@pytest.mark.parametrize(
    ("total_cents", "expected_result"),
    [
        (6000, True),   # qualifies for free delivery
        (4500, False),  # does not qualify for free delivery
        (0, False),     # does not qualify for free delivery
    ]
)
def test_qualifies_free_delivery_valid(total_cents, expected_result):
    assert qualifies_free_delivery(total_cents) == expected_result

def test_qualifies_free_delivery_invalid_type():
    with pytest.raises(TypeError):
        qualifies_free_delivery("1000")  # passing a string instead of an integer

def test_qualifies_free_delivery_invalid_value():
    with pytest.raises(ValueError):
        qualifies_free_delivery(-1000)  # passing a negative value

def test_qualifies_free_delivery_edge_case():
    assert qualifies_free_delivery(5000) == True  # edge case: exactly 5000 cents should qualify for free delivery