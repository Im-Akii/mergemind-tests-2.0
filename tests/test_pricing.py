import pytest

from tixly.pricing import quote


def test_single_ticket():
    q = quote(40.0, 1)
    assert (q.tickets, q.discount, q.service_fee, q.total) == (40.0, 0.0, 2.5, 42.5)


def test_promo_discount_applies_to_tickets_only():
    q = quote(40.0, 1, discount_rate=0.2)
    assert q.discount == 8.0
    assert q.total == 34.5  # 40 - 8 + 2.50 fee


def test_invalid_orders():
    with pytest.raises(ValueError):
        quote(40.0, 0)
    with pytest.raises(ValueError):
        quote(40.0, 1, discount_rate=1.5)
