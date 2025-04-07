import pygame
from player import Player
from constants import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Sprite Groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
# Add sprite groups to containers

Player.containers = updatable, drawable
Asteroid.containers = updatable, drawable, asteroids   
AsteroidField.containers = updatable  # Only updatable!

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create player at center
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # Add player to the updatable and drawable groups
    updatable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()

    collision_detected = False # Flag to track collisions state

    running = True
    while running:
        dt = clock.tick(60) / 1000  # delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Call the player's shoot method
                    player.shoot(updatable, drawable, shots)

        # check for collision between player and asteroid
        for asteroid in asteroids:
            if player.is_colliding(asteroid, []):
                if not collision_detected:
                    print("Game Over!")
                    collision_detected = True
                break
        else:
            collision_detected = False # Reset

        # Check for collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.is_colliding(asteroid, []):
                    print("Shot hit an asteroid!")
                    shot.kill()  # Remove the shot
                    asteroid.split()  # Remove the asteroid
                    break

        # Update and draw
        updatable.update(dt)

        screen.fill((0, 0, 0))
        for sprite in drawable:  # Clear screen
            sprite.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
