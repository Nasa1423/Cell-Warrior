import random

class GameField:
    def __init__(self):
        self.height, self.width = 50, 50
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]


class Bones:
    def __init__(self):
        self.boneA = random.randint(1, 6)
        self.boneB = random.randint(1, 6)
    def throw(self):
        self.boneA, self.boneB = random.randint(1, 6), random.randint(1, 6)
        return self.boneA, self.boneB