#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Entity import Entity
from code.const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 6)
        self.last_shot = 0
        self.shoot_delay = 300  # milissegundos

    def move(self):
        keys = pygame.key.get_pressed()

        # 🎮 PLAYER 1 (SETAS + CTRL)
        if self.name == 'Player1':
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

        # 🎮 PLAYER 2 (WASD + SPACE)
        elif self.name == 'Player2':
            if keys[pygame.K_w]:
                self.rect.y -= self.speed
            if keys[pygame.K_s]:
                self.rect.y += self.speed
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
            if keys[pygame.K_d]:
                self.rect.x += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))

    def shoot(self, current_time):
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time

            bullet_pos = (self.rect.right, self.rect.centery)

            from code.EntityFactory import EntityFactory
            return EntityFactory.get_entity('Bullet', bullet_pos)

        return None