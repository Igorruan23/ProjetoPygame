#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Level import Level
from Code.Menu import Menu
from Code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.Window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def Run(self ):
        while True:
            menu = Menu(self.Window)
            menu_return = menu.Run()
            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]:
                level = Level(self.Window,'Level1',menu_return)
                level_return= level.run()
            else:
                pygame.quit()
                sys.exit()






