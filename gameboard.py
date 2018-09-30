#!/usr/bin/env python3

import pygame

# Import static parameters
from conf import *

from groups import CourtGroup

COURT_RATIO = 0.8

def draw_gameboard():
    gameSurface = pygame.display.get_surface()
    gameSurface.fill(CL_BG)

    score_board = Court(CL_SCORE, (X_SIZE - 2 * GRID_SIZE, Y_SIZE - GRID_SIZE - COURT_RATIO * Y_SIZE))
    play_court = Court(CL_COURT, (X_SIZE - 2 * GRID_SIZE, Y_SIZE - 2 * GRID_SIZE - (1.0 - COURT_RATIO) * Y_SIZE))
    
    score_board.rect.topleft = [GRID_SIZE, GRID_SIZE]
    play_court.rect.bottomleft = [GRID_SIZE, Y_SIZE - GRID_SIZE]

    courts = CourtGroup()
    courts.add(score_board)
    courts.add(play_court)
    
    courts.draw(gameSurface)

class Court(pygame.sprite.Sprite):
    def __init__(self, color, size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface(size)
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        
