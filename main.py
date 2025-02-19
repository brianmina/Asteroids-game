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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        

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

