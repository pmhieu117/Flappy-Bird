import pygame,sys
pygame.init()
screen = pygame.display.set_mode((432,768))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()