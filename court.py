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
            court_picture = pygame.image.load('img/wood-floor-tileable.jpg').convert()
            court_picture = pygame.transform.scale(court_picture, (self.rect.size))
            court_picture.set_alpha(BG_COURT_OPACITY)
            self.image.blit(court_picture, court_picture.get_rect())

            pygame.draw.line(self.image, CL_BLACK, self.rect.midtop, self.rect.midbottom, 3)
            pygame.draw.circle(self.image, CL_BLACK, self.rect.center, GRID_SIZE, 3)

            penalty_box1 = pygame.draw.rect(self.image,
                             CL_BLACK, 
                             (self.rect.right - 4 * (GRID_SIZE + GRID_PADDING),
                             self.rect.centery - 1.5 * (GRID_SIZE + GRID_PADDING),
                             4 * (GRID_SIZE + GRID_PADDING),
                             3 * (GRID_SIZE + GRID_PADDING)),
                             3)
            pygame.draw.circle(self.image, CL_BLACK, penalty_box1.midleft, GRID_SIZE, 3)

            penalty_box2 = pygame.draw.rect(self.image,
                             CL_BLACK, 
                             (self.rect.left,
                             self.rect.centery - 1.5 * (GRID_SIZE + GRID_PADDING),
                             4 * (GRID_SIZE + GRID_PADDING),
                             3 * (GRID_SIZE + GRID_PADDING)),
                             3)
            pygame.draw.circle(self.image, CL_BLACK, penalty_box2.midright, GRID_SIZE, 3)

            
        self.name = name

class CourtTile(SelectableSprite):
    def __init__(self, x, y):
        SelectableSprite.__init__(self, main_color = CL_TILES, selected_color = CL_RED)

        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE], pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

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

class CommandTile(SelectableSprite):
    def __init__(self, name, symbol):
        SelectableSprite.__init__(self, main_color = CL_RED, selected_color = CL_BLACK)

        font_type = pygame.font.SysFont('comicsansms', 72)
        text_surface = font_type.render(symbol, True, [0, 0, 0])
        text_surface = pygame.transform.scale(text_surface, [GRID_SIZE // 2, GRID_SIZE // 2])

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
            tile.rect.midleft = [0.5 * GRID_SIZE + ref_pos[0], ref_pos[1]]
        elif name == 'right':
            tile.rect.midleft = [1.5 * GRID_SIZE + ref_pos[0], ref_pos[1]]
        elif name == 'up':
            tile.rect.midleft = [1 * GRID_SIZE + ref_pos[0], -0.5 * GRID_SIZE + ref_pos[1]]
        elif name == 'down':
            tile.rect.midleft = [1 * GRID_SIZE + ref_pos[0], 0.5 * GRID_SIZE + ref_pos[1]]
        elif name == 'submit':
            tile.rect.midleft = [3 * GRID_SIZE, ref_pos[1]]
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
            tile.rect.topleft = ((k + 1) * (1 + GRID_PADDING) * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[0],
                                 (j + 1) * (1 + GRID_PADDING) * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[1])

def init_all_court_fields():
    score_board = CourtField(CL_SCORE, (X_SIZE, Y_SCORE_SIZE), 'score_board')
    score_board.rect.topleft = (0, 0)

    play_court = CourtField(CL_COURT, (X_SIZE, Y_COURT_SIZE), 'play_court')
    play_court.rect.topleft = score_board.rect.bottomleft
