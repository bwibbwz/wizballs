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

        self.rect.topleft = sprite.rect.topleft

        #
        self.lifetime = 1 + random.randint(0,99)
        self.time = 0


    def update(self):
        #
        dt = 0.1
        
        if self.time > self.lifetime:
            self.kill()
        
        self.time += 1

        dx = self.dx * dt
        dy = self.dy * dt # integrator: (v + g * dt) * dt

        if Explode.gravity:
            self.dy += FORCE_OF_GRAVITY * dt

        self.rect.x += round(dx,0)
        self.rect.y += round(dy,0)

