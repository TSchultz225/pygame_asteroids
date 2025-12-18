import sys
import pygame
import player
import asteroid
import asteroidfield
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from logger import log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
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

        for asteroid_obj in asteroids:
            if asteroid_obj.collides_with(game_player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for draw_able in drawable:
            draw_able.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
