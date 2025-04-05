import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # take 1 argument (another CircleShape object) and return True or False
    def is_colliding(self, other, others):
        distance = self.position.distance_to(other.position)
        if distance < (self.radius + other.radius):
            return True
        
        for obj in others:
            distance = self.position.distance_to(obj.position)
            if distance < (self.radius + obj.radius):
                return True
            
        return False

    # def is_colliding(self, other):
    #     distance = self.position.distance_to(other.position)
    #     print(f"Self position: {self.position}, Radius: {self.radius}")
    #     print(f"Other position: {other.position}, Radius: {other.radius}")
    #     print(f"Distance: {distance}, Sum of radii: {self.radius + other.radius}")
    #     return distance < (self.radius + other.radius)