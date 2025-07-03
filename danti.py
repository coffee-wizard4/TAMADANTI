import pygame
import dialogue

class Danti(pygame.sprite.Sprite):
    def __init__(self, *groups, hunger, attention):
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
        self.emotion_flag = False

        self.quote = ""

        self.attention = attention
        self.hunger = hunger

        self.image = self.current_emotion[self.anim_index]
        self.rect = self.image.get_rect(midbottom = (150, 600))

        print("hunger set to", hunger)
        print("attention set to", attention)
    
    def anim_state(self):
        self.anim_index += 0.1
        if self.anim_index >= len(self.danti_happy):
           self.anim_index = 0
        self.image = self.current_emotion[int(self.anim_index)]

    def switch_emotion(self):
        if (self.hunger < 30 and self.attention < 30) or (self.hunger < 30):
            self.current_emotion = self.danti_sad
            self.quote = dialogue.get_random_quote(dialogue.Emotion.SAD)
        elif self.attention < 30:
            self.current_emotion = self.danti_angry
            self.quote = dialogue.get_random_quote(dialogue.Emotion.ANGRY)
        else: 
            self.current_emotion = self.danti_happy
            self.quote = dialogue.get_random_quote(dialogue.Emotion.HAPPY)
    
    def decrease_food(self):
        self.hunger = 0 if self.hunger <= 0 else self.hunger - 0.1
        self.attention = 0 if self.attention <= 0 else self.attention - 0.1

    def feed(self):
        self.emotion_flag = False
        self.hunger = 100
        self.switch_emotion()

    def pet(self):
        self.emotion_flag = False
        self.attention = 100
        self.switch_emotion()

    def update(self):
        self.anim_state()
        self.decrease_food()
        if (self.hunger < 30 or self.attention < 30) and self.emotion_flag == False:
            self.emotion_flag = True
            self.switch_emotion()