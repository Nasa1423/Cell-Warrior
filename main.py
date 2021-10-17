import random
import pygame
import sys
import os
pygame.init()

class Game:
    def __init__(self, height, width):
        window = pygame.display.set_mode((1280, 720)) #окно игры
        pygame.display.set_caption("Cell-Warrior") #название окна --> наша игра
        self.field = GameField(height, width)
        self.bones = Bones()
        #Отрисовка главного меню
    def turn(self):
        a, b = self.bones.throw()
        #Переотрисовка