#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.const import WIN_WIDTH, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position)
        self.speed = speed

    def move(self,):
        self.rect.x -= ENTITY_SPEED[self.name]

        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH