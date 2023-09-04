import pygame
from pathlib import Path

pygame.mixer.init()


# def load_res():
res_folder = Path(__file__).parent / 'res'

grow_sound = pygame.mixer.Sound(res_folder / 'grow_sound.mp3')
grow_sound.set_volume(1)
death_sound = pygame.mixer.Sound(res_folder / 'death_sound.mp3')
death_sound.set_volume(1)
bg_sound = pygame.mixer.Sound(res_folder / 'bg_sound.mp3')
bg_sound.set_volume(0.2)

snake_head_up_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Snake_head_up.png'), 0, 12 / 11)
snake_head_down_img = pygame.transform.rotozoom(snake_head_up_img, 180, 1.)
snake_head_left_img = pygame.transform.rotozoom(snake_head_up_img, 90, 1.)
snake_head_right_img = pygame.transform.rotozoom(snake_head_up_img, -90, 1.)
snake_body_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Snake_body.jpg'), 0, (60. / 85.))
fruit_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Fruit.jpg'), 0, (60. / 85.))
wall_img = pygame.transform.rotozoom(pygame.image.load(res_folder / 'Wall.jpg'), 0, (60. / 85.))
