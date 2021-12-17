# -*- coding: utf-8 -*-
import random
import pygame
from libs import *
import sys
import math
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
    """
    Class Game responsible for drawing the field.
    """

    def __init__(self, width):
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720))
        self.window.fill(BLACK)
        pygame.display.set_caption("Cell-Warrior")
        pygame.draw.rect(self.window, WHITE, (20, 20, 500, 500))
        self.size = 500 / width
        # print(self.size)
        for horizon in range(1, width):
            first = 20 + horizon * (self.size)
            pygame.draw.line(self.window, BLACK, [first, 20], [first, 520])
        for vertical in range(1, width):
            second = 20 + vertical * (self.size)
            pygame.draw.line(self.window, BLACK, [0, second], [520, second])
        pygame.display.update()
        field_pos = pygame.Rect(20, 20, 500, 500)
        self.fieldImageSave = self.window.subsurface(field_pos)
        pygame.image.save(self.fieldImageSave, "our_field.jpg")
        self.field_our = FieldImage(self.fieldImageSave)
        self.rect_dr = pygame.sprite.Group()
        self.rect_dr.add(self.field_our)
        self.game_manager = GameField(width, width)
        self.bones = Bones()
        while True:
            self.turn()

    def turn(self):
        """
        Function is responsible for drawing the rectangle.

        Returns:
            None
        """
        a, b = self.bones.throw()
        x, y = 0, 0
        positions = self.game_manager.getAvalablePositions(Square(x, y, a, b, 1))
        positions = [x.getCoords() for x in positions[0]]
        coordinates = [[((w - x) / 2 + x + 2) * self.size, ((h - y) / 2 + y + 2) * self.size] for x, y, w, h in positions]
        sel_positions = -1
        print(positions)
        self.rect = Rect_drawing(self.size * a, self.size * b, GREEN)
        self.rect_dr.add(self.rect)
        print(type(self.rect))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.window.fill(BLACK)
                    x, y = get_pos()
                    if 520 - 15 > x > 20 + 15 and 20 + 15 < y < 520 - 15:
                        self.window.fill(BLACK)
                        if pygame.mouse.get_focused():
                            massive = []
                            coord_x, coord_y = 500, 500
                            minimum_dist = math.hypot(500, 500)
                            # print(minimum_dist)
                            for posit in range(len(coordinates)):
                                if math.hypot(x - coordinates[posit][0], y - coordinates[posit][1]) < minimum_dist:
                                    minimum_dist = math.hypot(x - coordinates[posit][0], y - coordinates[posit][1])
                                    # print(minimum_dist)
                                    coord_x = coordinates[posit][0]
                                    coord_y = coordinates[posit][1]
                                    sel_positions = posit
                            self.rect.control(coord_x, coord_y)
                            self.rect.update()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 520 > x > 20 and 20 < y < 520:
                        self.window.fill(BLACK)
                        if pygame.mouse.get_focused():
                            f = self.game_manager.addSquare(positions[sel_positions][0], positions[sel_positions][1], a, b, 1)
                            print(f)
                            return
                            # pygame.draw.rect(self.window, GREEN, (x - 10, y - 10, 20, 20))
                self.rect_dr.update()
                self.rect_dr.draw(self.window)
                pygame.display.flip()


class FieldImage(pygame.sprite.Sprite):
    """
    Class FieldImage creates new sprite of field.
    """

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        # field_pos = pygame.Rect(20, 20, 500, 500)
        # self.image = image
        self.image = pygame.image.load("our_field.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = ((20, 520))
        # self.image = pygame.image.load("our_field.jpg").convert_alpha()


class Rect_drawing(pygame.sprite.Sprite):
    """
    Class Rect_drawing creates new sprite of rect.
    """

    def __init__(self, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.movex = 0
        self.movey = 0
        self.control(600, 400)
        self.update()

    def control(self, x, y):
        """
        Def control creates a sprite by coordinates.

        Args:
            x: coordination of X-axis
            y: coordination of Y-axis

        Returns:
            None
        """
        self.movex = x
        self.movey = y

    def update(self):
        """
        Def update creates a center at the specified coordinates.

        Returns:
            None
        """
        self.rect.center = (self.movex, self.movey)


test = Game(25)
# test.turn()
