#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY


class Level:
    # criação do level
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.mode = menu_option  # opção do menu
        self.name = name
        self.entity_List: list[Entity] = []
        self.entity_List.extend(EntityFactory.get_entity('LVLBG01'))
        if menu_option == MENU_OPTION[0]:
            self.entity_List.append(EntityFactory.get_entity('Player1'))
        elif menu_option == MENU_OPTION[1] or MENU_OPTION[2]:
            self.entity_List.append(EntityFactory.get_entity('Player1'))
            self.entity_List.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self):
        pygame.mixer_music.load(f"./Assets/{self.name}.wav")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_List:
                self.window.blit(source=ent.surf, dest=ent.rect)  # desenho de entidades
                #self.level_text(20, f'fps:{clock.get_fps():.0f}', COLOR_WHITE, (10, 10))
                ent.Move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_List.append(EntityFactory.get_entity(choice))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Italic", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
