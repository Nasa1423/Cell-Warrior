# -*- coding: utf-8 -*-

import random

class Square:
    """
    Describes single ingame Square

    Args:
        x:  x position of top left corner
        y: y position of top left corner
        w: width of square
        h: height of square
        value: value of self square, defines belonging to the specific player
    """
    def __init__(self, x:int, y:int, w:int, h:int, value:int):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.value = value
    def getCoords(self):
        """
        Get coordinates of self Square

        Returns:
            Top left and bottom right points of self square (x1, y1, x2, y2)
        """
        return (self.x, self.y, self.x + self.w, self.y + self.h)
    def getSize(self):
        """
        Get size of self Square
        Returns:
            Width and height of self square (width, height)
        """
        return (self.w, self.h)

class GameField:
    """
    Main class of the game field, performs all calculations

    Args:
        height: height of field
        width: width of field
    """
    def __init__(self, height:int, width:int):
        self.height, self.width = height, width
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.squares = []
    def addSquare(self, x:int, y:int, w:int, h:int, value:int):
        """
        Creates new square on the GameField

        Args:
            x:  x position of top left corner
            y: y position of top left corner
            w: width of square
            h: height of square
            value: value of self square, defines belonging to the specific player

        Returns:
            True if creation was successfull, False if not
        """
        square = Square(x, y, w, h, value)
        if not self.hasInterceptionAny(square) and self.fittsInField(square):
            try:
                for y in range(y, y + h):
                    self.cells[y][x: x + w] = [value for _ in range(w)]
                self.squares.append(square)
                return True
            except ValueError:
                return False
        else:
            return False
    def getAvalablePositions(self, square:Square):
        """
        Get all positions, in which game can fit selected square

        Args:
            square: Square game should fit

        Returns:
            List of avalable positions
        """
        w, h = square.getSize()
        playerNum = square.value
        squares = [[], []]
        preferredCells = []
        hasField = False
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x] == playerNum and not hasField:
                    hasField = True
                top = self.cells[y-1][x] if y > 0 else -1
                bottom = self.cells[y + 1][x] if y < self.height - 1 else -1
                left = self.cells[y][x-1] if x > 0 else -1
                right = self.cells[y][x + 1] if x < self.width - 1 else -1
                if playerNum in [top, bottom, left, right] and self.cells[y][x] == 0:
                    preferredCells.append((x,y))
        if not hasField:
            squares[0].append(Square(self.width - 1 - w, self.height - 1 - h, w, h, 1))
            squares[1].append(Square(self.width - 1 - h, self.height - 1 - w, w, h, 1))
        else:
            # for x,y in preferredCells:
            #     for iterY in range(y - w, y + w + 1, w * 2):
            #         for iterX in range(x - h, x + h + 1, h * 2):
            #             selSquare = Square(iterX, iterY, w, h, playerNum)
            #             if self.fittsInField(selSquare) and not self.hasInterceptionAny(selSquare):
            #                 squares[0].append(selSquare)
            #     for iterY in range(y - w, y + w + 1, w * 2):
            #         for iterX in range(x - h, x + h + 1, h * 2):
            #             selSquare = Square(iterX, iterY, h, w, playerNum)
            #             if self.fittsInField(selSquare) and not self.hasInterceptionAny(selSquare):
            #                 squares[1].append(selSquare)
            for y in range(self.height - h):
                for x in range(self.width - w):
                    selSquare = Square(x, y, w, h, playerNum)
                    if self.fittsInField(selSquare) and not self.hasInterceptionAny(selSquare):
                        if self.hasNeighbour(selSquare):
                            squares[0].append(selSquare)
                    selSquare = Square(x, y, h, w, playerNum)
                    if self.fittsInField(selSquare) and not self.hasInterceptionAny(selSquare):
                        if self.hasNeighbour(selSquare):
                            squares[1].append(selSquare)
        return squares

    def hasNeighbour(self, square:Square):
        w,h = square.getSize()
        for y in range(square.y, square.y+h+1):
            for x in range(square.x, square.x+w+1):
                if self.cells[y][x] == square.value and not hasField:
                    hasField = True
                top = self.cells[y - 1][x] if y > 0 else -1
                bottom = self.cells[y + 1][x] if y < self.height - 1 else -1
                left = self.cells[y][x - 1] if x > 0 else -1
                right = self.cells[y][x + 1] if x < self.width - 1 else -1
                #print([top, bottom, left, right])
                if square.value in [top, bottom, left, right] and self.cells[y][x] == 0:
                    return True
        return False
    def fittsInField(self, square:Square):
        """
        Calculates if selected square can fit in the GameField by the size

        Args:
            square: Selected square

        Returns:
            Boolean, True if we can, False if we can not
        """
        return square.x >= 0 and square.x + square.w <= self.width - 1 and square.y >= 0 and square.y + square.h <= self.height - 1
    def hasInterceptionAny(self, square:Square):
        """
        Calculates, if selected square intersects with any of placed earlier squares

        Args:
            square: Selected square

        Returns:
            Boolean, True if there are interception, False if not
        """
        for selSquare in self.squares:
            if self.hasInterceptionSingle(square, selSquare):
                return True
        return False
    def hasInterceptionSingle(self, square1:Square, square2:Square):
        """
        Func takes two square and calculates, if they are intercepting between each other or not
        Args:
            square1: first selected square
            square2: second selected square

        Returns:
            Boolean, True if there is interception, False it there is not
        """
        ax1, ay1, ax2, ay2 = square1.getCoords()
        bx1, by1, bx2, by2 = square2.getCoords()

        if max([ax1, ax2]) <= min([bx1, bx2]) or max([ay1, ay2]) <= min([by1, by2]) or min([ay1, ay2]) >= max([by1, by2]):
            return False
        else:
            return True

    def getState(self, x:int, y:int):
        """
        Get state of selected cell (is cell free or was used by one of the players

        Args:
            x: x coordinate of cell
            y: y coordinate of cell

        Returns:
            Cases:
                Integer 0 -> Cell is free,
                Integer not 0 -> Cell is occupied by the player with number of integer,
                None -> Error
        """
        try:
            return self.cells[y][x]
        except:
            return None


class Bones:
    """
    Emulates drop of two game bones, uses as randomizer
    """
    def __init__(self):
        self.boneA = random.randint(1, 6)
        self.boneB = random.randint(1, 6)

    def throw(self):
        """
        Get 2 random numbers (emulates result of throwing two bones)
        Returns:
            A, B -> two random numbers from 1 to 6
        """
        self.boneA, self.boneB = random.randint(1, 6), random.randint(1, 6)
        return self.boneA, self.boneB

# f = GameField(10, 10)
# f.addSquare(6,6,3,3,1)
# #f.addSquare(3,2,4,4,1)
# for el in f.cells:
#     print(el)
#
# print(f.getAvalablePositions(Square(3,2,4,4,1)))