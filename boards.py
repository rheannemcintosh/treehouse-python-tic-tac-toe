class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

class TicTacToe(Board):
    def __init__(self, width=3, height=3):
        super().__init__(width, height)