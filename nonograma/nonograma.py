from board import Tablero

class Nonograma:
    def __init__(self, rows,columns):
        self.tablero_jugador = Tablero(rows,columns)
        self.tablero_solucion = Tablero(rows, columns)

    def verificar_jugada(self,row,column):
        if self.tablero_jugador.board[row][column] == self.tablero_solucion.board[row][column]:
            return True
        else:
            return False

    def hacer_jugada(self, row, column, val):
        #Si se marco correctamente
        if self.tablero_jugador.update_cell(row, column,val):
            if int(val)==2 or int(val)==3:
                return True
            elif self.verificar_jugada(row, column):
                return True
            else:
                self.tablero_jugador.board[row][column]=4
                print("ERROOOOR")
                return False
        else:
            print("Error al actualizar la celda")
            return False