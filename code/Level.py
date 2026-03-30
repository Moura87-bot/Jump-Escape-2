#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from typing import List

import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.const import EVENT_ENEMY, MENU_OPTIONS


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: List[Entity] = []

        # fundo
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        # player 1
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        # player 2
        if game_mode == MENU_OPTIONS[1]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENT_ENEMY, 2000)

        self.entity_list.sort(key=lambda ent: ent.speed)

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer.music.load('./asset/Level1.wav')
        pygame.mixer.music.play(-1)
        keys = pygame.key.get_pressed()

        for ent in self.entity_list:
            if isinstance(ent, Player):

                # PLAYER1 atira com CTRL
                if ent.name == 'Player1' and keys[pygame.K_LCTRL]:
                    bullet = ent.shoot(pygame.time.get_ticks())
                    if bullet:
                        self.entity_list.append(bullet)

                # PLAYER2 atira com SPACE
                if ent.name == 'Player2' and keys[pygame.K_SPACE]:
                    bullet = ent.shoot(pygame.time.get_ticks())
                    if bullet:
                        self.entity_list.append(bullet)

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for ent in self.entity_list:
                            if ent.name == 'Player1':
                                bullet = ent.shoot(pygame.time.get_ticks())
                                if bullet:
                                    self.entity_list.append(bullet)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    enemy = EntityFactory.get_entity('Enemy1')
                    self.entity_list.append(enemy)

            # lógica
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # render
            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            pygame.display.flip()