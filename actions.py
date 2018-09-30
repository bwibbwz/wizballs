""" Class to handle possible actions

    MOVE actions: RIGHT, LEFT, UP, DOWN

"""

import pygame
import random

from conf import *

dr = GRID_SIZE

class WizBallsActions:

    def __init__(self):
        # LOG previous player actions
        self.log = []

    def check_log(self):
        #
        pass

    def update(self, action):
        # Movement
        if action == 'RIGHT':
            self.rect.x += dr
        elif action == 'LEFT':
            self.rect.x -= dr
        elif action == 'UP':
            self.rect.y -= dr
        elif action == 'DOWN':
            self.rect.y += dr
