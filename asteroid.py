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

    def split(self):
        # Split the asteroid into two smaller asteroids
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(random_angle) # scale up by 1.2
            new_velocity2 = self.velocity.rotate(-random_angle) # scale up by 1.2

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            # Set their velocities
            new_asteroid1.velocity = new_velocity1
            new_asteroid2.velocity = new_velocity2
            # Add new asteroids to the appropriate group
            for container in self.containers:
                container.add(new_asteroid1)
                container.add(new_asteroid2)
        # Remove the original asteroid
        self.kill()