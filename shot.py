import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
    # Convert self.position to a tuple of integers
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        # Update the shot's position based on its velocity
        self.position += self.velocity * dt
        # Check if the shot is out of bounds and remove it if necessary
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
        self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()