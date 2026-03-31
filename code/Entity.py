#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.const import ENTITY_HEALTH


class Entity:  # ✅ FALTAVA ISSO

    _image_cache = {}  # ✅ necessário para o load_image funcionar

    def __init__(self, name, position):
        self.name = name

        # usar o sistema de cache
        self.surf = self.load_image(name)

        self.rect = self.surf.get_rect(topleft=position)
        self.health = ENTITY_HEALTH.get(self.name, 0)
        self.speed = 0

    @classmethod
    def load_image(cls, name):
        if name not in cls._image_cache:
            try:
                cls._image_cache[name] = pygame.image.load(
                    f'./asset/{name}.png'
                ).convert_alpha()
            except:
                # fallback (debug)
                surf = pygame.Surface((20, 20))
                surf.fill((255, 0, 255))
                cls._image_cache[name] = surf

        return cls._image_cache[name]

    def move(self):
        pass