# Various Groups which handle different sprites
import pygame

class AllSprites(pygame.sprite.LayeredUpdates):
    def __init__(self):
        pygame.sprite.LayeredUpdates.__init__(self)

class Group(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def find_by_name(self, search):
        return [sprite for sprite in self.sprites() if sprite.name == search]

class CourtTilesGroup(Group):
    def __init__(self):
        Group.__init__(self)

    def get_tile(self, x, y):
        x_sprites = [sprite for sprite in self.sprites() if sprite.x == x]
        return [sprite for sprite in x_sprites if sprite.y == y][0]

class PlayerGroup(pygame.sprite.OrderedUpdates):
    # Group to handle player sprites

    def __init__(self):
        #
        pygame.sprite.OrderedUpdates.__init__(self)

    def update_render(self):
        #
        for s in self.sprites():
            s.update_render()

class SpecialEffectsGroup(pygame.sprite.Group):
    """ Group to handle special effects (explosions)
    """

    def __init__(self):
        #
        pygame.sprite.Group.__init__(self)
