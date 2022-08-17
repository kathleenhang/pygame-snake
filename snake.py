import pygame
import random
import sys
from pygame.math import Vector2
pygame.init()
screen_width, screen_height = 800, 800

# init window/screen for display
screen = pygame.display.set_mode((screen_width, screen_height))

red_color = (255, 0, 0)
black_color = pygame.color.Color('#000000')
x = screen_width/3
y = screen_height/3

picture = pygame.image.load('jake.gif').convert()
image_size = (30, 30)
picture = pygame.transform.scale(picture, image_size)


while 1:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:  # right
                x += 10
            if event.key == pygame.K_a:  # left
                x -= 10
            if event.key == pygame.K_w:  # up
                y -= 10
            if event.key == pygame.K_s:  # down
                y += 10

        x += 1
        screen.fill(black_color)
        # draw the elements - jake
        screen.blit(picture, (x, y))
        # quit game
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.flip()
