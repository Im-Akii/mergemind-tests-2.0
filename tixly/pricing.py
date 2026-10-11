"""Order pricing: ticket price x quantity, an optional promo discount, and a per-ticket service fee."""

from __future__ import annotations

from dataclasses import dataclass

SERVICE_FEE_PER_TICKET = 2.50


def round_money(value: float) -> float:
    return round(value + 1e-9, 2)


@dataclass(frozen=True)
class Quote:
    tickets: float
    discount: float
    service_fee: float

    @property
    def total(self) -> float:
        return round_money(self.tickets - self.discount + self.service_fee)


def quote(unit_price: float, quantity: int, discount_rate: float = 0.0) -> Quote:
    """Price an order. The promo discount applies to tickets only; the service fee is charged per ticket."""
    if quantity < 1:
        raise ValueError("quantity must be at least 1")
    if not 0.0 <= discount_rate < 1.0:
        raise ValueError("discount_rate must be in [0, 1)")
    tickets = round_money(unit_price * quantity)
    discount = round_money(tickets * discount_rate)
    fee = round_money(SERVICE_FEE_PER_TICKET)
    return Quote(tickets=tickets, discount=discount, service_fee=fee)
