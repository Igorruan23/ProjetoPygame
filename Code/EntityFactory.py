#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.Background import Background
from Code.Enemy import Enemy
from Code.Player import Player
from Code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'LVLBG01':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'LVLBG0{i}', (0, 0)))
                    list_bg.append(Background(f'LVLBG0{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 5, random.randint(0 - 50, WIN_HEIGHT)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 5, random.randint(0 - 50, WIN_HEIGHT)))
