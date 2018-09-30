# Player groups and sprites

import pygame
import random
from actions import WizBallsActions as WBA

from conf import *

class Player(pygame.sprite.Sprite):
   # Constructor for active players

   def __init__(self, c_idx, grid_size, team):
       #
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.Surface([grid_size, grid_size])
       self.image.fill(CL_STONE[c_idx])

       self.rect = self.image.get_rect()

       self.action = WBA(self.rect)
       self.team = team

   def update(self, action):
       self.action.update(action)

class Wizard(pygame.sprite.Sprite):
    # Constructor for active wizards

    def __init__(self, c_idx, grid_size, team):
        #
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([grid_size, grid_size])
        self.image.fill(CL_WTONE[c_idx])

        self.rect = self.image.get_rect()
        self.team = team

        #self.action = WBA()

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
