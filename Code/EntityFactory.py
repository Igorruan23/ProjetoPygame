#!/usr/bin/python
#-*- coding: utf-8 -*-
from Code.Background import Background
from Code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case'LVLBG01':
                list_bg=[]
                for i in range (7):
                    list_bg.append(Background(f'LVLBG0{i}', (0,0)))
                    list_bg.append(Background(f'LVLBG0{i}', (WIN_WIDTH, 0)))
                return list_bg

