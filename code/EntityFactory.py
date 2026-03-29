#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.const import WIN_WIDTH

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []

                # fundo (lento)
                for i in range(2):
                    list_bg.append(Background('Level1Bg0', (i * WIN_WIDTH, 0), 0))

                # meio
                for i in range(2):
                    list_bg.append(Background('Level1Bg1', (i * WIN_WIDTH, 0), 0))

                # frente
                for i in range(2):
                    list_bg.append(Background('Level1Bg2', (i * WIN_WIDTH, 0), 0))

                return list_bg
