#!/usr/bin/env python3

import pygame
import logging as l
from conf import *

class SelectableSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.selected = False

