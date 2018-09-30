# Player groups and sprites

import pygame
import random
from groups import PlayerGroup
from actions import WizBallsActions as WBA

from conf import *

class Player(pygame.sprite.Sprite):
   # Constructor for active players

   def __init__(self, c_idx, grid_size, team):
       #
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.Surface([grid_size, grid_size])
       self.image.fill(CL_STONE[c_idx][0])

       self.rect = self.image.get_rect()

       self.action = WBA(self.rect)
       self.team = team
       self.tag = CL_STONE[c_idx][1]

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
        self.tag = 'W' # Wizard

        self.action = WBA(self.rect)

    def update(self, action):
        self.action.update(action)  

def init_all_players(court_tiles_group):
    """ TEAM 1   TEAM 2

            P    P
         W          W
            P    P

        FIELD: 20x10

    """
    # TEAM 1 corresponds to Sprites
    

    group = PlayerGroup()
    # Two teams of T_SIZE + W_SIZE
    for team in [0, 1]:
        for player in range(T_SIZE):
           c_idx = random.randint(0,5)
           p = Player(c_idx, GRID_SIZE, team)
           court_sprite = court_tiles_group.get_tile(team*10 + 3, player*3 + 4)
           p.rect.x = court_sprite.rect.x
           p.rect.y = court_sprite.rect.y
           group.add(p)
        c_idx = random.randint(0,2)
        w = Wizard(c_idx, GRID_SIZE, team)
        court_sprite = court_tiles_group.get_tile(team*10 + 3 * team + 2, 5)
        w.rect.x = court_sprite.rect.x
        w.rect.y = court_sprite.rect.y 
        group.add(w)       

    return group

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
