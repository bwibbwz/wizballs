""" Class to handle possible actions

    MOVE actions: RIGHT, LEFT, UP, DOWN

"""

import pygame
import random

from conf import *

dr = GRID_SIZE

class WizBallsActions:

    def __init__(self, rect):
        # LOG previous player actions
        self.log = []
        self.rect = rect

    def check_log(self):
        #
        pass

    def update(self, action):
        # Movement
        if action == 'RIGHT':
            self.rect.move_ip(dr,0)
        elif action == 'LEFT':
            self.rect.move_ip(-dr,0)
        elif action == 'UP':
            self.rect.move_ip(0,-dr)
        elif action == 'DOWN':
            self.rect.move_ip(0,dr)
