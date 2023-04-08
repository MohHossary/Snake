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
        for block in self.blocks:
            if block.is_overlapping(location):
                return True
        # else:
        #     return False
        return False

    def __build_brick(self, location, board):
        ws = WallSegment(location)
        board.move_to(ws, location)
        self.blocks.append(ws)


class NoWallsBuilder(WallBuilder):
    def build_walls(self, board: Board):
        pass


class VerticalWallsBuilder(WallBuilder):

    def build_walls(self, board: Board):
        for i in range(board.rows):
            self.__build_brick((0, i), board)
            self.__build_brick((board.cols - 1, i), board)


class HorizontalWallsBuilder(WallBuilder):
    def build_walls(self, board: Board):
        # for every position related to the upper row, i.e. (x, 0)
        #     create a wall segment
        #     and put it in its location
        #     add it to the list
        for i in range(board.cols):
            self.__build_brick((i, 0), board)
            self.__build_brick((i, board.rows - 1), board)


class AllWallsBuilder(WallBuilder):
    def build_walls(self, board: Board):
        for i in range(board.rows):
            self.__build_brick((0, i), board)
            self.__build_brick((board.cols - 1, i), board)

        for i in range(1, board.cols - 1):
            self.__build_brick((i, 0), board)
            self.__build_brick((i, board.rows - 1), board)
