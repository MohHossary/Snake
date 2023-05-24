import sys
from snake import Snake  # SnakeSegment
from board import Board
from fruit import Fruit
from clock import Clock, ClockListener
from wallbuilder import WallBuilder, NoWallsBuilder, HorizontalWallsBuilder, VerticalWallsBuilder, AllWallsBuilder
from keyboardhandler import KeyboardHandler
from libkeyboardkeyboardhandler import LibkeyboardKeyboardHandler
import random as rdm


class Controller(ClockListener):

    board: Board
    snake: Snake
    fruit: Fruit
    clock: Clock
    walls:  WallBuilder
    handler: KeyboardHandler

    def init_game(self):
        # wallrandom = rdm.randrange(1,4)
        # if wallrandom == 1:
        #     self.walls: WallBuilder = NoWallsBuilder()
        # elif wallrandom == 2:
        #     self.walls: WallBuilder = HorizontalWallsBuilder()
        # else:
        #     self.walls: WallBuilder = VerticalWallsBuilder()

        self.walls = rdm.choice([NoWallsBuilder(), VerticalWallsBuilder(), HorizontalWallsBuilder(), AllWallsBuilder()])

        self.board: Board = Board(10, 10)
        self.walls.build_walls(self.board)
        self.snake = Snake(self.board)
        self.fruit = Fruit(self.board)
        # head: Head = cast(snake.all_segments[0], Head)
        # head: SnakeSegment = self.snake.all_segments[0]
        self.board.print_to_console()
        self.handler = LibkeyboardKeyboardHandler()

    def start_game(self):
        self.clock = Clock()
        self.clock.add_listener(self)
        self.clock.start()

    def clock_ticked(self):
        snake = self.snake
        board = self.board
        fruit = self.fruit

        if self.handler.is_up_pressed():
            snake.up_pressed()
        elif self.handler.is_down_pressed():
            snake.down_pressed()
        elif self.handler.is_left_pressed():
            snake.left_pressed()
        elif self.handler.is_right_pressed():
            snake.right_pressed()
        next_location = snake.next_location(board)
        if board.is_empty(next_location):
            snake.step(board)
        elif self.fruit.is_overlapping(next_location):
            snake.eat(fruit, board)
            snake.grow(board)
            snake.step(board)
            fruit.move_to_random(board)
            self.clock.speed_up()
        elif self.walls.is_overlapping(next_location):
            snake.die()
        elif snake.is_overlapping(next_location):
            snake.die()

        board.print_to_console()


def main(argv):
    controller = Controller()
    controller.init_game()
    controller.start_game()


if __name__ == '__main__':
    main(sys.argv)
