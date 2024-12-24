import pytest
import pygame

from asteroid import Asteroid

@pytest.fixture
def asteroid():
    return Asteroid(0, 0, 10)


def test_asteroid_split(asteroid):
    asteroid.split()
    assert asteroid.alive() is False


def test_asteroid_update(asteroid):
    asteroid.update(1)
    assert asteroid.position == pygame.Vector2(0, 0)
