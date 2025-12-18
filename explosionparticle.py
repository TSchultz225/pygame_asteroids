import circleshape
import constants
import pygame

class ExplosionParticle(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.EXPLOSION_RADIUS)
        self.velocity = 0
        self.current_life_length = 0

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.current_life_length += dt
