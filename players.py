# Player groups and sprites

import pygame
import random

# Skin Tones
stone = {}
stone[0] = (234, 192, 134) # cauc-brown
stone[1] = (255, 224, 189) # cauc-pink
stone[2] = (255, 173, 96)  # cauc-orange


class Player(pygame.sprite.Sprite):
   # Constructor for active players

   def __init__(self, c_idx, width, height):
       #
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.Surface([width, height])
       self.image.fill(stone[c_idx])

       self.rect = self.image.get_rect()

   def update(self, action):
       pass

class Balls(pygame.sprite.Sprite):
    # Constructor for balls

    def __init__(self, radius):
        #
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height]) 
        self.image.fill()
