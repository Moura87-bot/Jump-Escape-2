#!/usr/bin/python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.menu import Menu
from code.Level import Level  # ✔ import correto da classe


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            # ▶ iniciar jogo
            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(self.window, "level1", menu_return)
                level.run()

            # ❌ sair do jogo
            elif menu_return == MENU_OPTIONS[3]:
                pygame.quit()
                quit()