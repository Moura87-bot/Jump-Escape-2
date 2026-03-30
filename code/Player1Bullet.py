#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Entity import Entity
from code.const import WIN_WIDTH


class Bullet(Entity):
    def __init__(self, name, position, speed=8):
        super().__init__(name, position)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed

        # remove quando sair da tela
        if self.rect.left > WIN_WIDTH:
            self.health = 0