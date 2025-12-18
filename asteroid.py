import random
from logger import log_event
import circleshape
import pygame
import constants
import explosionparticle

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
            
            explo_particle1_random_angle = random.uniform(5,55)
            explo_particle2_random_angle = random.uniform(65,115)
            explo_particle3_random_angle = random.uniform(125,175)

            explo_particle1_new_rotation = self.velocity.rotate(explo_particle1_random_angle)
            explo_particle1 = explosionparticle.ExplosionParticle(self.position.x, self.position.y)
            explo_particle1.velocity = explo_particle1_new_rotation * 0.8
            
            explo_particle2_new_rotation = self.velocity.rotate(explo_particle2_random_angle)
            explo_particle2 = explosionparticle.ExplosionParticle(self.position.x, self.position.y)
            explo_particle2.velocity = explo_particle2_new_rotation * 0.8
            
            explo_particle3_new_rotation = self.velocity.rotate(explo_particle3_random_angle)
            explo_particle3 = explosionparticle.ExplosionParticle(self.position.x, self.position.y)
            explo_particle3.velocity = explo_particle3_new_rotation * 0.8

            explo_particle4_new_rotation = self.velocity.rotate(-explo_particle1_random_angle)
            explo_particle4 = explosionparticle.ExplosionParticle(self.position.x, self.position.y)
            explo_particle4.velocity = explo_particle4_new_rotation * 0.8
            
            explo_particle5_new_rotation = self.velocity.rotate(-explo_particle2_random_angle)
            explo_particle5 = explosionparticle.ExplosionParticle(self.position.x, self.position.y)
            explo_particle5.velocity = explo_particle5_new_rotation * 0.8
            
            explo_particle6_new_rotation = self.velocity.rotate(-explo_particle3_random_angle)
            explo_particle6 = explosionparticle.ExplosionParticle(self.position.x, self.position.y)
            explo_particle6.velocity = explo_particle6_new_rotation * 0.8
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