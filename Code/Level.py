#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window:Surface = window
        self.mode = menu_option #opção do menu
        self.name = name
        self.entity_List: list[Entity] = []
        self.entity_List.extend(EntityFactory.get_entity('LVLBG01'))

    def run(self, ):
        while True:
            for ent in self.entity_List:
                self.window.blit(source=ent.surf,dest=ent.rect)
                ent.Move()
            pygame.display.flip()
        pass

