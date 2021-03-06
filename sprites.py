#!/usr/bin/env python3

import pygame
import logging as l
from conf import *
from groups import SingleSelectableSpriteGroup

class HighlightableSprite():
    def __init__(self, main_color=CL_ALPHA, highlighted_color=CL_BLUE):
        self._highlighted = False
        self._highlighted_color = highlighted_color
        self._main_color = main_color
        self._active_color = main_color

    # NB: Need to make sure this works properly with selected.
    def highlight(self):
        self._active_color = self._highlighted_color
        self._highlighted = True

    def dehighlight(self):
        self._active_color = self._main_color
        self._highlighted = False

    def is_highlighted(self):
        return self._highlighted == True

class SelectableSprite(pygame.sprite.Sprite):
    def __init__(self, main_color=CL_ALPHA, selected_color=CL_RED):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self._selected = False
        self._selected_color = selected_color
        self._main_color = main_color
        self._active_color = main_color

    def select(self):
        self._active_color = self._selected_color
        self._selected = True
        for group in self.groups:
            if group.__class__ == SingleSelectableSpriteGroup:
                group.deselect_all_other_sprites(self)

    def deselect(self):
        self._active_color = self._main_color
        self._selected = False

    def is_selected(self):
        return self._selected == True
