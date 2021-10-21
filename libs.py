import random

class Square:
    def __init__(self, x, y, w, h, value):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.value = value
    def getCoords(self):
        return (self.x, self.y, self.x + self.w, self.y + self.h)
    def getSize(self):
        return (self.w, self.h)

class GameField: #игровое поле, все, что его касается#
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.squares = []
    def addSquare(self, x, y, w, h, value):
        square = Square(x, y, w, h, value)
        if not self.hasInterceptionAny(square):
            try:
                for y in range(y, y + h):
                    self.cells[y][x: x + w] = [value for _ in range(w)]
                self.squares.append(square)
                return True
            except ValueError:
                return False
        else:
            return False
    def getAvalablePositions(self, square):
        w, h = square.getSize()
        playerNum = square.value
        squares = []
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
            squares.append(Square(self.width - 1 - w, self.height - 1 - h, self.width-1))
            squares.append(Square(self.width - 1 - h, self.height - 1 - w, self.width-1))
        else:
            for x,y in preferredCells:
                for iterY in range(y - h, y + h + 1, h * 2):
                    for iterX in range(x - w, x + w + 1, w * 2):
                        selSquare = Square(iterX, iterY, iterX + w, iterY + h, playerNum)
                        if self.fittsInField(selSquare) and not self.hasInterceptionAny(selSquare):
                            squares.append(selSquare)
                for iterY in range(y - w, y + w + 1, w * 2):
                    for iterX in range(x - h, x + h + 1, h * 2):
                        selSquare = Square(iterX, iterY, iterX + h, iterY + w, playerNum)
                        if self.fittsInField(selSquare) and not self.hasInterceptionAny(selSquare):
                            squares.append(selSquare)
        return squares
    def fittsInField(self, square):
        return square.x >= 0 and square.x + square.w <= self.width - 1 and square.y >= 0 and square.y + square.h <= self.height - 1
    def hasInterceptionAny(self, square):
        for selSquare in self.squares:
            if self.hasInterceptionSingle(square, selSquare):
                return True
        return False
    def hasInterceptionSingle(self, square1, square2):
        ax1, ay1, ax2, ay2 = square1.getCoords()
        bx1, by1, bx2, by2 = square2.getCoords()

        if max([ax1, ax2]) <= min([bx1, bx2]) or max([ay1, ay2]) <= min([by1, by2]) or min([ay1, ay2]) >= max([by1, by2]):
            return False
        else:
            return True

    def getState(self, x, y):
        try:
            return self.cells[y][x]
        except:
            return None


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

#field = GameField(50, 50)