import random

class GameField: #игровое поле, все, что его касается#
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]
    def setSquare(self, x0, y0, w, h, value):
        try:
            for y in range(y0, y0 + h + 1):
                self.cells[y][x0, x0 + w + 1] = [value for _ in range(w)]
            return True
        except ValueError:
            return False


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