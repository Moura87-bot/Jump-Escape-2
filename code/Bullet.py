import pygame
from code.Entity import Entity
from code.const import ENTITY_SPEED

class Bullet(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # Bala indo para a direita
        self.rect.centerx += ENTITY_SPEED[self.name]