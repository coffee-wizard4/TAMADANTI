import pygame
from sys import exit
import danti
import save_load_manager

pygame.init()

width = 300
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TAMADANTI")
clock = pygame.time.Clock()

data = save_load_manager.load()

bg_surface = pygame.transform.scale(pygame.image.load('assets/background.png'), (300, 600))
dante = pygame.sprite.GroupSingle()
d_obj = danti.Danti(hunger=data["hunger"], attention=data["attention"])
dante.add(d_obj)



#game_loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_load_manager.save(d_obj.hunger, d_obj.attention)
            pygame.quit()
            exit()
             
    screen.blit(bg_surface, (0, 0))
    dante.draw(screen)
    dante.update()
    pygame.display.update()
    clock.tick(20)