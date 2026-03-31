#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Entity import Entity
from code.const import ENTITY_SPEED


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 3)

        # 🔫 controle de tiro
        self.last_shot = 0
        self.shoot_delay = 1200  # milissegundos

    def move(self):
        self.rect.x -= self.speed

    def shoot(self, current_time):
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time
            print("ATIROU")


            bullet_pos = (self.rect.left, self.rect.centery)

            from code.EntityFactory import EntityFactory
            return EntityFactory.get_entity('Enemy1Bullet', bullet_pos)


        return None