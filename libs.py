import random

class Square:
    def __init__(self, x, y, w, h, value):
        self.x, self.y, self.w, self.h = x, y, w, h
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
                for y in range(y, y + h + 1):
                    self.cells[y][x, x + w + 1] = [value for _ in range(w)]
                self.squares.append(square)
                return True
            except ValueError:
                return False
        else:
            return False
    def getAvalablePositions(self, square):
        w, h = square.getSize()
        squares = []
        for y in range(len(self.height - h)):
            for x in range(len(self.width - w)):
                if self.cells[y][x] == self.cells[y + h][x] == self.cells[y][x+w] == self.cells[y+h][x+w] == 0 and not self.hasInterceptionAny(square):
                    squares.append(square)
        return squares
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