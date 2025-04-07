import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
    # Convert self.position to a tuple of integers
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt
        # Moves asteroid in a straight line randomly
        self.position.x += random.randint(-1, 1)
        self.position.y += random.randint(-1, 1)