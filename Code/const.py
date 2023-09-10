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
                'Player1Shot': 4,
                'Player2Shot': 3,
                'Enemy1': 2,
                'Enemy2': 1,
                'Enemy1Shot': 6,
                'Enemy2Shot': 8
                }

ENTITY_HEALTH = {'LVLBG00': 999,
                 'LVLBG01': 999,
                 'LVLBG02': 999,
                 'LVLBG03': 999,
                 'LVLBG04': 999,
                 'LVLBG05': 999,
                 'LVLBG06': 999,
                 'Player1': 200,
                 'Player2': 200,
                 'Player1Shot': 1,
                 'Player2Shot': 1,
                 'Enemy1': 50,
                 'Enemy2': 40,
                 'Enemy1Shot': 1,
                 'Enemy2Shot': 1}

ENTITY_DAMAGE = {'LVLBG00': 0,
                 'LVLBG01': 0,
                 'LVLBG02': 0,
                 'LVLBG03': 0,
                 'LVLBG04': 0,
                 'LVLBG05': 0,
                 'LVLBG06': 0,
                 'Player1': 1,
                 'Player2': 1,
                 'Player1Shot': 25,
                 'Player2Shot': 20,
                 'Enemy1': 1,
                 'Enemy2': 1,
                 'Enemy1Shot': 20,
                 'Enemy2Shot': 20}

ENTITY_SCORE = {'LVLBG00': 0,
                 'LVLBG01': 0,
                 'LVLBG02': 0,
                 'LVLBG03': 0,
                 'LVLBG04': 0,
                 'LVLBG05': 0,
                 'LVLBG06': 0,
                 'Player1': 0,
                 'Player2': 0,
                 'Player1Shot': 0,
                 'Player2Shot': 0,
                 'Enemy1': 100,
                 'Enemy2': 110,
                 'Enemy1Shot': 0,
                 'Enemy2Shot': 0}

# intervalo de criação de tiro
ENTITY_SHOT_DELAY = {'Player1': 30,
                     'Player2': 20,
                     'Enemy1': 100,
                     'Enemy2': 100
                     }

EVENT_ENEMY = pygame.USEREVENT + 1

# P
PLAYER_K_UP = {'Player2': pygame.K_UP,
               'Player1': pygame.K_w}
PLAYER_K_DOWN = {'Player2': pygame.K_DOWN,
                 'Player1': pygame.K_s}
PLAYER_K_LEFT = {'Player2': pygame.K_LEFT,
                 'Player1': pygame.K_a}
PLAYER_K_RIGHT = {'Player2': pygame.K_RIGHT,
                  'Player1': pygame.K_d}

PLAYER_K_SHOOT = {'Player1': pygame.K_LCTRL,
                  'Player2': pygame.K_RCTRL}
