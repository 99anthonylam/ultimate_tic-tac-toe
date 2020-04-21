import numpy as np
import math

class tic_tac_toe:
  def __init__(self):
    self.board = np.zeros((3, 3))
  
  def map_to_xo(self,val):
    if val == 0:
      return 0
    elif val == 1:
      return 'X'
    elif val == -1:
      return 'O'

  def draw(self):
    for i, row in enumerate(self.board):
      row = list(map(self.map_to_xo,row))
      print(" {} | {} | {}".format(row[0],row[1],row[2]))
      if i == 2:
        break
      print("-----------")
    
  def place(self, marker, move):
    row, col = move
    self.board[row][col] = marker

game = tic_tac_toe()
game.place(1,(2,2))
game.draw()