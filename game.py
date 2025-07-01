import pygame
from sys import exit
import danti

pygame.init()

width = 300
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TAMADANTI")
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background.png')

dante = pygame.sprite.GroupSingle()
dante.add(danti.Danti())

guy = pygame.image.load('assets/danti/happy_0001.png')


#game_loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             
    screen.blit(bg_surface, (0, 0))
    dante.draw(screen)
    dante.update()
    pygame.display.update()
    clock.tick(20)