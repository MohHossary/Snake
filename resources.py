import pygame
from pathlib import Path
from enum import Enum


ICON_TYPES: Enum = Enum('ICON_TYPES', ['HEAD', 'BODY', 'TAIL'], start=0)

pygame.mixer.init()


# def load_res():
res_folder = Path(__file__).parent / 'res'

grow_sound = pygame.mixer.Sound(res_folder / 'grow_sound.mp3')
grow_sound.set_volume(1)
death_sound = pygame.mixer.Sound(res_folder / 'death_sound.mp3')
death_sound.set_volume(1)
bg_sound = pygame.mixer.Sound(res_folder / 'bg_sound.mp3')
bg_sound.set_volume(0.2)

icon = pygame.image.load(res_folder / 'snake.ico')

snake_head_up_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Snake_head_up.png'), 0, 12 / 11)
snake_head_down_img = pygame.transform.rotozoom(snake_head_up_img, 180, 1.)
snake_head_left_img = pygame.transform.rotozoom(snake_head_up_img, 90, 1.)
snake_head_right_img = pygame.transform.rotozoom(snake_head_up_img, -90, 1.)
snake_head_up_turn_right_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Snake_head_turn.png'), 0, 60. / 85.)
snake_head_right_turn_right_img = pygame.transform.rotozoom(snake_head_up_turn_right_img, 90, 60. / 85.)
snake_head_down_turn_right_img = pygame.transform.rotozoom(snake_head_up_turn_right_img, 180, 60. / 85.)
snake_head_left_turn_right_img = pygame.transform.rotozoom(snake_head_up_turn_right_img, -90, 60. / 85.)
snake_head_up_turn_left_img = pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load(res_folder / 'Snake_head_turn.png'), True, False), 0, 60. / 85.)
snake_head_right_turn_left_img = pygame.transform.rotozoom(snake_head_up_turn_left_img, 90, 60./ 85.)
snake_head_down_turn_left_img = pygame.transform.rotozoom(snake_head_up_turn_left_img, 180, 60./ 85.)
snake_head_left_turn_left_img = pygame.transform.rotozoom(snake_head_up_turn_left_img, -90, 60./ 85.)

snake_body_vertical_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Snake_body_vertical.jpg'), 0, (60. / 85.))
snake_body_horizontal_img = pygame.transform.rotozoom(snake_body_vertical_img, 90, 1.)
snake_body_turn_connected_at_down_and_left_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Snake_body_turn.jpg'), 0, 60. / 85.)
snake_body_turn_connected_at_down_and_right_img = pygame.transform.rotozoom(snake_body_turn_connected_at_down_and_left_img, 90, 1)
snake_body_turn_connected_at_up_and_left_img = pygame.transform.rotozoom(snake_body_turn_connected_at_down_and_left_img, -90, 1)
snake_body_turn_connected_at_up_and_right_img = pygame.transform.rotozoom(snake_body_turn_connected_at_down_and_left_img, 180, 1)
snake_body_up_img = snake_body_down_img = snake_body_vertical_img
snake_body_left_img = snake_body_right_img = snake_body_horizontal_img
snake_body_right_after_turn_left_img = snake_body_up_after_turn_right_img = snake_body_turn_connected_at_up_and_right_img
snake_body_down_after_turn_right_img = snake_body_left_after_turn_left_img = snake_body_turn_connected_at_down_and_left_img
snake_body_right_after_turn_right_img = snake_body_down_after_turn_left_img = snake_body_turn_connected_at_down_and_right_img
snake_body_left_after_turn_right_img = snake_body_up_after_turn_left_img = snake_body_turn_connected_at_up_and_left_img


fruit_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Fruit.jpg'), 0, (60. / 85.))
wall_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Wall.jpg'), 0, (60. / 85.))
icons = [
    [  # snake head
        [  # snake head up
            snake_head_up_img,
            snake_head_up_turn_right_img,
            snake_head_up_turn_left_img,
        ],
        [  # snake head right
            snake_head_right_img,
            snake_head_right_turn_right_img,
            snake_head_right_turn_left_img,
        ],
        [  # snake head Down
            snake_head_down_img,
            snake_head_down_turn_right_img,
            snake_head_down_turn_left_img,
        ],
        [  # snake head LEFT
            snake_head_left_img,
            snake_head_left_turn_right_img,
            snake_head_left_turn_left_img,
        ]
    ],  # End of snake head
    [  # snake body
        [  # snake body up
            snake_body_up_img,
            snake_body_up_after_turn_right_img,
            snake_body_up_after_turn_left_img,
        ],
        [  # snake body right
            snake_body_right_img,
            snake_body_right_after_turn_right_img,
            snake_body_right_after_turn_left_img,
        ],
        [  # snake body Down
            snake_body_down_img,
            snake_body_down_after_turn_right_img,
            snake_body_down_after_turn_left_img,
        ],
        [  # snake body LEFT
            snake_body_left_img,
            snake_body_left_after_turn_right_img,
            snake_body_left_after_turn_left_img,
        ]
    ],  # End of snake body
    [  # snake tail

    ]  # end of snake tail
]
