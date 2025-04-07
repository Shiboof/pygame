from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, radius)
        #call parent class constructor passing in player_radius
        self.player_radius = radius
        # create a field called rotation, initialized to 0
        self.rotation = 0
        self.shoot_timer = 0.0 # Timer variable initialized to 0

    def draw(self, screen):
    # Convert triangle vertices to tuples of integers
        pygame.draw.polygon(screen, (255, 255, 255), [(int(v.x), int(v.y)) for v in self.triangle()])
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def update(self, dt):
        # Decrement the shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            # Rotate left
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            # Rotate right
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            # Move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # Move backward
            self.move(dt)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            # Move forward
            self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_TURN_SPEED * dt
        if keys[pygame.K_s]:
            # Move backward
            self.position += pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_TURN_SPEED * dt
    
    def shoot(self, updatable, drawable, shots):
        # Calculate the forward direction based on the player's rotation
        if self.shoot_timer <= 0:
            # Reset the shoot timer
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            # Calculate the position of the shot
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot_position = self.position + forward * self.radius

            # Create the shot with the calculated position and velocity
            velocity = forward * PLAYER_SHOOT_SPEED
            shot = Shot(shot_position.x, shot_position.y, velocity)

            # Add the shot to the appropriate sprite groups
            updatable.add(shot)
            drawable.add(shot)
            shots.add(shot)