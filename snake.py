import pygame
import random
import sys
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        # move right
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(
                block.x * cell_size,
                block.y * cell_size,
                cell_size, cell_size)
            green_color = (51, 255, 0)
            pygame.draw.rect(screen, green_color, snake_rect)

    def move_snake(self):
        # list with last item removed
        body_copy = self.body[:-1]
        self.body = body_copy
        # create new head based off of direction that the user inputted
        new_head = self.direction + self.body[0]
        self.body.insert(0, new_head)


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
snake = Snake()
# create a custom event for screen updates
screen_update = pygame.USEREVENT
# custom screen update event triggers every 150 ms
pygame.time.set_timer(screen_update, 150)
while 1:

    for event in pygame.event.get():
        if event.type == screen_update:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # right
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_a:  # left
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_w:  # up
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_s:  # down
                snake.direction = Vector2(0, 1)
        # fill bg color before snake/food
        screen.fill(black_color)
        food.draw_food()
        snake.draw_snake()

        # draw the elements
        screen.blit(blue_surface, blue_rect)
        # quit game
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
        # limit frame rate of game - 60 fps
        clock.tick(60)
