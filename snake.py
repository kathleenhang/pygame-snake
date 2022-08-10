import pygame

pygame.init()


# window
surface = pygame.display.set_mode((800, 800))

# red
color = (255, 0, 0)

pygame.draw.rect(surface, color, pygame.Rect(30, 30, 50, 50))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
