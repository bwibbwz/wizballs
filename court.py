#!/usr/bin/env python3

import pygame
from conf import *

class CourtLine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
class CourtField(pygame.sprite.Sprite):
    def __init__(self, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

class CourtTiles(pygame.sprite.Sprite):
    def __init__(self, color, pos, size):
        pass

def initialise_all_court_fields():
    score_board = CourtField(CL_SCORE, (X_SIZE - 2 * GRID_SIZE, Y_SIZE - GRID_SIZE - COURT_RATIO * Y_SIZE))
    score_board.rect.topleft = [GRID_SIZE, GRID_SIZE]
    
    play_court = CourtField(CL_COURT, (X_SIZE - 2 * GRID_SIZE, Y_SIZE - 2 * GRID_SIZE - (1.0 - COURT_RATIO) * Y_SIZE))
    play_court.rect.bottomleft = [GRID_SIZE, Y_SIZE - GRID_SIZE]

    court_fields_group = pygame.sprite.Group()
    court_fields_group.add(score_board)
    court_fields_group.add(play_court)

    return court_fields_group
