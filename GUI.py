import random as rdm
import time
from pathlib import Path
import pygame
from pygame import Vector2
from fruit import Fruit
from snake import Snake, Head, Body
from board import Board
from clock import ClockListener, Clock
from wallbuilder import WallSegment, NoWallsBuilder, VerticalWallsBuilder, HorizontalWallsBuilder, AllWallsBuilder


class PygameBoard(ClockListener):
    cell_width: int
    cell_height: int
    frame_width: int
    frame_height: int
    x_translation: int
    y_translation: int
    score: int
    snake_head_up_img = None
    snake_head_down_img = None
    snake_head_right_img = None
    snake_head_left_img = None
    snake_body_img = None
    fruit_img = None
    wall_img = None

    def __init__(self, board: Board, snake: Snake):
        pygame.init()
        self.board = board
        self.snake = snake
        self.load_images()
        self.update_parameters()
        self.screen = pygame.display.set_mode((self.board.cols * self.cell_width + self.frame_width, self.board.rows * self.cell_height + self.frame_height))
        pygame.display.set_caption("Snake")

    def update_parameters(self):
        self.cell_width = 60
        self.cell_height = 60
        self.frame_width = 10
        self.frame_height = 10
        self.x_translation, self.y_translation = self.frame_width // 2, self.frame_height // 2

    def project(self, x, y) -> tuple[int, int]:
        inflate_x, inflate_y = x * self.cell_width, y * self.cell_height
        return self.x_translation + inflate_x, self.y_translation + inflate_y

    def clock_ticked(self):
        self.repaint()

    def repaint(self):
        # font = pygame.font.Font(None, 100)
        # score_surf = font.render(str(self.snake.score), False, (255, 255, 255))
        # text_surf1 = font.render('Score', False, (255, 255, 255))
        # text_surf2 = font.render('Snake', False, (255, 255, 255))
        # self.screen.blit(score_surf, (615, 300))
        # self.screen.blit(text_surf1, (615, 225))
        # self.screen.blit(text_surf2, (615, 25))
        self.screen.fill((50, 50, 50), (0, 0, self.board.cols * self.cell_width, self.board.rows * self.cell_height))
        for c in range(0, self.board.cols + 1):
            px1, py1 = self.project(c, 0)
            px2, py2 = self.project(c, self.board.rows)
            pygame.draw.line(self.screen, (255, 255, 255), (px1, py1 - self.y_translation + 1),
                             Vector2(px2, py2 + self.y_translation), width=self.frame_width)

        for r in range(0, self.board.rows + 1):
            px1, py1 = self.project(0, r)
            px2, py2 = self.project(self.board.cols, r)
            pygame.draw.line(self.screen, (255, 255, 255), (px1, py1), Vector2(px2 - self.x_translation, py2),
                             width=self.frame_width)

        for y in range(self.board.rows):
            for x in range(self.board.cols):
                cell = self.board.get_cell(x, y)
                if isinstance(cell, Head):
                    head_direction = self.snake.all_segments[0].direction
                    if head_direction == self.snake.RIGHT:
                        self.screen.blit(self.snake_head_right_img, self.project(x, y))
                    elif head_direction == self.snake.LEFT:
                        self.screen.blit(self.snake_head_left_img, self.project(x, y))
                    elif head_direction == self.snake.UP:
                        self.screen.blit(self.snake_head_up_img, self.project(x, y))
                    elif head_direction == self.snake.DOWN:
                        self.screen.blit(self.snake_head_down_img, self.project(x, y))

                elif isinstance(cell, Body):
                    self.screen.blit(self.snake_body_img, self.project(x, y))

                elif isinstance(cell, Fruit):
                    self.screen.blit(self.fruit_img, self.project(x, y))

                elif isinstance(cell, WallSegment):
                    self.screen.blit(self.wall_img, self.project(x, y))
        pygame.display.update()

    def load_images(self):
        res_folder = Path(__file__).parent / 'res'
        self.snake_head_up_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Snake head_up.png'), 0, 12 / 11)
        self.snake_head_down_img = pygame.transform.rotozoom(self.snake_head_up_img, 180, 1.)
        self.snake_head_left_img = pygame.transform.rotozoom(self.snake_head_up_img, 90, 1.)
        self.snake_head_right_img = pygame.transform.rotozoom(self.snake_head_up_img, -90, 1.)
        self.snake_body_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Snake body.jpg'), 0, (60. / 85.))
        self.fruit_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Fruit.jpg'), 0, (60. / 85.))
        self.wall_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Wall.jpg'), 0, (60. / 85.))


if __name__ == '__main__':
    walls = rdm.choice([NoWallsBuilder(), VerticalWallsBuilder(), HorizontalWallsBuilder(), AllWallsBuilder()])

    dummy_board = Board(10, 10)
    walls.build_walls(dummy_board)
    snake = Snake(dummy_board)
    fruit = Fruit(dummy_board)
    pygameboard = PygameBoard(dummy_board, snake)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time.sleep(1)
        pygameboard.clock_ticked()

    pygame.quit()
