import pygame

import pygame

# CORES
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

# EVENTOS
EVENT_ENEMY = pygame.USEREVENT + 1

# VELOCIDADE
ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 2,
    'Level1Bg2': 3,
    'Player1': 6,
    'Player2': 6,
    'Player1Bullet': 1,
    'Player2Bullet': 3,
    'Enemy1': 4,
    'Bullet': 10,
}

# VIDA (ESSENCIAL)
ENTITY_HEALTH = {
    'Player1': 100,
    'Player2': 100,
    'Enemy1': 50,
    'Level1Bg0': 9999,
    'Level1Bg1': 9999,
    'Level1Bg2': 9999,
    'player1Bullet': 1,
    'player2Bullet':3,

}

# MENU
MENU_OPTIONS = (
    'NEW GAME 1P - COOPERATIVE',
    'NEW GAME 2P - COOPERATIVE',
    'SCORE',
    'EXIT'
)

# TELA
WIN_WIDTH = 576
WIN_HEIGHT = 324