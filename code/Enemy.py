#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = 3

    def move(self):
        # inimigo anda para esquerda
        self.rect.x -= self.speed

        # se sair da tela, volta para direita
        if self.rect.right < 0:
            self.rect.left = 800  # largura da tela (ajuste se quiser)