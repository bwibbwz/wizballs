#!/usr/bin/env python3

import pygame
import logging as l
from conf import *
from groups import Group, CourtTilesGroup
from sprites import SelectableSprite, HighlightableSprite
from graphics_functions import draw_border, copy_color
from controls import Direction

class GridPosition():
    def __init__(self, x, y, max_x=X_TILES, max_y=Y_TILES):
        self._max_x = max_x
        self._max_y = max_y
        self.pos = x, y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self.pos = x, self.y

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self.pos = self.x, y

    @property
    def pos(self):
        return self._x, self._y
    
    @pos.setter
    def pos(self, pos):
        if pos[0] >= self._max_x or pos[1] >= self._max_y or pos[0] < 0 or pos[1] < 0:
            raise IndexError('(%i, %i) is outside the grid area' % (pos[0], pos[1]))
        self._x = pos[0]
        self._y = pos[1]

    def move(self, direction):
        if len(direction) == 2:
            self.pos = self.x + direction[0], self.y + direction[1]
        else:
            raise ValueError('Move only accepts a (x, y) or Direction() input.')

        return self.pos

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError('There are only 2 values possible, 0 and 1 (%i was given)' % key)

    def __call__(self):
        return self.pos

    def __str__(self):
        return str(self.pos)

    def __add__(self, dpos):
        self.move(dpos[0], dpos[1])

    def __sub__(self, dpos):
        self.__add__((-dpos[0], -dpos[1]))

    def __eq__(self, pos):
        return self.x == pos[0] and self.y == pos[1]


class CourtLine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)
        # NYI
        
class CourtField(pygame.sprite.Sprite):
    def __init__(self, color, size, name):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

        if name == 'play_court':
            court_picture = pygame.image.load('img/wood-floor-tileable.jpg').convert()
            court_picture = pygame.transform.scale(court_picture, (self.rect.size))
            court_picture.set_alpha(BG_COURT_OPACITY)
            self.image.blit(court_picture, court_picture.get_rect())

            pygame.draw.circle(self.image, CL_BLACK, self.rect.center, GRID_SIZE, 3)
            pygame.draw.circle(self.image, CL_BLACK, self.rect.center, GRID_SIZE // 3, 3)

            oob_lines = pygame.draw.rect(self.image, CL_BLACK, (self.rect.topleft[0] + 2 * GRID_SIZE * GRID_PADDING, 
                                                                self.rect.topleft[1] + 2 * GRID_SIZE * GRID_PADDING,
                                                                X_TILES * GRID_SIZE * (1 + GRID_PADDING) - 3 * GRID_SIZE * GRID_PADDING,
                                                                Y_TILES * GRID_SIZE * (1 + GRID_PADDING) - 3 * GRID_SIZE * GRID_PADDING),
                                                                3)

            center_line = pygame.draw.line(self.image, CL_BLACK, oob_lines.midtop, (oob_lines.midbottom[0], oob_lines.midbottom[1] - 1), 3)

            penalty_box1 = pygame.draw.rect(self.image,
                             CL_BLACK, 
                             (oob_lines.right - (4 * (GRID_SIZE * (1 + GRID_PADDING)) - 3 * GRID_PADDING * GRID_SIZE),
                              oob_lines.centery - 1.5 * (GRID_SIZE * (1 + GRID_PADDING)) + 1.5 * GRID_PADDING * GRID_SIZE,
                              4 * (GRID_SIZE * (1 + GRID_PADDING)) - 3 * GRID_PADDING * GRID_SIZE,
                              3 * (GRID_SIZE * (1 + GRID_PADDING)) - 3 * GRID_PADDING * GRID_SIZE),
                             3)
            pygame.draw.circle(self.image, CL_BLACK, penalty_box1.midleft, GRID_SIZE, 3)

            penalty_box2 = pygame.draw.rect(self.image,
                             CL_BLACK, 
                             (oob_lines.left,
                              oob_lines.centery - 1.5 * (GRID_SIZE * (1 + GRID_PADDING)) + 1.5 * GRID_PADDING * GRID_SIZE,
                              4 * (GRID_SIZE * (1 + GRID_PADDING)) - 3 * GRID_PADDING * GRID_SIZE,
                              3 * (GRID_SIZE * (1 + GRID_PADDING)) - 3 * GRID_PADDING * GRID_SIZE),
                             3)
            pygame.draw.circle(self.image, CL_BLACK, penalty_box2.midright, GRID_SIZE, 3)

        self.name = name

class CourtTile(SelectableSprite, HighlightableSprite):
    def __init__(self, x, y):
        HighlightableSprite.__init__(self, main_color = CL_TILES, highlighted_color = CL_BLUE)
        SelectableSprite.__init__(self, main_color = CL_TILES, selected_color = CL_RED)

        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE], pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.pos = GridPosition(x, y, X_TILES, Y_TILES)

        self._fill_opacity = COURT_TILE_OPACITY

        self.update()

    def update(self):
        self.image.fill(copy_color(self._active_color, alpha = self._fill_opacity))
        draw_border(self.image, color = self._active_color)

class BasketTile(CourtTile):
    def __init__(self, x, y):
        CourtTile.__init__(self, x, y)

    def update(self):
        self.image.fill(copy_color(self._active_color, alpha = BASKET_TILE_OPACITY))
        draw_border(self.image, color = self._active_color)
        # BUG: The basket itself should be drawn on top of the player sprite. 
        pygame.draw.circle(self.image, CL_BLACK, (int(GRID_SIZE / 2), int(GRID_SIZE / 2)), int(GRID_SIZE / 3), 3)

def init_all_court_tiles(play_court):
    for k in range(X_TILES):
        for j in range(Y_TILES):
            if j == int(Y_TILES / 2) and (k == 0 or k == X_TILES - 1):
                # Set up the special BasketTiles
                tile = BasketTile(k, j)
            else:
                tile = CourtTile(k, j)
            tile.rect.topleft = ((k + 1) * (1 + GRID_PADDING) * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[0],
                                 (j + 1) * (1 + GRID_PADDING) * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[1])

def init_all_court_fields():
    score_board = CourtField(CL_SCORE, (X_SIZE, Y_SCORE_SIZE), 'score_board')
    score_board.rect.topleft = (0, 0)

    play_court = CourtField(CL_COURT, (X_SIZE, Y_COURT_SIZE), 'play_court')
    play_court.rect.topleft = score_board.rect.bottomleft
