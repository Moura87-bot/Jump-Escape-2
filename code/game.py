#!/usr/bin/python
# -*- coding: utf-8 -*-
from turtledemo.clock import jump

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()

            pass
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Close Window
                    pygame.quit()  # end pygame
                    quit()


