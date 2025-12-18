import random
from logger import log_event
import circleshape
import pygame
import constants

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position+= (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        new_rotation_asteroid1 = self.velocity.rotate(random_angle)
        new_rotation_asteroid2 = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

        asteroid1.velocity = new_rotation_asteroid1 * 1.2
        asteroid2.velocity = new_rotation_asteroid2 * 1.2