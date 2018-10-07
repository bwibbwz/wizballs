# Player groups and sprites

import pygame
import random
from sprites import SelectableSprite
from groups import PlayersGroup, CourtTilesGroup
from actions import WizBallsActions as WBA
from animator import AnimateMove as ANIM
from special_effects import Explode
from graphics_functions import draw_border, load_image
from court import GridPosition

from conf import *

def get_group(sprite, group_in):
    for group in sprite.groups:
        if group.__class__ == pygame.sprite.LayeredUpdates:
            all_sprites = group
            break
    for s in all_sprites.sprites():
        for g in s.groups:
            if g.__class__ == group_in:
                group_out = g
                break
    return group_out

def Stats():
    def __init__(self):
        self._stats = {'health': 100,
                       'str': 8,
                       'dex': 8,
                       'int': 8,
                      }

class ActivePlayers(SelectableSprite):
    """ Main class for basketball players and wizards 

    """
    def __init__(self, color, x=0, y=0):
        #
        SelectableSprite.__init__(self, main_color = CL_ALPHA, selected_color = CL_BLACK)

        self.pos = GridPosition(x, y)

        self.action   = WBA()

        self.image      = None
        self.orig_image = None
        self.c_idx      = None
        self.color      = None
        self.speed = 1
        self.rect = None

        # Need ctrl for animations
        self.image_index = 0
        self.anim_counter = 0
        self.animate = False

        self.color = color
        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE], pygame.SRCALPHA)
        self.image.fill(self.color)

        #self.update()

    def select(self):
        super().select()
        return

    def update(self, action=None):
        if action is None:
            pass
        else:
           self.action.update(action, self.pos)

        if self.action.has_moved:
            beg = self.rect.center
            end = self.update_rect()
            self.action.has_moved = False
            self.movement.initialize(beg, end)
            self.movement.animate = True

        if self.movement.animate:
            self.image = self.movement.update(self.rect)

        if self.action.has_changed:
            self.kill()

        # This takes care of drawing the border in the correct color
        draw_border(self.image, color = self._active_color)

    def kill(self):
        for _ in range(random.randint(15,30)):
            Explode(self)
        pygame.sprite.Sprite.kill(self)

    def update_rect(self):
        if self.rect is None:
            pass
        # match grid_pos to corresponding court rect
        x = self.pos.x
        y = self.pos.y
        g = get_group(self, CourtTilesGroup)
        return g.get_tile(self.pos).rect.center


class BasketballPlayers(ActivePlayers):
   # Constructor for active players

   def __init__(self, c_idx, team):
       #
       ActivePlayers.__init__(self, CL_STONE[c_idx][0])

       # Hold on to original image
       self.orig_image  = self.image.copy()
       self.rect = self.image.get_rect()

       self.team = team
       self.tag = CL_STONE[c_idx][1]
       self.c_idx = c_idx

       self.movement = ANIM([self.image, self.image], 10)

       # Actions and logics
       self.action = WBA()

class Wizards(ActivePlayers):
    # Constructor for active wizards

    def __init__(self, c_idx, team):
        #
        ActivePlayers.__init__(self, CL_WTONE[c_idx])

        # Hold on to original image
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()

        angle = (team + 1) * 90

        #
        self.images = []
        self.images.append(load_image('img/anim/wizard/wizard_1_still.png', self.rect, angle))
        self.images.append(load_image('img/anim/wizard/wizard_1_walk_1.png', self.rect, angle))
        self.images.append(load_image('img/anim/wizard/wizard_1_still.png', self.rect, angle))
        self.images.append(load_image('img/anim/wizard/wizard_1_walk_2.png', self.rect, angle))

        # Animate Movement
        self.movement = ANIM(self.images, 10)

        self.image_index = 0
        self.image = self.images[self.image_index]

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

    for team in [-1, 1]:
        # Regular players
        for player in range(T_SIZE):
           c_idx = random.randint(0,5)
           p = BasketballPlayers(c_idx, team)
           p.pos.pos = (int(X_TILES / 2 + team), int(Y_TILES / 2) - 1 + player * 2)
           # Inital position
           p.rect.center = \
            court_tiles_group.get_tile(p.pos).rect.center

        # Wizards
        c_idx = random.randint(0,2)
        w = Wizards(c_idx, team)
        w.pos.pos = (int(X_TILES / 2 + team * 3), int(Y_TILES / 2))
        w.rect.center = \
         court_tiles_group.get_tile(w.pos).rect.center


class Balls(pygame.sprite.Sprite):
    # Constructor for balls

    def __init__(self, radius):
        #
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE])
        self.image.fill(CL_BG) 
        self.rect  = pygame.draw.circle(self.image, (0,0,0), (10, 10), radius)

    def update(self, prop):
        pass
