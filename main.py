import random
import pygame
from libs import *
import sys
import os
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

class Game:
    def __init__(self, width):
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720)) #окно игры
        pygame.display.set_caption("Cell-Warrior") #название окна --> наша игра
        pygame.draw.rect(self.window, WHITE, (20, 20, 500, 500))
        self.size = 500 / width
        print(self.size)
        for horizon in range(1, width):
            first = 20 + horizon * (self.size)
            pygame.draw.line(self.window, BLACK, [first, 20], [first, 520], 1)
            pygame.display.update()
        for vertical in range(1, width):
            second = 20 + vertical * (self.size)
            pygame.draw.line(self.window, BLACK, [0, second], [520, second], 1)
            pygame.display.update()
        self.draw_rect(2, 2, 5, 3, GREEN)
        self.field = GameField(width, width)
        self.bones = Bones()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        #Отрисовка главного меню
    def draw_rect(self, x0, y0, width, height, color):
        print(20 + (x0 - 1) * self.size)
        pygame.draw.rect(self.window, color, (21 + (x0 - 1) * self.size, 21 + (y0 - 1) * self.size, width * self.size, height * self.size))
        pygame.display.update()
    def turn(self):
        a, b = self.bones.throw()
        #Переотрисовка
test = Game(30)
