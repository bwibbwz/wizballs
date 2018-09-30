#!/usr/bin/env python3

import pygame, logging
from conf import *
from groups import Group, CourtTilesGroup

class CourtLine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
class CourtField(pygame.sprite.Sprite):
    def __init__(self, color, size, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.name = name

class CourtTile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE])
        self.image.fill(CL_TILES)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

def init_all_court_tiles(play_court):
    court_tiles_group = CourtTilesGroup()
    for k in range(X_TILES):
        for j in range(Y_TILES):
            tile = CourtTile(k, j)
            tile.rect.topleft = [(k + 1) * 2 * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[0], (j + 1) * 2 * GRID_SIZE - GRID_SIZE + play_court.rect.topleft[1]]
            logging.debug(tile.rect.topleft)
            court_tiles_group.add(tile)
            
    return court_tiles_group
    

def init_all_court_fields():
    score_board = CourtField(CL_SCORE, (X_SIZE - 2 * GRID_SIZE, Y_SIZE - GRID_SIZE - COURT_RATIO * Y_SIZE), 'score_board')
    score_board.rect.topleft = [GRID_SIZE, GRID_SIZE]
    
    play_court = CourtField(CL_COURT, (X_SIZE - 2 * GRID_SIZE, Y_SIZE - 2 * GRID_SIZE - (1.0 - COURT_RATIO) * Y_SIZE), 'play_court')
    play_court.rect.bottomleft = [GRID_SIZE, Y_SIZE - GRID_SIZE]

    court_fields_group = Group()
    court_fields_group.add(score_board)
    court_fields_group.add(play_court)

    return court_fields_group
