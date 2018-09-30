# Player groups and sprites

import pygame
import random

from conf import *

class Player(pygame.sprite.Sprite):
   # Constructor for active players

   def __init__(self, c_idx, grid_size):
       #
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.Surface([grid_size, grid_size])
       self.image.fill(CL_STONE[c_idx])

       self.rect = self.image.get_rect()

   def update(self, action):
       pass

class Wizard(pygame.sprite.Sprite):
    # Constructor for active wizards

    def __init__(self, c_idx, grid_size):
        #
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([grid_size, grid_size])
        self.image.fill(CL_WTONE[c_idx])

        self.rect = self.image.get_rect()

    def update(self, action):
        pass

class Balls(pygame.sprite.Sprite):
    # Constructor for balls

    def __init__(self, radius, grid_size):
        #
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([grid_size, grid_size])
        self.image.fill(CL_BG) 
        self.rect  = pygame.draw.circle(self.image, (0,0,0), (10, 10), radius)

    def update(self, prop):
        pass
