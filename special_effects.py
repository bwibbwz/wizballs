import pygame, random
from conf import *

class Explode(pygame.sprite.Sprite):
    """ Explosion which throws one fragment around.  
        The fragment falls down off the screen due to 'gravity'.
    """
    gravity = True

    def __init__(self, sprite):
        #
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.dx = random.randint(-GRID_SIZE*2, GRID_SIZE*2) # vel-x
        self.dy = random.randint(-GRID_SIZE*2, GRID_SIZE*2) # vel-y

        # 
        self.image = pygame.Surface([random.randint(3, GRID_SIZE // 5), 
                                     random.randint(3, GRID_SIZE // 5)])

        self.alpha = 225
        # Color
        self.image.fill(sprite.color)
        self.image.set_alpha(self.alpha) # Start slightly faded

        self.rect = self.image.get_rect()
        self.rect.center = sprite.rect.center

        #
        self.lifetime = 1 + random.randint(0,99)
        self.time = 0


    def update(self, dt=0.1):
        #
        if (self.time > self.lifetime 
            or self.rect.x < 0 
            or self.rect.x > X_SIZE
            or self.rect.y > Y_SIZE):
            self.kill()
       
        self.alpha -= 224 / self.lifetime
        # Fade out relative to lifetime.
        self.image.set_alpha(self.alpha)

        self.time += 1

        dx = self.dx * dt
        dy = self.dy * dt # integrator: (v + g * dt) * dt

        if Explode.gravity:
            self.dy += FORCE_OF_GRAVITY * dt

        self.rect.x += round(dx,0)
        self.rect.y += round(dy,0)
