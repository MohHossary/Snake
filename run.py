import sys
import time
import pygame
import resources
from snake import Snake  # SnakeSegment
from board import Board
from fruit import Fruit
from clock import Clock, ClockListener
from wallbuilder import WallBuilder, NoWallsBuilder, HorizontalWallsBuilder, VerticalWallsBuilder, AllWallsBuilder
from libpygamekeyboardhandler import LibpygameKeyboardHandler
import random as rdm
from GUI import PygameBoard


class Controller(ClockListener):

    pygame.mixer.init()
    board: Board
    snake: Snake
    fruit: Fruit
    clock: Clock
    walls:  WallBuilder
    handler: LibpygameKeyboardHandler = None
    pygameBoard: PygameBoard = None


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
        self.handler = LibpygameKeyboardHandler()
        self.pygameBoard = PygameBoard(self.board, self.snake)

    def start_game(self):
        resources.bg_sound.play(loops=-1)
        self.clock = Clock()
        self.clock.add_listener(self)
        self.clock.add_listener(self.pygameBoard)
        self.clock.start()
        while self.clock.active:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.handler.consume_input(event)
                elif event.type == pygame.QUIT:
                    # running = False
                    self.clock.stop()
                    pygame.quit()
                    sys.exit()

    def clock_ticked(self):
        snake = self.snake
        board = self.board
        fruit = self.fruit

        if self.handler and self.handler.is_up_pressed():
            snake.up_pressed()
        elif self.handler and self.handler.is_down_pressed():
            snake.down_pressed()
        elif self.handler and self.handler.is_left_pressed():
            snake.left_pressed()
        elif self.handler and self.handler.is_right_pressed():
            snake.right_pressed()
        next_location = snake.next_location(board)
        if board.is_empty(next_location):
            snake.step(board)
        elif self.fruit.is_overlapping(next_location):
            snake.eat(fruit)
            snake.grow(board)
            snake.step(board)
            fruit.move_to_random(board)
            self.clock.speed_up()
        elif self.walls.is_overlapping(next_location):
            self.lose()
        elif snake.is_overlapping(next_location):
            self.lose()

        board.print_to_console()

    def lose(self):
        self.clock.stop()
        resources.bg_sound.stop()
        self.snake.die()
        time.sleep(4.0)


def main(argv):
    controller = Controller()
    controller.init_game()
    controller.start_game()


if __name__ == '__main__':
    main(sys.argv)
