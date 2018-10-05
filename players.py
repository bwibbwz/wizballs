# Player groups and sprites

import pygame
import random
from sprites import SelectableSprite
from groups import PlayersGroup
from actions import WizBallsActions as WBA
from special_effects import Explode
from graphics_functions import draw_border
from court import GridPosition
from basic_functions import load_image

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

        self.update()


    def select(self):
        super().select()
        return
        # The following code has NO effect at the moment but will be used in the future.
        from groups import CourtTilesGroup
        court_tiles_group = None
        for group in self.groups:
            if group.__class__ == pygame.sprite.LayeredUpdates:
                all_sprites = group
                break
        for s in all_sprites.sprites():
            for g in s.groups:
                if g.__class__ == CourtTilesGroup:
                    court_tiles_group = g
                    break
        court_tiles_group.get_tile(self.pos + (1, 0)).highlight()
        court_tiles_group.get_tile(self.pos - (1, 0)).highlight()

    def update(self, action=None):
        if action is None:
            pass
        else:
           self.action.update(action, self.pos)

        if self.action.has_moved:
            self.old_tl = self.rect.topleft  # Beg
            self.new_tl = self.update_rect() # End
            self.action.has_moved = False
            self.animate = True

        if self.animate:
            self.animate_move(self.old_tl, self.new_tl)

        if self.action.has_changed:
            self.kill()

        # This takes care of drawing the border in the correct color
        draw_border(self.image, color = self._active_color)

    def kill(self):
        for _ in range(random.randint(6,15)):
            Explode(self)
            pygame.sprite.Sprite.kill(self)

    def update_rect(self):
        if self.rect is None:
            pass
        # match grid_pos to corresponding court rect
        x = self.pos.x
        y = self.pos.y
        CourtTiles = ActivePlayers.groups[0].get_sprites_from_layer(CT_L)
        #self.rect.topleft = \
        #      CourtTiles[0].groups[1].get_tile(self.pos).rect.topleft
        return CourtTiles[0].groups[1].get_tile(self.pos).rect.topleft

    def animate_move(self, old_tl, new_tl):
        # Update image in intervals of ??
        # X
        X = new_tl[0] - old_tl[0]
        Y = new_tl[1] - old_tl[1]
        dX = X // 10 # Three loops of 1,2,3
        dY = Y // 10 
        # end is image 0
        self.image_index += 1

        if self.image_index > 3:
            self.image_index = 0

        self.image = self.images[self.image_index]
        self.rect.x += dX
        self.rect.y += dY

        self.anim_counter += 1

        if self.anim_counter == 9: # Overwrite
            self.image = self.images[0]
            self.rect.topleft = new_tl
            self.anim_counter = 0
            self.image_index = 0
            self.animate = False
            

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

        # HACK to overwrite current image
        self.images = []
        self.images.append(load_image('img/anim/wizard/wizard_1_still.bmp', self.rect))
        self.images.append(load_image('img/anim/wizard/wizard_1_walk_1.bmp', self.rect))
        self.images.append(load_image('img/anim/wizard/wizard_1_still.bmp', self.rect))
        self.images.append(load_image('img/anim/wizard/wizard_1_walk_3.bmp', self.rect))

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
    CourtTiles = ActivePlayers.groups[0].get_sprites_from_layer(CT_L)

    for team in [-1, 1]:
        # Regular players
        for player in range(T_SIZE):
           c_idx = random.randint(0,5)
           p = BasketballPlayers(c_idx, team)
           p.pos.pos = (int(X_TILES / 2 + team), int(Y_TILES / 2) - 1 + player * 2)
           # Inital position
           p.rect.topleft = \
            CourtTiles[0].groups[1].get_tile(p.pos).rect.topleft

        # Wizards
        c_idx = random.randint(0,2)
        w = Wizards(c_idx, team)
        w.pos.pos = (int(X_TILES / 2 + team * 3), int(Y_TILES / 2))
        w.rect.topleft = \
         CourtTiles[0].groups[1].get_tile(w.pos).rect.topleft


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
