# -*- coding: utf-8 -*-
import random
import pygame
from libs import *
import sys
import math
from pygame.mouse import *
from server import *
import os


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)


class Game:

    def __init__(self, width, online=False, server=False, sock=None):
        """
        Class Game responsible for drawing the field.

        Args:
            width: the number of cells on the playing field.
        """
        self.sock = sock
        self.online = online
        self.server = server
        if online:
            if server == True:
                sock.send(str(width))
            else:
                width = int(sock.recieve())
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720))
        self.window.fill(BLACK)
        pygame.display.set_caption("Cell-Warrior")
        pygame.draw.rect(self.window, WHITE, (20, 20, 500, 500))
        self.size = 500 / width
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
        self.field_our = FieldImage()
        self.rect_dr = pygame.sprite.Group()
        self.rect_dr.add(self.field_our)
        self.game_manager = GameField(width, width)
        self.bones = Bones()
        self.turn_num = 1
        self.summ1 = 0
        self.summ2 = 0
        self.failed = 0
        while self.failed < 2:
            if online == False:
                self.turn()
                self.turn_num = 2 if self.turn_num == 1 else 1
            else:
                if not(server) and self.turn_num == 1:
                    self.turn_2()
                elif server and self.turn_num == 2:
                    self.turn_2()
                elif server and self.turn_num == 1:
                    self.turn()
                elif not(server) and self.turn_num == 2:
                    self.turn()
                self.turn_num = 2 if self.turn_num == 1 else 1

        if self.summ1 > self.summ2:
            print(f"First player is winner! {self.summ1} vs {self.summ2}")
        elif self.summ1 < self.summ2:
            print(f"Second player is winner! {self.summ1} vs {self.summ2}")
        else:
            print("DRAW!")

    def turn(self):
        """
        Function is responsible for calculating the moves of the players.

        Returns:
            None
        """
        a, b = self.bones.throw()
        x, y = 0, 0
        positions = self.game_manager.getAvalablePositions(Square(x, y, a, b, self.turn_num))
        positions = [x.getCoords() for x in positions[0]]
        coordinates = [[((w - x) / 2 + x + 1) * self.size, ((h - y) / 2 + y + 1) * self.size] for x, y, w, h in positions]
        if coordinates == []:
            self.failed += 1
            return
        self.failed = 0
        sel_positions = -1
        self.rect = Rect_drawing(self.size * a, self.size * b, GREEN) if self.turn_num == 1 else Rect_drawing(self.size * a, self.size * b, PINK)
        self.rect_dr.add(self.rect)
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
                            coord_x, coord_y = 500, 500
                            minimum_dist = math.hypot(500, 500)
                            for posit in range(len(coordinates)):
                                if math.hypot(x - coordinates[posit][0], y - coordinates[posit][1]) < minimum_dist:
                                    minimum_dist = math.hypot(x - coordinates[posit][0], y - coordinates[posit][1])
                                    coord_x = coordinates[posit][0]
                                    coord_y = coordinates[posit][1]
                                    sel_positions = posit
                            self.rect.control(coord_x, coord_y)
                            self.rect.update()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.window.fill(BLACK)
                    if pygame.mouse.get_focused():
                        self.game_manager.addSquare(positions[sel_positions][0], positions[sel_positions][1], a, b, self.turn_num)
                        if self.turn_num == 1:
                            if self.online and self.server:
                                self.sock.send("/".join([str(positions[sel_positions][0]), str(positions[sel_positions][1]), str(a), str(b), str(self.turn_num)]))
                            self.summ1 += a * b
                        elif self.turn_num == 2:
                            if self.online and not(self.server):
                                self.sock.send("/".join([str(positions[sel_positions][0]), str(positions[sel_positions][1]), str(a), str(b), str(self.turn_num)]))
                            self.summ2 += a * b
                        return
                self.rect_dr.update()
                self.rect_dr.draw(self.window)
                pygame.display.flip()

    def turn_2(self):
        """
        Move function for remote player.
        Returns:
            None
        """
        posits = self.sock.recieve()
        print(posits)
        posits = list(map(int, posits.split("/")))
        print(posits)
        self.game_manager.addSquare(int(posits[0]), int(posits[1]), int(posits[2]), int(posits[3]), int(posits[4]))
        self.window.fill(BLACK)
        self.rect = Rect_drawing(self.size * posits[2], self.size * posits[3], GREEN) if self.turn_num == 1 else Rect_drawing(
            self.size * posits[2], self.size * posits[3], PINK)
        self.rect.control((posits[0] + 1) * self.size + (posits[2] * self.size) / 2, (posits[1] + 1) * self.size + (posits[3] * self.size) / 2)
        self.rect_dr.add(self.rect)
        self.rect_dr.update()
        self.rect_dr.draw(self.window)
        pygame.display.flip()



class FieldImage(pygame.sprite.Sprite):
    def __init__(self):
        """
        Class FieldImage creates new sprite of field.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("our_field.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = ((20, 520))


class Rect_drawing(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        """
        Class Rect_drawing creates new sprite of rectangle.

        Args:
            width: width of the rectangle.
            height: length of the rectangle.
            color: color of the rectangle.
        """
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

print("Вы хотите играть по сети?")
answer = input()
if answer == "Да":
    print("Вы хотите быть клиентом или сервером? 1 - клиент, 2 - сервер.")
    player = int(input())
    if player == 1:
        sock = Client("localhost", 8911)
        test = Game(25, online=True, sock=sock)
    elif player == 2:
        sock = Server()
        print("Игрок подключился.")
        test = Game(25, online=True, server=True, sock=sock)
else:
    test = Game(25)
