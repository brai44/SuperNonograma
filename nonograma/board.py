import numpy as np

class Tablero:
    def __init__(self, rows, columns):
        self.board = np.zeros((rows, columns), dtype=int)
        self.rows = rows
        self.columns = columns

    def update_cell(self, row, column, val):
        if self.board[row][column]!=4: #Si no te has equivocado
            if self.board[row][column] != val:
                if int(val)==3:
                    self.board[row][column]=0
                else:
                    self.board[row][column] = val
                return True
        return False



    def print_board(self):
        for row in self.board:
            print(row)