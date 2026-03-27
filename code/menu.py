#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_RED, COLOR_GREEN, MENU_OPTIONS


class Menu:
	def __init__(self, window):
		self.window = window
		self.surf = pygame.image.load('./asset/MenuBg.png')
		self.rect = self.surf.get_rect(left=0, top=0)

	def run(self):
		pygame.mixer_music.load("./asset/Menu.mp3")
		pygame.mixer.music.play(-1)

		while True:
			self.window.blit(source=self.surf, dest=self.rect)


			self.menu_text(
				text_size=40,
				text="JUMP ESCAPE",
				text_color= COLOR_GREEN,
				text_center_pos=(WIN_WIDTH // 2, 100)

			)
			opcoes = [
				"NEW GAME 1P - COOPERATIVE",
				"NEW GAME P - COOPERATIVE",
				"SCORE",
				"EXIT"
			]

			y = 160

			for opcao in opcoes:
				self.menu_text_shadow(
					20,
					opcao,
					(255, 128, 0),
					(0, 0, 0),
					(WIN_WIDTH // 2, y)
				)
				y += 40  # espaço entre linhas


			pygame.display.flip()


			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()


	def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
		text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
		text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
		text_rect: Rect = text_surf.get_rect(center=text_center_pos)
		self.window.blit(text_surf, text_rect)

	def menu_text_shadow(self, text_size, text, color, shadow_color, pos):
		font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)


		shadow_surf = font.render(text, True, shadow_color)
		shadow_rect = shadow_surf.get_rect(center=(pos[0] + 2, pos[1] + 2))


		text_surf = font.render(text, True, color)
		text_rect = text_surf.get_rect(center=pos)

		self.window.blit(shadow_surf, shadow_rect)
		self.window.blit(text_surf, text_rect)