import circleshape
import pygame
import constants

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = 0

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)