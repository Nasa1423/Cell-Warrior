import random

# class GameField

class GameField:
    def __init__(self):
        self.height, self.width = 50, 50
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]


class Bones:
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