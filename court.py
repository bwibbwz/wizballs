#!/usr/bin/env python3

import pygame
import logging as l
from conf import *
from groups import Group, CourtTilesGroup
from sprites import SelectableSprite
from graphics_functions import draw_border, copy_color

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
            self.image = pygame.image.load('img/wood-floor-tileable.jpg').convert()
            self.image = pygame.transform.scale(self.image, (self.rect.size))

        self.name = name

class CourtTile(SelectableSprite):
    def __init__(self, x, y):
        SelectableSprite.__init__(self, main_color = CL_TILES, selected_color = CL_RED)

        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE], pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        # NB: Need a better way to do this.
        self._fill_opacity = 50

        self.update()

    def update(self):
        self.image.fill(copy_color(self._active_color, alpha = self._fill_opacity))
        draw_border(self.image, color = self._active_color)

class BasketTile(CourtTile):
    def __init__(self, x, y):
        CourtTile.__init__(self, x, y)

    def update(self):
        self.image.fill(copy_color(self._active_color, alpha = 150))
        draw_border(self.image, color = self._active_color)
        # BUG: The basket itself should be drawn on top of the player sprite. 
        pygame.draw.circle(self.image, CL_BLACK, (int(GRID_SIZE / 2), int(GRID_SIZE / 2)), int(GRID_SIZE / 3), 3)

class CommandTile(SelectableSprite):
    def __init__(self, name, symbol):
        SelectableSprite.__init__(self)

        font_type = pygame.font.SysFont('comicsansms', 72)
        text_surface = font_type.render(symbol, True, [0, 0, 0])
        text_surface = pygame.transform.scale(text_surface, [GRID_SIZE, GRID_SIZE])

        self.image = text_surface
        self.rect = text_surface.get_rect()

        self.name = name
        self.symbol = symbol

def init_all_command_tiles(score_board):
    ref_pos = score_board.rect.midleft
    commands = {'left': '<', 'right': '>', 'up': '^', 'down': 'v', 'submit': 'S', 'endturn': 'T'}
    for name, symbol in commands.items():
        tile = CommandTile(name, symbol)
        if name == 'left':
            tile.rect.midleft = [1 * GRID_SIZE + ref_pos[0], ref_pos[1]]
        elif name == 'right':
            tile.rect.midleft = [3 * GRID_SIZE + ref_pos[0], ref_pos[1]]
        elif name == 'up':
            tile.rect.midleft = [2 * GRID_SIZE + ref_pos[0], -1 * GRID_SIZE + ref_pos[1]]
        elif name == 'down':
            tile.rect.midleft = [2 * GRID_SIZE + ref_pos[0], 1 * GRID_SIZE + ref_pos[1]]
        elif name == 'submit':
            tile.rect.midleft = [6 * GRID_SIZE, ref_pos[1]]
        elif name == 'endturn':
            tile.rect.midleft = [8 * GRID_SIZE, ref_pos[1]]

def init_all_court_tiles(play_court):
    for k in range(X_TILES):
        for j in range(Y_TILES):
            if j == int(Y_TILES / 2) and (k == 0 or k == X_TILES - 1):
                # Set up the special BasketTiles
                tile = BasketTile(k, j)
            else:
                tile = CourtTile(k, j)
            tile.rect.topleft = [(k + 1) * 1.1 * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[0], (j + 1) * 1.1 * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[1]]

def init_all_court_fields():
    score_board = CourtField(CL_SCORE, (X_SIZE - GRID_SIZE, Y_SIZE - 0.5 * GRID_SIZE - COURT_RATIO * Y_SIZE), 'score_board')
    score_board.rect.topleft = [0.5 * GRID_SIZE, 0.5 * GRID_SIZE]
    
    play_court = CourtField(CL_COURT, (X_SIZE - GRID_SIZE, Y_SIZE - GRID_SIZE - (1.0 - COURT_RATIO) * Y_SIZE), 'play_court')
    play_court.rect.bottomleft = [0.5 * GRID_SIZE, Y_SIZE - 0.5 * GRID_SIZE]
