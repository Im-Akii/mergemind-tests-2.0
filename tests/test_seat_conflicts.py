from tixly.seats import SeatMap


def test_group_never_gets_a_taken_seat():
    m = SeatMap({"A": 6})
    m.take("A2")
    assert m.reserve_together("A", 2) == ["A3", "A4"]
