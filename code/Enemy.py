#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity
from code.const import ENTITY_SPEED


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 3)

    def move(self):
        self.rect.x -= self.speed