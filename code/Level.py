#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
from typing import List

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTIONS, EVENT_ENEMY


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: List[Entity] = []

        # Fundo (lista)
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        # Player 1
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        # Player 2 (corrigido)
        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, millis=2000)
        # Ordena camadas (parallax)
        self.entity_list.sort(key=lambda ent: ent.speed)

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer.music.load('./asset/Level1.wav')
        pygame.mixer.music.play(-1)

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))


            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            self.level_text(
                text_size=14,
                text=f'{self.name} - timeout: {self.timeout / 1000:.1f}s',
                text_color=COLOR_WHITE,
                text_pos=(10, 5)
            )

            self.level_text(
                text_size=14,
                text=f'fps: {clock.get_fps():.0f}',
                text_color=COLOR_WHITE,
                text_pos=(10, WIN_HEIGHT - 35)
            )

            self.level_text(
                text_size=14,
                text=f'entidades: {len(self.entity_list)}',
                text_color=COLOR_WHITE,
                text_pos=(10, WIN_HEIGHT - 20)
            )

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surface, text_rect)