from datetime import datetime

import pytest

from tixly.promo import InvalidPromo, discount_for
from tixly.refunds import refund_amount


def test_promo_codes_are_case_insensitive():
    assert discount_for("earlybird", datetime(2026, 11, 1, 12, 0)) == 0.20


def test_unknown_and_long_expired_codes():
    with pytest.raises(InvalidPromo, match="unknown"):
        discount_for("FREE100", datetime(2026, 11, 1))
    with pytest.raises(InvalidPromo, match="expired"):
        discount_for("EARLYBIRD", datetime(2027, 2, 1))


def test_no_refund_close_to_or_after_the_event():
    start = datetime(2026, 11, 20, 20, 0)
    assert refund_amount(100.0, start, datetime(2026, 11, 20, 10, 0)) == 0.0  # 10 hours before
    assert refund_amount(100.0, start, datetime(2026, 11, 20, 21, 0)) == 0.0  # after it started
