#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Menu import Menu
from Code.const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.Window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def Run(self ):
        while True:
            menu = Menu(self.Window)
            menu.Run()
            pass







