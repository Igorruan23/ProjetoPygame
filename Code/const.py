# C
import pygame

COLOR_GAME = (0, 200, 150)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOP',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
ENTITY_SPEED = {'LVLBG00': 0,
                'LVLBG01': 1,
                'LVLBG02': 2,
                'LVLBG03': 3,
                'LVLBG04': 4,
                'LVLBG05': 5,
                'LVLBG06': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 2,
                'Enemy2': 1}

EVENT_ENEMY = pygame.USEREVENT + 1


# P
PLAYER_K_UP = {'Player1': pygame.K_UP,
               'Player2': pygame.K_w}
PLAYER_K_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_K_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_K_RIGHT = {'Player1': pygame.K_RIGHT,
                  'Player2': pygame.K_d}
