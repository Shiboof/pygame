from circleshape import CircleShape
import pygame
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, radius)
        #call parent class constructor passing in player_radius
        self.player_radius = radius
        # create a field called rotation, initialized to 0
        self.rotation = 0

    def draw(self, screen):
        # Draw the player as a triangle
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle())
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(dt):
        rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
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