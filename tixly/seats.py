"""Seat maps: rows of numbered seats; groups are seated next to each other."""

from __future__ import annotations


class SoldOut(Exception):
    pass


class SeatMap:
    def __init__(self, rows: dict[str, int]):
        """rows: {"A": 10, "B": 12} -> row A has seats A1..A10."""
        self.taken: dict[str, list[bool]] = {row: [False] * n for row, n in rows.items()}

    def is_free(self, seat: str) -> bool:
        row, number = seat[0], int(seat[1:])
        return not self.taken[row][number - 1]

    def take(self, seat: str) -> None:
        row, number = seat[0], int(seat[1:])
        if self.taken[row][number - 1]:
            raise ValueError(f"{seat} is already taken")
        self.taken[row][number - 1] = True

    def reserve_together(self, row: str, count: int) -> list[str]:
        """Reserve `count` adjacent free seats in `row` (the first block that fits) and return them."""
        seats = self.taken[row]
        run_start, run_len = 0, 0
        for i, taken in enumerate(seats):
            if not taken:
                if run_len == 0:
                    run_start = i
                run_len += 1
            else:
                run_len = 0
            if run_len == count:
                block = [f"{row}{n + 1}" for n in range(run_start, run_start + count)]
                for s in block:
                    seats[int(s[1:]) - 1] = True
                return block
        raise SoldOut(f"no {count} adjacent seats left in row {row}")

    def free_count(self, row: str) -> int:
        return sum(1 for t in self.taken[row] if not t)
