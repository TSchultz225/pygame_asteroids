import circleshape
import constants
import pygame
import shot

class Player(circleshape.CircleShape):
    rotation = 0
    shot_cooldown = 0

    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),constants.LINE_WIDTH)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self,dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        else:
            self.shot_cooldown = constants.PLAYER_SHOOT_COOLDOWN_SECONDS

        bullet_shot = shot.Shot(self.position.x, self.position.y)
        velocity_vector = pygame.Vector2(0,1)
        rotated_velocity_vector = velocity_vector.rotate(self.rotation)
        shoot_speed_vector = rotated_velocity_vector * constants.PLAYER_SHOOT_SPEED
        bullet_shot.velocity = shoot_speed_vector
