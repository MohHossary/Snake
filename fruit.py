from board import Board, CellOccupier


class Fruit(CellOccupier):

    score: int

    def __init__(self, board: Board, score: int = 1):
        self.score = score
        strt_loc = board.find_possible_location()
        super(Fruit, self).__init__(location=strt_loc)
        board.move_to(self, strt_loc)

    def move_to_random(self, board):
        loc = board.find_possible_location()
        self.location = loc
        board.move_to(self, loc)

    def print_to_console(self):
        score = self.score
        print(score, end='')