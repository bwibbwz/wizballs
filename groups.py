# Various Groups which handle different sprites
import pygame

class Group(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def find_by_name(self, search):
        return [sprite for sprite in self.sprites() if sprite.name == search]

class SingleSelectableSpriteGroup(Group):
    def __init__(self):
        Group.__init__(self)

    def select_sprite(self, sprite):
        sprite.select()
        self.deselect_all_other_sprites(sprite)
        # NB: Should raise an error if the sprite is not found.

    def deselect_sprite(self, sprite):
        sprite.deselect()
    
    def deselect_all_other_sprites(self, sprite):
        for s in self.sprites():
            if s != sprite:
                s.deselect()

    def deselect_all_sprites(self):
        for s in self.sprites():
            s.deselect()

class CourtTilesGroup(Group):
    def __init__(self):
        Group.__init__(self)

    def get_tile(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            raise IndexError('Negative numbers are not allowed when addressing the tile grid.')
        found_tiles = [tile for tile in self.sprites() if tile.pos == pos]
        if len(found_tiles) == 1:
            return found_tiles[0]
        elif len(found_tiles) > 0:
            raise IndexError('Multiple tiles were found. This should not happen.')
        else:
            raise IndexError('No tiles were found with index (%i, %i).' % (pos[0], pos[1]))

class PlayersGroup(pygame.sprite.OrderedUpdates):
    # Group to handle player sprites

    def __init__(self):
        #
        pygame.sprite.OrderedUpdates.__init__(self)
