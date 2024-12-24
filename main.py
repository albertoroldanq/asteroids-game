import sys

import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    AsteroidField()

    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable_group:
            obj.update(dt)

        for obj in asteroids_group:
            for bullet in shot_group:
                if obj.collides_with(bullet):
                    obj.split()
                    bullet.kill()
            if obj.collides_with(player):
                print("Game Over!")
                sys.exit()

        screen.fill("Black")

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
