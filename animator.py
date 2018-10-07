""" Class to handle animations
"""

import pygame
from conf import *

class AnimateMove():

    def __init__(self, images, interval):

        self.animate = False
        self.images  = images
        self.interval = interval
        self.max_idx  = len(images)

        self.idx     = 0
        self.counter = 0

        #
        self.dX = 0
        self.dY = 0
        self.end = None

    @property
    def image(self):
        return self.images[self.idx]

    def iterate(self):
        self.idx += 1
        self.counter += 1

    def update(self, rect, rotate=False, team=-1):
        if not self.animate:
            pass

        if rotate:
            return self.rotate(team)

        self.iterate()
        #
        if self.idx == self.max_idx:
             self.idx = 0

        rect.x += self.dX
        rect.y += self.dY

        if self.counter == self.interval:
            self.idx = 0
            rect.center = self.end
            self.animate = False

        return self.image

    def rotate(self, team):
        pass

    def initialize(self, beg, end):        
        self.counter = 0

        X = end[0] - beg[0]
        Y = end[1] - beg[1]

        self.dX = X // self.interval
        self.dY = Y // self.interval

        self.end = end
