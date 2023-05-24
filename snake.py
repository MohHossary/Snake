import sys
from abc import ABC
from os import system
from typing import List, Tuple
import random as rdm
from board import Board, CellOccupier
from fruit import Fruit


class SnakeSegment(CellOccupier, ABC):
    direction: str
    alive = True

    def __init__(self, location, direction: str, board: Board):
        super().__init__(location)
        self.location = location
        self.direction = direction
        self.move_to(location, board)

    def move_to(self, location: Tuple[int, int], board: Board):
        board.move_to(self, location)

    def die(self):
        self.alive = False


class Head(SnakeSegment):
    def print_to_console(self):
        print('o', end='')

    def __init__(self, location, direction: str, board: Board):
        super(Head, self).__init__(location, direction, board)


class Body(SnakeSegment):
    def print_to_console(self):
        print('+', end='')

    def __init__(self, location, direction: str, board: Board):
        super(Body, self).__init__(location, direction, board)


class Snake:
    UP = 'UP'
    DOWN = 'DN'
    LEFT = 'LT'
    RIGHT = 'RT'

    all_segments: List[SnakeSegment]
    score: int

    def __init__(self, board: Board):
        head = Head(board.find_possible_location(), rdm.choice([self.RIGHT, self.LEFT, self.UP, self.DOWN]), board)
        self.all_segments = [head]
        self.score = 0

    def grow(self, board: Board):
        prospect_segment = Body((-1, -1), Snake.RIGHT, board)
        self.all_segments.append(prospect_segment)

    def eat(self, fruit: Fruit, board: Board):
        self.score = self.score + fruit.score
#        del fruit
#         self.grow(board)

    def step(self, board: Board):
        for idx in range(len(self.all_segments)-1, 0, -1):
            curr_segment = self.all_segments[idx]
            prev_segment = self.all_segments[idx - 1]
            # curr_segment.location = prev_segment.location
            curr_segment.move_to(prev_segment.location, board)
            curr_segment.direction = prev_segment.direction

        next_location = self.next_location(board)
        head = self.all_segments[0]
        head.move_to(next_location, board)

    def next_location(self, board: Board) -> Tuple[int, int]:
        head = self.all_segments[0]
        x, y = head.location
        if head.direction == Snake.RIGHT:
            x = x + 1
            if x >= board.cols:
                x = 0
        elif head.direction == Snake.LEFT:
            x = x - 1
            if x < 0:
                x = board.cols - 1
        elif head.direction == Snake.UP:
            y = y - 1
            if y < 0:
                y = board.rows - 1
        elif head.direction == Snake.DOWN:
            y = y + 1
            if y >= board.rows:
                y = 0
        return x, y

    def right_pressed(self):
        my_head = self.all_segments[0]
        # if my_head.direction == Snake.UP or my_head.direction == Snake.DOWN:
        if my_head.direction in (Snake.UP, Snake.DOWN):
            my_head.direction = Snake.RIGHT

    def left_pressed(self):
        my_head = self.all_segments[0]
        if my_head.direction in (Snake.UP, Snake.DOWN):
            my_head.direction = Snake.LEFT

    def up_pressed(self):
        my_head = self.all_segments[0]
        if my_head.direction in (Snake.LEFT, Snake.RIGHT):
            my_head.direction = Snake.UP

    def down_pressed(self):
        my_head = self.all_segments[0]
        if my_head.direction in (Snake.RIGHT, Snake.LEFT):
            my_head.direction = Snake.DOWN

    def die(self):
        for seg in self.all_segments:
            seg.die()
        print('Game Over')
        print()
        print('your score is:', self.score)
        sys.exit()

    def is_overlapping(self, location: Tuple[int, int]) -> bool:
        # if none of the segments overlap, return false

        # loop on all segments
        for segment in self.all_segments:
            # check if given location is overlapping with segment location
            if segment.is_overlapping(location):
                # if given location is overlapping with segment location, return true
                return True
            # else:
            #     continue
        # if none of the segments overlap, return false
        return False
