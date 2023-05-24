from abc import ABC, abstractmethod
from typing import Tuple, List

from board import Board, CellOccupier


class WallSegment(CellOccupier):

    def __init__(self, location: Tuple[int, int]):
        super(WallSegment, self).__init__(location=location)

    def print_to_console(self):
        print('#', end='')


class WallBuilder(ABC):
    blocks: List[WallSegment] = []

    @abstractmethod
    def build_walls(self, board: Board):
        pass

    def is_overlapping(self, location: Tuple[int, int]) -> bool:
        for brick in self.blocks:
            if brick.is_overlapping(location):
                return True
        return False

    def build_brick(self, location, board):
        wallseg = WallSegment(location)
        board.move_to(wallseg, location)
        self.blocks.append(wallseg)


class NoWallsBuilder(WallBuilder):
    def build_walls(self, board: Board):
        pass


class VerticalWallsBuilder(WallBuilder):

    def build_walls(self, board: Board):
        for x in range(board.rows):
            location = (0, x)
            self.build_brick(location, board)
        for x in range(board.rows):
            location = (board.cols - 1, x)
            self.build_brick(location, board)


class HorizontalWallsBuilder(WallBuilder):
    def build_walls(self, board: Board):
        for x in range(board.cols):
            location = (x, 0)
            self.build_brick(location, board)
        for x in range(board.cols):
            location = (x, board.rows - 1)
            self.build_brick(location, board)


class AllWallsBuilder(WallBuilder):
    def build_walls(self, board: Board):
        for x in range(1, board.rows - 1):
            location = (0, x)
            self.build_brick(location, board)
        for x in range(1, board.rows - 1):
            location = (board.cols - 1, x)
            self.build_brick(location, board)

            for x in range(board.cols):
                location = (x, 0)
                self.build_brick(location, board)
            for x in range(board.cols):
                location = (x, board.rows - 1)
                self.build_brick(location, board)