#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:

            case 'Level1Bg':
                list_bg = []

                # fundo (lento)
                for i in range(2):
                    list_bg.append(Background('Level1Bg0', (i * WIN_WIDTH, 0), 1))

                # meio
                for i in range(2):
                    list_bg.append(Background('Level1Bg1', (i * WIN_WIDTH, 0), 2))

                # frente
                for i in range(2):
                    list_bg.append(Background('Level1Bg2', (i * WIN_WIDTH, 0), 3))

                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT // 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT // 2 + 30))

            case 'Enemy1':
                return Enemy(
                    'Enemy1',
                    (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT))
                )