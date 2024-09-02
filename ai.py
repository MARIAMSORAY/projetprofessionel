import random

class AI:
    def __init__(self):
        pass

    def make_move(self, board):
        empty_cells = [(i, j) for i in range(5) for j in range(5) if board[i][j] is None]
        if empty_cells:
            row, col = random.choice(empty_cells)
            board[row][col] = 'O'
