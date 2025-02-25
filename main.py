import pygame
from constants import *
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        dt = clock.tick(60) / 1000
        

         # Update all non-player sprites
        for sprite in updatable:
            if not isinstance(sprite, Player):
                sprite.update(dt)

        player.update(dt, shots_group)
        

        # Remove shots out of bounds
        player.shots = [shot for shot in player.shots if 0 <= shot.position.x <= SCREEN_WIDTH and 0 <= shot.position.y <= SCREEN_HEIGHT]
        

        for shot in shots_group:
            shot.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots_group:
                if shot.collides_with(asteroid):
                    asteroid.kill()
                    shot.kill()

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main() 

