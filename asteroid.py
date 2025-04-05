import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
            # Draw the asteroid as a circle
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update(self, dt):
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt
        # Moves asteroid in a straight line randomly
        self.position.x += random.randint(-1, 1)
        self.position.y += random.randint(-1, 1)