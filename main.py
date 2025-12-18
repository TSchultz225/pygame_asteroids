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
    #initialize pygame
    pygame.init()
    
    #create font for score display
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    #create game screen for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #debug info
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #score tracking info
    score = 0
    asteroids_shot = 0

    #create game clock and delta time vars
    game_clock = pygame.time.Clock()
    dt = 0

    #sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosion_particles = pygame.sprite.Group()

    #class sprite group additions
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)
    explosionparticle.ExplosionParticle.containers = (explosion_particles,drawable,updatable)

    #create player instance
    game_player = player.Player(SCREEN_WIDTH /2,SCREEN_HEIGHT /2)

    #create asteroid field instance
    asteroid_field = asteroidfield.AsteroidField()

    #define player as not dead - will allow to break game loop
    playerDead = False

    #GAME LOOP
    while playerDead!= True:
        
        #Allows the exit button to function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #log game state to log file                
        log_state()

        #fill the screen black
        screen.fill("black")
        
        # Sets the delta time to update all updatable objects with
        updatable.update(dt)

        #check if player collides with asteroid
        for asteroid_obj in asteroids:
            if asteroid_obj.collides_with(game_player):
                log_event("player_hit")
                playerDead = True

        #update player score                
        score += dt

        #check if shots collide with asteroids
        for asteroid_obj in asteroids:
            for shot_obj in shots:
                if asteroid_obj.collides_with(shot_obj):
                    log_event("asteroid_shot")
                    asteroid_obj.split()
                    shot_obj.kill()

                    #update score with asteroid point value
                    #TODO: Update with formal score class
                    score += ASTEROID_POINT_VALUE
                    asteroids_shot += 1

        #check for explosion particle expiration
        for explo_part_obj in explosion_particles:
            if explo_part_obj.current_life_length >= EXPLOSION_PARTICLE_LIFE:
                explo_part_obj.kill()

        #draw all drawable objects
        for draw_able in drawable:
            draw_able.draw(screen)

        #create text_surface to display score
        text_surface = my_font.render(f"Score: {math.floor(score)}", False, (180, 180, 180))

        #display score board
        if playerDead!=True:
            screen.blit(text_surface, (SCREEN_WIDTH / 2.4 , 0))

        #refresh game display
        pygame.display.flip()
        
        #update delta time
        dt = game_clock.tick (60) / 1000
    
    #scoreboard
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        text_surface = my_font.render(f"Score: {math.floor(score)}", False, (180, 180, 180))
        text_surface2 = my_font.render(f"Asteroids Shot: {asteroids_shot}", False, (180, 180, 180))
        screen.blit(text_surface, (SCREEN_WIDTH / 2.4 , SCREEN_HEIGHT / 2.2 ))
        screen.blit(text_surface2, (SCREEN_WIDTH / 2.4 , SCREEN_HEIGHT / 1.8 ))
        pygame.display.flip()

if __name__ == "__main__":
    main()
