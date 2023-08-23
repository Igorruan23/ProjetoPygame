#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.const import WIN_WIDTH, COLOR_GAME, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.Window: Surface = window
        self.surf = pygame.image.load('./Assets/Bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def Run(self):
        pygame.mixer_music.load("./Assets/Menu.mp3")
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            #desenhar na tela
            self.Window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Space", COLOR_GAME, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_GAME, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH/2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            #verificação de eventos
            for event in pygame.event.get():
                #evento para fechar o pygame
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type ==pygame.KEYDOWN: #testar tecla pressionada
                    if event.key ==pygame.K_DOWN: #tecla pressionada:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key ==pygame.K_UP: #tecla pressionada:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]






    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Italic", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.Window.blit(source=text_surf, dest=text_rect)
