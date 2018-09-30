import pygames, random
from conf import *

class Explosions(pygame.sprite.Sprite):
    """ Explosions which throw fragments around.  
        The fragments fall down off the screen due to gravity.

    """
    gravity = True

    def __init__(self, pos, color, speed): # tuples
        #
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = pos

        self.dx = random.randint(-speed,speed) # vel-x
        self.dy = random.randint(-speed,speed) # vel-y

        # Set up here surface image and corresponding rect -->

    def update(self, seconds):
        #
        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds # integrator: (v + g * ds) * ds

        if Explosions.gravity:
            self.dy += FORCE_OF_GRAVITY * seconds

        self.rect.centerx = round(self.pos[0],0)
        self.rect.centery = round(self.pos[1],0)
