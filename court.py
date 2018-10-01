#!/usr/bin/env python3

import pygame
import logging as l
from conf import *
from groups import Group, CourtTilesGroup
from sprites import SelectableSprites

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

        self.name = name

class CourtTile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE])
        self.image.fill(CL_TILES)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

class CommandTile(SelectableSprite):
    def __init__(self, name, symbol):
        pygame.sprite.Sprite.__init__(self, self.groups)

        font_type = pygame.font.SysFont('comicsansms', 72)
        text_surface = font_type.render(symbol, True, [0, 0, 0])
        text_surface = pygame.transform.scale(text_surface, [2 * GRID_SIZE, 2 * GRID_SIZE])

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
            tile.rect.midleft = [2 * GRID_SIZE + ref_pos[0], ref_pos[1]]
        elif name == 'right':
            tile.rect.midleft = [6 * GRID_SIZE + ref_pos[0], ref_pos[1]]
        elif name == 'up':
            tile.rect.midleft = [4 * GRID_SIZE + ref_pos[0], -2 * GRID_SIZE + ref_pos[1]]
        elif name == 'down':
            tile.rect.midleft = [4 * GRID_SIZE + ref_pos[0], 2 * GRID_SIZE + ref_pos[1]]
        elif name == 'submit':
            tile.rect.midleft = [11 * GRID_SIZE, ref_pos[1]]
        elif name == 'endturn':
            tile.rect.midleft = [15 * GRID_SIZE, ref_pos[1]]

def init_all_court_tiles(play_court):
    for k in range(X_TILES):
        for j in range(Y_TILES):
            tile = CourtTile(k, j)
            tile.rect.topleft = [(k + 1) * 2 * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[0], (j + 1) * 2 * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[1]]

def init_all_court_fields():
    score_board = CourtField(CL_SCORE, (X_SIZE - 2 * GRID_SIZE, Y_SIZE - GRID_SIZE - COURT_RATIO * Y_SIZE), 'score_board')
    score_board.rect.topleft = [GRID_SIZE, GRID_SIZE]
    
    play_court = CourtField(CL_COURT, (X_SIZE - 2 * GRID_SIZE, Y_SIZE - 2 * GRID_SIZE - (1.0 - COURT_RATIO) * Y_SIZE), 'play_court')
    play_court.rect.bottomleft = [GRID_SIZE, Y_SIZE - GRID_SIZE]
