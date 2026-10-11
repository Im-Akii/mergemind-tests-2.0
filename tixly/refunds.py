"""Refund policy: full refund up to 48 hours before the event starts, none after that."""

from __future__ import annotations

from datetime import datetime

REFUND_WINDOW_HOURS = 48


def hours_until(event_start: datetime, now: datetime) -> float:
    return (event_start - now).seconds / 3600


def refund_amount(paid: float, event_start: datetime, now: datetime) -> float:
    if now >= event_start:
        return 0.0
    if hours_until(event_start, now) >= REFUND_WINDOW_HOURS:
        return paid
    return 0.0
