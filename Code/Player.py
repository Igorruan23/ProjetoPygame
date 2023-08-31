#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Code.Entity import Entity
from Code.PlayerShot import PlayerShot
from Code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_K_UP, PLAYER_K_DOWN, PLAYER_K_LEFT, PLAYER_K_RIGHT, \
    PLAYER_K_SHOOT, ENTITY_SHOT_DELAY


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def Move(self):
        pressed_key = pygame.key.get_pressed()
        # se a tecla seta para cima for pressionada
        if pressed_key[PLAYER_K_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        # se a tecla seta para cima for pressionada
        if pressed_key[PLAYER_K_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        # se a tecla seta para cima for pressionada
        if pressed_key[PLAYER_K_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        # se a tecla seta para cima for pressionada
        if pressed_key[PLAYER_K_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_K_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery,))
            else:
                return None
        else:
            return None
