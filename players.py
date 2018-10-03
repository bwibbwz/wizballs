# Player groups and sprites

import pygame
import random
from sprites import SelectableSprite
from groups import PlayersGroup
from actions import WizBallsActions as WBA
from special_effects import Explode

from conf import *

def draw_rect(surface, outline_color, fill_color, border=6):
    """ Draw outline on image

    """
    # assert surface has rect <---
    # should have a more general option for 'fill_color' such as image from file
    surface.fill(outline_color)
    rect = surface.get_rect()
    surface.fill(fill_color, rect.inflate(-border, -border))

class ActivePlayers(SelectableSprite):
    """ Main class for basketball players and wizards 

    """
    def __init__(self):
        #
        SelectableSprite.__init__(self)

        self.grid_pos = [0, 0]
        self.action   = WBA()
        self.image      = None
        self.orig_image = None
        self.c_idx      = None
        self.color      = None
        self.speed = 1
        self.rect = None

    def update(self, action=None):
        if action is None:
            pass
        else:
           self.action.update(action, self.grid_pos)

        if self.action.has_moved:
            self.update_rect()
            self.action.has_moved = False

        if self.action.has_changed:
            self.kill()

    def kill(self):
        for _ in range(random.randint(6,15)):
            Explode(self)
            pygame.sprite.Sprite.kill(self)

    def update_render(self):
        if self.is_selected() and self.image is not None:
            draw_rect(self.image, CL_RED, self.color)
        else:
            self.image = self.orig_image.copy() 

    def update_rect(self):
        if self.rect is None:
            pass
        # match grid_pos to corresponding court rect
        x = self.grid_pos[0]
        y = self.grid_pos[1]
        CourtTiles = ActivePlayers.groups[0].get_sprites_from_layer(CT_L)
        self.rect.topleft = \
             CourtTiles[0].groups[1].get_tile(x, y).rect.topleft

class BasketballPlayers(ActivePlayers):
   # Constructor for active players

   def __init__(self, c_idx, grid_size, team):
       #
       ActivePlayers.__init__(self)

       self.color = CL_STONE[c_idx][0]
       self.image = pygame.Surface([grid_size, grid_size])
       self.image.fill(self.color)

       # Hold on to original image
       self.orig_image  = self.image.copy()
       self.rect = self.image.get_rect()

       self.team = team
       self.tag = CL_STONE[c_idx][1]
       self.c_idx = c_idx

       # Actions and logics
       self.action = WBA()

class Wizards(ActivePlayers):
    # Constructor for active wizards

    def __init__(self, c_idx, grid_size, team):
        #
        ActivePlayers.__init__(self)

        self.color = CL_WTONE[c_idx] 
        self.image = pygame.Surface([grid_size, grid_size])
        self.image.fill(self.color)

        # Hold on to original image
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()

        self.team = team
        self.tag = 'W' # Wizard
        self.c_idx = c_idx

        # Action and logics
        self.action = WBA()

def init_all_players(court_tiles_group):
    """ TEAM 1   TEAM 2

            P    P
         W          W
            P    P

    """
    # FIELD
    CourtTiles = ActivePlayers.groups[0].get_sprites_from_layer(CT_L)

    for team in [-1, 1]:
        # Regular players
        for player in range(T_SIZE):
           c_idx = random.randint(0,5)
           p = BasketballPlayers(c_idx, GRID_SIZE, team)
           p.grid_pos = [int(X_TILES / 2 + team), 
                         int(Y_TILES / 2) - 1 + player * 2]
           # Inital position
           p.rect.topleft = \
            CourtTiles[0].groups[1].get_tile(p.grid_pos[0], 
                                             p.grid_pos[1]).rect.topleft

        # Wizards
        c_idx = random.randint(0,2)
        w = Wizards(c_idx, GRID_SIZE, team)
        w.grid_pos = [int(X_TILES / 2 + team * 3), 
                      int(Y_TILES / 2)]
        w.rect.topleft = \
         CourtTiles[0].groups[1].get_tile(w.grid_pos[0], 
                                          w.grid_pos[1]).rect.topleft


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
