import pygame, random
from conf import *

class Explode(pygame.sprite.Sprite):
    """ Explosions which throw 'cubic' fragments around.  
        The fragments fall down off the screen due to 'gravity'.
    """
    gravity = True

    def __init__(self, sprite):
        #
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.dx = random.randint(-GRID_SIZE*2, GRID_SIZE*2) # vel-x
        self.dy = random.randint(-GRID_SIZE*2, GRID_SIZE*2) # vel-y

        self.image = pygame.Surface([random.randint(5,GRID_SIZE/2), 
                                     random.randint(5,GRID_SIZE/2)])
        # Color
        self.image.fill(sprite.color)
        self.image.set_alpha(225) # Start slightly faded

        self.rect = self.image.get_rect()
        self.rect.topleft = sprite.rect.topleft

        #
        self.lifetime = 1 + random.randint(0,99)
        self.time = 0


    def update(self, dt=0.1):
        #
        if self.time > self.lifetime:
            self.kill()
        
        # Fade out according to lifetime.
        self.image.set_alpha(225 - 224 / self.lifetime)
        # need to get rect again? Not sure this is working

        self.time += 1

        dx = self.dx * dt
        dy = self.dy * dt # integrator: (v + g * dt) * dt

        if Explode.gravity:
            self.dy += FORCE_OF_GRAVITY * dt

        self.rect.x += round(dx,0)
        self.rect.y += round(dy,0)
