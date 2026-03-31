#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.Player1Bullet import Player1Bullet
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name.lower():

            case 'level1bg':
                list_bg = []

                for i in range(2):
                    list_bg.append(Background('Level1Bg0', (i * WIN_WIDTH, 0), 1))

                for i in range(2):
                    list_bg.append(Background('Level1Bg1', (i * WIN_WIDTH, 0), 2))

                for i in range(2):
                    list_bg.append(Background('Level1Bg2', (i * WIN_WIDTH, 0), 3))

                return list_bg

            case 'player1':
                return Player('Player1', (10, WIN_HEIGHT // 2 - 30))

            case 'player2':
                return Player('Player2', (10, WIN_HEIGHT // 2 + 30))

            case 'enemy1':
                return Enemy(
                    'Enemy1',
                    (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT))
                )

            case 'player1bullet':
                print("CRIANDO BALA PLAYER1")
                return Player1Bullet('Player1Bullet', position)

            case 'player2bullet':
                from code.Player2Bullet import Player2Bullet
                return Player2Bullet('Player2Bullet', position)

            case 'enemy1bullet':
                from code.Enemy1Bullet import Enemy1Bullet
                return Enemy1Bullet('Enemy1Bullet', position)

            case _:
                print(f"ERRO: entidade '{entity_name}' não existe!")
                return None