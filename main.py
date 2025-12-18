import sys
import math
import pygame
import player
import asteroid
import asteroidfield
import shot
import explosionparticle
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import EXPLOSION_PARTICLE_LIFE
from constants import ASTEROID_POINT_VALUE
from logger import log_state
from logger import log_event

def main():
    pygame.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    score = 0

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosion_particles = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)
    explosionparticle.ExplosionParticle.containers = (explosion_particles,drawable,updatable)

    game_player = player.Player(SCREEN_WIDTH /2,SCREEN_HEIGHT /2)

    asteroid_field = asteroidfield.AsteroidField()

    #GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        updatable.update(dt)
        text_surface = my_font.render(f"Score: {math.floor(score)}", False, (180, 180, 180))
        for asteroid_obj in asteroids:
            if asteroid_obj.collides_with(game_player):
                log_event("player_hit")
                print("Game over!")
                print(f"{score}")
                sys.exit()
                
        score += dt

        for asteroid_obj in asteroids:
            for shot_obj in shots:
                if asteroid_obj.collides_with(shot_obj):
                    log_event("asteroid_shot")
                    asteroid_obj.split()
                    shot_obj.kill()
                    score += ASTEROID_POINT_VALUE

        for explo_part_obj in explosion_particles:
            if explo_part_obj.current_life_length >= EXPLOSION_PARTICLE_LIFE:
                explo_part_obj.kill()

        for draw_able in drawable:
            draw_able.draw(screen)
        screen.blit(text_surface, (SCREEN_WIDTH / 2.4 , 0))
        pygame.display.flip()
        
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
