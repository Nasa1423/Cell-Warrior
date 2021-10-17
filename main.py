import random
import pygame
from libs import *
import sys
import os


class Game:
    def __init__(self, height, width):
        pygame.init()
        window = pygame.display.set_mode((1280, 720)) #окно игры
        pygame.display.set_caption("Cell-Warrior") #название окна --> наша игра
        pygame.draw.rect(window, (0, 0, 0),
                         (20, 20, 520, 520))
        for horizon in range(1, height):
            first = 20 + horizon * (500 // height)
            pygame.draw.line(window, (0, 0, 0),
                             [first, 20],
                             [first, 520], 1)
        for vertical in range(1, width):
            second = 20 + vertical * (500 // width)
            pygame.draw.line(window, (0, 0, 0),
                             [0, second],
                             [520, second], 1)

        self.field = GameField(height, width)
        self.bones = Bones()

        #Отрисовка главного меню
    def turn(self):
        a, b = self.bones.throw()
        #Переотрисовка
test = Game(50, 50)
