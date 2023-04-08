from __future__ import annotations

import random as rdm
from abc import ABC, abstractmethod
from typing import Optional, Tuple, List


class CellOccupier(ABC):
    location: Tuple[int, int]

    def __init__(self, location):
        self.location = location

    def move_to(self, location, b: Board):
        b.move_to(self, location)

    @abstractmethod
    def print_to_console(self):
        pass

    def is_overlapping(self, location: Tuple[int, int]) -> bool:
        return self.location == location


class Board:
    __arr: List[List[Optional[CellOccupier]]]
    rows: int
    cols: int

    def __init__(self, rows=5, cols=7):
        self.rows, self.cols = rows, cols
        self.__arr = [[None] * rows for _ in range(cols)]

    def find_possible_location(self) -> Tuple[int, int]:
        while True:
            x = rdm.randrange(0, self.cols)
            y = rdm.randrange(0, self.rows)
            if self.__arr[x][y] is None:
                return x, y

    def print_to_console(self):
        print()
        print()
        for y in range(self.rows):
            for x in range(self.cols):
                cell = self.__arr[x][y]
                if cell is None:
                    print('-', end='')
                elif isinstance(cell, CellOccupier):
                    co: CellOccupier = cell
                    co.print_to_console()
            print()

    def put_object(self, item, location):
        item.location = location
        if location != (-1, -1):
            self.__arr[location[0]][location[1]] = item

    def remove_object(self, item: CellOccupier):
        x, y = location = item.location
        if location != (-1, -1) and self.__arr[x][y] == item:
            self.__arr[x][y] = None

    def move_to(self, item, new_location: Tuple[int, int]):
        self.remove_object(item)
        self.put_object(item, new_location)

    def is_empty(self, location: Tuple[int, int]) -> bool:
        return self.__arr[location[0]][location[1]] is None


if __name__ == '__main__':
    board = Board()
    board.print_to_console()
