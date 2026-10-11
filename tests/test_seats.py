import pytest

from tixly.seats import SeatMap, SoldOut


def test_group_in_an_empty_row():
    m = SeatMap({"A": 6})
    assert m.reserve_together("A", 3) == ["A1", "A2", "A3"]
    assert m.free_count("A") == 3


def test_a_seat_cannot_be_taken_twice():
    m = SeatMap({"A": 4})
    m.take("A1")
    assert not m.is_free("A1")
    with pytest.raises(ValueError):
        m.take("A1")


def test_sold_out():
    m = SeatMap({"B": 2})
    with pytest.raises(SoldOut):
        m.reserve_together("B", 3)
