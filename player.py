import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    containers = None
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = []
        self.shoot_timer = 0
        if Player.containers:
            for group in Player.containers:
                group.add(self)


    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    
    def update(self, dt, shots_group):
        keys = pygame.key.get_pressed()

        if self.shoot_timer > 0 :
            self.shoot_timer -= dt
        
        if self.shoot_timer < 0 :
            self.shoot_timer = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(shots_group)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, shots_group):

        if  self.shoot_timer > 0 : 
            return
        

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        tip_position = self.position - forward * self.radius
        
        # Create a new Shot at the Player's current position
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        
        self.shoot_timer =  PLAYER_SHOOT_COOLDOWN

        # Set initial velocity (use a vector pointing upward and rotate it by player's angle)
        velocity = -forward * PLAYER_SHOOT_SPEED 
        
        shot.velocity = velocity

        # Add the shot to a group (like `shots` list or sprite group)
        self.shots.append(shot)   
        
