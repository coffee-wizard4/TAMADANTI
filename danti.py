import pygame

class Emotion:
    HAPPY = 0
    SAD = 1
    ANGRY = 2

class Danti(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        #danti animations#
        danti_happy_1 = pygame.transform.scale(pygame.image.load("assets/danti/happy_0001.png"),(256,256))
        danti_happy_2 = pygame.transform.scale(pygame.image.load("assets/danti/happy_0002.png"),(256,256))
        danti_sad_1 = pygame.transform.scale(pygame.image.load("assets/danti/sad_0001.png"),(256,256))
        danti_sad_2 = pygame.transform.scale(pygame.image.load("assets/danti/sad_0002.png"),(256,256))
        danti_angry_1 = pygame.transform.scale(pygame.image.load("assets/danti/angry_0001.png"),(256,256))
        danti_angry_2 = pygame.transform.scale(pygame.image.load("assets/danti/angry_0002.png"),(256,256))

        self.danti_happy = [danti_happy_1, danti_happy_2]
        self. danti_sad = [danti_sad_1, danti_sad_2]
        self.danti_angry = [danti_angry_1, danti_angry_2]
        self.current_emotion = self.danti_happy
        self.anim_index = 0

        self.emotion = Emotion.HAPPY
        self.attention = 100
        self.hunger = 100

        self.image = self.current_emotion[self.anim_index]
        self.rect = self.image.get_rect(midbottom = (150, 600))

    
    def anim_state(self):
        self.anim_index += 0.1
        if self.anim_index >= len(self.danti_happy):
           self.anim_index = 0
        self.image = self.current_emotion[int(self.anim_index)]

    def switch_emotion(self):
        if (self.hunger < 30 and self.attention < 30) or (self.hunger < 30):
            self.current_emotion = self.danti_sad
        elif self.attention < 30:
            self.current_emotion = self.danti_angry
        else: 
            self.current_emotion = self.danti_happy

    def decrease_food(self):
        self.hunger -= 0.01
        self.attention -= 0.02

    def feed(self):
        self.hunger = 100
        self.switch_emotion()

    def pet(self):
        self.attention = 100
        self.switch_emotion()

    def update(self):
        self.anim_state()
        self.decrease_food()
        if self.hunger < 30 or self.attention < 30:
            self.switch_emotion()