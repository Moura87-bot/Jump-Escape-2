#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import ENTITY_HEALTH

class Entity:
    def __init__(self, name, position):
        self.name = name

        self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)

        # ✔ correto
        self.health = ENTITY_HEALTH.get(self.name, 0)

        self.speed = 0