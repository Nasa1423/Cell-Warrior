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

class GameField: #игровое поле, все, что его касается#
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]


class Bones:#кости
    def __init__(self):
        self.boneA = random.randint(1, 6)
        self.boneB = random.randint(1, 6)

    # method throw
    #return:
    #   self.boneA : Integer => Value of the first dropped bone
    #   self.boneB : Integer => Value of the second dropped bone
    def throw(self):
        self.boneA, self.boneB = random.randint(1, 6), random.randint(1, 6)
        return self.boneA, self.boneB