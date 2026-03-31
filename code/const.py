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
    'Enemy1': 1,
    'Player1Bullet': 10,
    'Player2Bullet': 4,
    'Enemy1Bullet': 2,

}

# VIDA (ESSENCIAL)
ENTITY_HEALTH = {
    'Player1': 100,
    'Player2': 100,
    'Enemy1': 50,
    'Level1Bg0': 9999,
    'Level1Bg1': 9999,
    'Level1Bg2': 9999,
    'Player1Bullet': 1,
    'Player2Bullet':1,
    'Enemy1Bullet':1,

}

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'PLAYER2': pygame.K_w}
PLAYER_KEY_DOW = {'Player1': pygame.K_DOWN,
                 'PLAYER2': pygame.K_s},
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'PLAYER2': pygame.K_a},
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'PLAYER2': pygame.K_d},
PLAYER_KEY_SHOOT = {'Player1': pygame.K_UP,
                 'PLAYER2': pygame.K_LCTRL}



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


def WIN():
    return None