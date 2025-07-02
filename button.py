import pygame

class Button():
    def __init__(self, x, y, image, action, scale):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.image.width * scale, self.image.height * scale))
        self.rect = self.image.get_rect(topleft= (x, y))
        self.action = action

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        mp = pygame.mouse.get_pos()

        if self.rect.collidepoint(mp):
            if pygame.mouse.get_just_pressed()[0] == 1:
                print("action happened!")
                self.action()
    