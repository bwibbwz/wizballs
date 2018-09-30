# Various Groups which handle different sprites
import pygame

class PlayerGroup(pygame.sprite.OrderedUpdates):
    # Group to handle player sprites

    def __init__(self):
        #
        pygame.sprite.OrderedUpdates.__init__(self)

class CourtGroup(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)


