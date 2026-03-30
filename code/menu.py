#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_GREEN, MENU_OPTIONS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load("./asset/Menu.mp3")
        pygame.mixer.music.play(-1)

        while True:
            self.window.fill((0, 0, 0))
            self.window.blit(self.surf, self.rect)

            # TÍTULO
            self.menu_text(40, "JUMP ESCAPE", COLOR_GREEN, (WIN_WIDTH // 2, 60))

            # OPÇÕES
            y = 120
            for i, opcao in enumerate(MENU_OPTIONS):
                if i == menu_option:
                    cor = COLOR_GREEN
                    tamanho = 25
                else:
                    cor = (0, 255, 0)
                    tamanho = 20

                self.menu_text_shadow(
                    tamanho,
                    opcao,
                    cor,
                    (255, 128, 0),
                    (WIN_WIDTH // 2, y)
                )
                y += 40

            # 🔥 CONTROLES (NOVO)
            self.draw_controls()

            pygame.display.flip()

            # EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTIONS)

                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTIONS)

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]

    # TEXTO NORMAL
    def menu_text(self, size, text, color, pos):
        font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf: Surface = font.render(text, True, color)
        rect: Rect = surf.get_rect(center=pos)
        self.window.blit(surf, rect)

    # TEXTO COM SOMBRA
    def menu_text_shadow(self, size, text, color, shadow_color, pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)

        shadow = font.render(text, True, shadow_color)
        shadow_rect = shadow.get_rect(center=(pos[0] + 2, pos[1] + 2))

        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=pos)

        self.window.blit(shadow, shadow_rect)
        self.window.blit(text_surf, text_rect)

    # 🔥 NOVA FUNÇÃO: CONTROLES
    def draw_controls(self):
        controls = [
            "CONTROLES:",
            "↑ ↓ ← →  - Mover",
            "SPACE     - Atirar",
            "ENTER     - Selecionar",
            "ESC       - Sair"
        ]

        y = WIN_HEIGHT - 180  # posição inferior da tela

        for linha in controls:
            self.menu_text(
                16,
                linha,
                (0, 255, 0),
                (WIN_WIDTH // 6, y)
            )
            y += 10