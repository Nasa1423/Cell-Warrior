class GameField:
    def __init__(self):
        height, width = 50, 50
        cells = [[0 for _ in range(width)] for _ in range(height)]