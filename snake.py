import pygame
import random
import sys
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        # move right
        self.direction = Vector2(1, 0)
        self.will_grow = False
        self.head_down = pygame.image.load(
            'images/snake_head_D.png').convert_alpha()
        self.head_up = pygame.transform.rotate(self.head_down, 180)
        self.head_left = pygame.transform.rotate(self.head_down, 90)
        self.head_right = pygame.transform.rotate(self.head_down, 270)

        self.tail_down = pygame.image.load(
            'images/snake_tail_U.png').convert_alpha()
        self.tail_up = pygame.transform.rotate(self.tail_down, 180)
        self.tail_left = pygame.transform.rotate(self.tail_down, 270)
        self.tail_right = pygame.transform.rotate(self.tail_down, 90)

        self.body_vertical = pygame.image.load(
            'images/snake_body_UD.png').convert_alpha()
        self.body_horizontal = pygame.transform.rotate(self.body_vertical, 90)

        # come from bottom and turn left
        self.body_turn_DL = pygame.image.load(
            'images/snake_body_DL.png').convert_alpha()
        # come from bottom and turn right
        self.body_turn_DR = pygame.transform.rotate(self.body_turn_DL, 270)
        # come from top and turn left
        self.body_turn_UL = pygame.transform.rotate(self.body_turn_DL, 90)
        # come from top and turn right
        self.body_turn_UR = pygame.transform.rotate(self.body_turn_left, 180)

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(
                block.x * cell_size,
                block.y * cell_size,
                cell_size, cell_size)
            yellow_color = (255, 255, 0)
            pygame.draw.rect(screen, yellow_color, snake_rect)

    def move_snake(self):
        if not self.will_grow:
            # list with last item removed
            body_copy = self.body[:-1]
            self.body = body_copy
            # create new head based off of direction that the user inputted
            new_head = self.direction + self.body[0]
            self.body.insert(0, new_head)
        else:
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
        #white_color = (255, 255, 255)
        #pygame.draw.rect(screen, white_color, food_rect)
        screen.blit(food, food_rect)

    def move_food(self):
        self.x = random.randint(0, cell_count-1)
        self.y = random.randint(0, cell_count-1)
        self.pos = Vector2(self.x, self.y)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def draw_elements(self):
        self.snake.draw_snake()
        self.food.draw_food()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_move()

    def check_collision(self):
        if self.snake.body[0] == self.food.pos:
            self.snake.will_grow = True
            self.food.move_food()

    def check_move(self):
        snake_head = self.snake.body[0]
        if (snake_head.x < 0 or snake_head.x >= cell_count or
                snake_head.y < 0 or snake_head.y >= cell_count):
            self.game_over()
        # check snake body (excluding the head)
        for block in self.snake.body[1:]:
            if snake_head == block:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()

# cell width/height
cell_size = 30
# 20x20 grid
cell_count = 20
# screen
screen_width, screen_height = cell_count * cell_size, cell_count * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
black_color = pygame.color.Color('#000000')


# track time
clock = pygame.time.Clock()

food = pygame.image.load('images/food.png').convert_alpha()

main_game = Main()

# create a custom event for screen updates
screen_update = pygame.USEREVENT
# custom screen update event triggers every 150 ms
pygame.time.set_timer(screen_update, 150)
while 1:

    for event in pygame.event.get():
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:  # right
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_a:  # left
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_w:  # up
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_s:  # down
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
        # draw elements: board, snake, food
        screen.fill(black_color)
        main_game.draw_elements()

        # quit game
        if event.type == pygame.QUIT:
            main_game.game_over()
        pygame.display.update()
        # limit frame rate of game - 60 fps
        clock.tick(60)
