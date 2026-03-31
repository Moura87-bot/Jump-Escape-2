#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from typing import List
import pygame

from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.const import EVENT_ENEMY, MENU_OPTIONS


class Level:
    def __init__(self, window, name, game_mode):
        self.score = 0
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



    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer.music.load('./asset/Level1.wav')
        pygame.mixer.music.play(-1)

        font = pygame.font.SysFont(None, 30)



        while True:
            clock.tick(60)
            keys = pygame.key.get_pressed()

            # 🎯 EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    enemy = EntityFactory.get_entity('Enemy1')
                    self.entity_list.append(enemy)

            # 🧠 LÓGICA
            for ent in self.entity_list:
                ent.move()

                # PLAYER ATIRANDO
                if isinstance(ent, Player):

                    if ent.name == 'Player1' and keys[pygame.K_LCTRL]:
                        bullet = ent.shoot(pygame.time.get_ticks())
                        if bullet:
                            self.entity_list.append(bullet)

                    if ent.name == 'Player2' and keys[pygame.K_SPACE]:
                        bullet = ent.shoot(pygame.time.get_ticks())
                        if bullet:
                            self.entity_list.append(bullet)

                # INIMIGO ATIRANDO
                if isinstance(ent, Enemy):
                    bullet = ent.shoot(pygame.time.get_ticks())
                    if bullet:
                        self.entity_list.append(bullet)

            # 💥 COLISÕES + SCORE
            EntityMediator.verify_collision(self.entity_list, self)

            # 🧹 REMOVE MORTOS
            EntityMediator.verify_health(self.entity_list)

            # 🎮 GAME OVER
            players_alive = [ent for ent in self.entity_list if ent.name.startswith('Player')]
            if len(players_alive) == 0:
                print("GAME OVER")
                pygame.mixer.music.stop()
                return self.score

            # 🎨 RENDER
            self.window.fill((0, 0, 0))

            # 1. fundo primeiro
            for ent in self.entity_list:
                if 'Bg' in ent.name:
                    self.window.blit(ent.surf, ent.rect)

            # 2. entidades normais
            for ent in self.entity_list:
                if 'Bg' not in ent.name and 'Bullet' not in ent.name:
                    self.window.blit(ent.surf, ent.rect)

            # 3. balas por cima (IMPORTANTE 🔥)
            for ent in self.entity_list:
                if 'Bullet' in ent.name:
                    self.window.blit(ent.surf, ent.rect)
            # 🧮 SCORE NA TELA
            score_text = font.render(f"SCORE: {self.score}", True, (255, 255, 255))
            self.window.blit(score_text, (10, 10))

            pygame.display.flip()