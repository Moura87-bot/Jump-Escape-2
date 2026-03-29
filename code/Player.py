#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Entity import Entity
from code.const import WIN_WIDTH, WIN_HEIGHT

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = 6
        self.last_shot = 0
        self.shoot_delay = 300  # milissegundos

    def move(self):
        keys = pygame.key.get_pressed()

        # Player 1
        if self.name == 'Player1':
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

        # limites
        self.rect.clamp_ip(pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))

    def shoot(self, current_time):
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time

            # posição da bala (na frente do player)
            bullet_pos = (self.rect.right, self.rect.centery)

            from code.EntityFactory import EntityFactory
            return EntityFactory.get_entity('Bullet', bullet_pos)

        return None