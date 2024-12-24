import pytest
import pygame

from asteroid import Asteroid

@pytest.fixture
def asteroid_fixture():
    return Asteroid(0, 0, 10)


def test_asteroid_split(asteroid_fixture):
    asteroid_fixture.split()
    assert asteroid_fixture.alive() is False


def test_asteroid_update(asteroid_fixture):
    asteroid_fixture.update(1)
    assert asteroid_fixture.position == pygame.Vector2(0, 0)
