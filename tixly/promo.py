"""Promo codes. A code is valid up to and including its expiry date."""

from __future__ import annotations

from datetime import date, datetime, time

PROMOS: dict[str, tuple[float, date]] = {
    "EARLYBIRD": (0.20, date(2026, 12, 31)),
    "STUDENT": (0.15, date(2027, 6, 30)),
}


class InvalidPromo(ValueError):
    pass


def discount_for(code: str, now: datetime) -> float:
    """Discount rate for a promo code at time `now` (codes are case-insensitive)."""
    key = code.strip().upper()
    if key not in PROMOS:
        raise InvalidPromo(f"unknown promo code: {code}")
    rate, expires = PROMOS[key]
    if now > datetime.combine(expires, time.min):
        raise InvalidPromo(f"promo code {key} has expired")
    return rate
