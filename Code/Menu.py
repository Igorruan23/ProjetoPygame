#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.Window: Surface = window
        self.surf = pygame.image.load('./Assets/Bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def Run(self):
        pygame.mixer_music.load("./Assets/Menu.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.Window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "MOUNTAIN", (0, 200, 150), ((WIN_WIDTH / 2), 70))
            pygame.display.flip()
            pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Italic", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.Window.blit(source=text_surf, dest=text_rect)
