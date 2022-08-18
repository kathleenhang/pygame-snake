import pygame
import random
import sys
from pygame.math import Vector2


class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def draw_elements(self):
        self.check_collision()
        self.snake.draw_snake()
        self.food.draw_food()

    def update(self):
        self.snake.move_snake()

    def check_collision(self):
        if self.snake.body[0] == self.food.pos:
            self.snake.will_grow = True
            self.food.move_food()


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        # move right
        self.direction = Vector2(1, 0)
        self.will_grow = False

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(
                block.x * cell_size,
                block.y * cell_size,
                cell_size, cell_size)
            green_color = (51, 255, 0)
            pygame.draw.rect(screen, green_color, snake_rect)

    def move_snake(self):
        if not self.will_grow:
            # list with last item removed
            body_copy = self.body[:-1]
            self.body = body_copy
            # create new head based off of direction that the user inputted
            new_head = self.direction + self.body[0]
            self.body.insert(0, new_head)
        else:
            # list with last item removed
            body_copy = self.body[:]
            self.body = body_copy
            # create new head based off of direction that the user inputted
            new_head = self.direction + self.body[0]
            self.body.insert(0, new_head)
            self.will_grow = False


class Food:
    def __init__(self):
        # randomize food location
        self.move_food()

    def draw_food(self):
        # create food rectangle
        food_rect = pygame.Rect(self.pos.x * cell_size,
                                self.pos.y * cell_size, cell_size, cell_size)
        white_color = (255, 255, 255)
        pygame.draw.rect(screen, white_color, food_rect)

    def move_food(self):
        self.x = random.randint(0, cell_count-1)
        self.y = random.randint(0, cell_count-1)
        self.pos = Vector2(self.x, self.y)


pygame.init()
# screen
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
black_color = pygame.color.Color('#000000')


# track time
clock = pygame.time.Clock()

# create grid

# cell width/height
cell_size = 30
# 20x20 grid
cell_count = 20
main = Main()

# create a custom event for screen updates
screen_update = pygame.USEREVENT
# custom screen update event triggers every 150 ms
pygame.time.set_timer(screen_update, 150)
while 1:

    for event in pygame.event.get():
        if event.type == screen_update:
            main.snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # right
                main.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_a:  # left
                main.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_w:  # up
                main.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_s:  # down
                main.snake.direction = Vector2(0, 1)
        # draw elements: board, snake, food
        screen.fill(black_color)
        main.draw_elements()

        # quit game
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
        # limit frame rate of game - 60 fps
        clock.tick(60)
