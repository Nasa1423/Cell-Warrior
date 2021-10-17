import random

class Square:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

class GameField: #игровое поле, все, что его касается#
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.squares = []
    def addSquare(self, x, y, w, h, value):

        try:
            for y in range(y, y + h + 1):
                self.cells[y][x, x + w + 1] = [value for _ in range(w)]
            return True
        except ValueError:
            return False
    def hasInterceptionAny(self, square):
        for selSquare in self.squares:
            if
    def hasInterceptionSingle(self):

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