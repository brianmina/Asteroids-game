import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.velocity = velocity if velocity else pygame.math.Vector2(0, 0)


    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position.x, self.position.y, new_radius, new_velocity1 * 1.2)
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity2 * 1.2)
