from typing import Tuple

from board import Board, CellOccupier


class Fruit(CellOccupier):

    score: int

    def __init__(self, board: Board, score: int = 1):
        self.score = score
        loc = board.find_possible_location()
        super(Fruit, self).__init__(location=loc)
        self.move_to(loc, board)

    def move_to_random(self, board) -> Tuple[int, int]:
        # 1) find an empty location
        empty = board.find_possible_location()
        # 2) call move_to(possible_loc, board)
        self.move_to(empty, board)
        return empty
#        print(self.location)

    def print_to_console(self):
        score = self.score
        print(score, end='')

    #    def eaten(self):
#        del self
#        pass

    # def __del__(self):
    #     print('destructor of', self)


# if __name__ == '__main__':
#     f1 = Fruit(5)
#     f2 = Fruit()
#     print(f1.score)
#     print(f2.score)
#     # f1.eaten()
#     print('after calling eaten')
#     f3 = f1
#     del f1
#     del f3
#     print('after deleting all references to the 5 score fruit')
#     # f2.eaten()
#     # f2.score
#     print('after deleting all references to the 1 score fruit')
#
#     # print(f3.score)
