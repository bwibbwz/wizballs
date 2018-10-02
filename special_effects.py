import pygame, random
from conf import *

class Explode(pygame.sprite.Sprite):
    """ Explosions which throw fragments around.  
        The fragments fall down off the screen due to gravity.

    """
    gravity = True

    def __init__(self, sprite): # tuples
        #
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = sprite.rect.copy()

        self.dx = random.randint(-GRID_SIZE, GRID_SIZE) # vel-x
        self.dy = random.randint(-GRID_SIZE, GRID_SIZE) # vel-y

        # Set up here surface image and corresponding rect -->
        self.image = pygame.Surface((GRID_SIZE/2, GRID_SIZE/2))
        #
        # -- Need to ctrl colors here
        self.image.fill(sprite.color)
        pygame.draw.circle(self.image, (random.randint(1,32),0,0),
                                       (5,5),
                                       random.randint(2,5))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.lifetime = 1 + random.randint(0,99)
        self.maxspeed = sprite.speed * 2
        self.time = 0

    def update(self):
        #
        seconds = 0.1
        
        if self.time > self.lifetime:
            self.kill()
        
        self.time += 1

        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds # integrator: (v + g * ds) * ds

        if Explode.gravity:
            self.dy += FORCE_OF_GRAVITY * seconds

        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

