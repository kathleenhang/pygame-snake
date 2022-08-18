import pygame
import random
import sys
from pygame.math import Vector2


class Food:
    def __init__(self):
        # randomize food location
        self.x = random.randint(0, cell_count-1)
        self.y = random.randint(0, cell_count-1)
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        # create food rectangle
        food_rect = pygame.Rect(self.pos.x * cell_size,
                                self.pos.y * cell_size, cell_size, cell_size)
        white_color = (255, 255, 255)
        pygame.draw.rect(screen, white_color, food_rect)


pygame.init()
# screen
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
black_color = pygame.color.Color('#000000')


x = screen_width/3
y = screen_height/3

# surface
blue_surface = pygame.Surface((30, 30))
blue_surface.fill((0, 0, 255))
# position blue rect center at screen midpoint
blue_rect = blue_surface.get_rect(center=(screen_width/2, screen_height/2))


# track time
clock = pygame.time.Clock()


# create grid

# cell width/height
cell_size = 30
# 20x20 grid
cell_count = 20


food = Food()
while 1:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # right
                blue_rect.right += 10
            if event.key == pygame.K_a:  # left
                blue_rect.left -= 10
            if event.key == pygame.K_w:  # up
                blue_rect.top -= 10
            if event.key == pygame.K_s:  # down
                blue_rect.bottom += 10
        # fill bg color before snake/food
        screen.fill(black_color)
        food.draw_food()
        # draw the elements
        screen.blit(blue_surface, blue_rect)
        # quit game
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
        # limit frame rate of game - 60 fps
        clock.tick(60)
