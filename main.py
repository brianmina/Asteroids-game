import pygame
from constants import *
import sys
from player import Player
from asteroid import *
from asteroidfield import AsteroidField
from circleshape import CircleShape
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

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Spacebar pressed
                if event.key == pygame.K_SPACE:
                    player.shoot()  # Call your shoot method

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:   # Rotate player counterclockwise
                    player.angle += 10
                elif event.key == pygame.K_RIGHT:  # Rotate player clockwise
                    player.angle -= 10

            if event.type == pygame.QUIT:
                :pygame.quit()
                sys.exit()

        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        for shot in player.shots:
            shot.update(dt)
        

        # Remove shots out of bounds
        player.shots = [shot for shot in player.shots if 0 <= shot.position.x <= screen_width and 0 <= shot.position.y <= screen_height]
        

        for shot in player.shots:
            shot.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over")
                sys.exit()


        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main() 

