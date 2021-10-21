import random
import pygame
from libs import *
import sys
from pygame.mouse import *
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
        self.window.fill(BLACK)
        pygame.display.set_caption("Cell-Warrior") #название окна --> наша игра
        pygame.draw.rect(self.window, WHITE, (20, 20, 500, 500))
        self.size = 500 / width
        #print(self.size)
        for horizon in range(1, width):
            first = 20 + horizon * (self.size)
            pygame.draw.line(self.window, BLACK, [first, 20], [first, 520])
            pygame.display.update()
        for vertical in range(1, width):
            second = 20 + vertical * (self.size)
            pygame.draw.line(self.window, BLACK, [0, second], [520, second])
            pygame.display.update()
        field_pos = pygame.Rect(20, 20, 500, 500)
        save_field = self.window.subsurface(field_pos)
        pygame.image.save(save_field, "our_field.jpg")

        self.draw_rect(2, 2, 3, 3, GREEN)
        self.field = GameField(width, width)
        self.bones = Bones()
        self.turn()


        #Отрисовка главного меню
        #Отрисовка прямоугольников
    def draw_rect(self, x0, y0, width, height, color):
        #print(20 + (x0 - 1) * self.size)
        pygame.draw.rect(self.window, color, (21 + (x0 - 1) * self.size, 21 + (y0 - 1) * self.size, width * self.size - 1, height * self.size - 1))
        pygame.display.update()

    #отрисовка поля
    def draw_cell(self, width):
        field = pygame.sprite.Group()
        field.add("our_field.jpg")


    def turn(self):
        a, b = self.bones.throw()
        x, y = 0, 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = get_pos()
                    print(x, y)
                    if 520 > x > 20 and 20 < y < 520:
                        self.window.fill(BLACK)
                        self.draw_cell(30)
                        if pygame.mouse.get_focused():
                            pygame.draw.rect(
                                self.window, GREEN, (x - 10,
                                           y - 10,
                                           20, 20))

                        pygame.display.update()

class Objects(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        field_pos = pygame.Rect(20, 20, 500, 500)
        save_field = self.window.subsurface(field_pos)
        pygame.image.save(save_field, "our_field.jpg")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(player)
        self.image = pygame.transform.scale(self.image, (300, 75))

        startPoint = (100, 500)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (startPoint)
        #Переотрисовка
test = Game(30)
test.turn()
