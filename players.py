# Player groups and sprites

import pygame
import random
from groups import PlayersGroup
from actions import WizBallsActions as WBA

from conf import *

def draw_rect(surface, outline_color, fill_color, border=6):
    """ Draw outline on image

    """
    # assert surface has rect <---
    # should have a more general option for 'fill_color'
    surface.fill(outline_color)
    rect = surface.get_rect()
    surface.fill(fill_color, rect.inflate(-border, -border))

class ActivePlayers(pygame.sprite.Sprite):
    """ Main class for basketball players and wizards 

    """
    def __init__(self):
        #
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.grid_pos = [0, 0]
        self.selected = False
        self.action   = WBA()
        self.image      = None
        self.orig_image = None
        self.c_idx      = None
        self.color      = None
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
            self.update_render()
            self.action.has_changed = False

    def update_render(self):
        if self.selected and self.image is not None:
            draw_rect(self.image, CL_RED, self.color)
        else:
            self.image = self.orig_image.copy() 

    def update_rect(self):
        if self.rect is None:
            pass
        # IF grid_pos has changed - match grid_pos
        # to corresponding court rect
        x = self.grid_pos[0]
        y = self.grid_pos[1]
        CourtTiles = ActivePlayers.groups[0].get_sprites_from_layer(2)
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
        self.grid_pos = [0, 0] 
        self.c_idx = c_idx

        # Action and logics
        self.action = WBA()

def init_all_players(court_tiles_group):
    """ TEAM 1   TEAM 2

            P    P
         W          W
            P    P

        FIELD: 20x10

    """
    # Two teams of T_SIZE + W_SIZE
    for team in [0, 1]:
        # Regular players
        for player in range(T_SIZE):
           c_idx = random.randint(0,5)
           p = BasketballPlayers(c_idx, GRID_SIZE, team)
           p.grid_pos = [team * 10 + 3, player * 3 + 4]
           # Inital position
           p.rect.topleft = \
             court_tiles_group.get_tile(p.grid_pos[0], 
                                        p.grid_pos[1]).rect.topleft

        # Wizards
        c_idx = random.randint(0,2)
        w = Wizards(c_idx, GRID_SIZE, team)
        w.grid_pos = [team * 10 + 3 * team + 2, 5]
        w.rect.topleft = \
          court_tiles_group.get_tile(w.grid_pos[0], 
                                     w.grid_pos[1]).rect.topleft


class Fragments(pygame.sprite.Sprite):
    """ Fragments of 'some' exploding sprite

    """
    gravity = True
    def __init__(self,sprite):
        pygame.sprite.Sprite.__init__(self, self.groups)
        # Pos is a reference to the court grid (int, int)
        self.pos = [0, 0]
        self.pos[0] = sprite.pos[0]
        self.pos[1] = sprite.pos[1]

        # inherit color from exploding object
        self.color = sprite.color

        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        # Set transparency? self.image.set_colorkey(CL_BG)
        pygame.draw.circle(self.image, (random.randint(1,64),0,0),
                                       (5,5),
                                       random.randint(2,5))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.lifetime = 1 + random.randint(0,5) # max 6
        self.maxspeed = sprite.speed * 2 

        # Get 


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
