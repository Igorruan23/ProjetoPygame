#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Code.Entity import Entity
from Code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_K_UP, PLAYER_K_DOWN, PLAYER_K_LEFT, PLAYER_K_RIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def Move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_K_UP[self.name]] and self.rect.top > 0:  # se a tecla seta para cima for pressionada
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_K_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # se a tecla seta para cima for pressionada
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_K_LEFT[self.name]] and self.rect.left > 0:  # se a tecla seta para cima for pressionada
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_K_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # se a tecla seta para cima for pressionada
            self.rect.centerx += ENTITY_SPEED[self.name]
