import numpy as np
import math

class tic_tac_toe:
  def __init__(self):
    self.board = np.zeros((3, 3))
    self.active = True
    self.winner = None
  
  def map_to_xo(self,val):
    if val == 0:
      return 0
    elif val == 1:
      return 'X'
    elif val == -1:
      return 'O'
  
  def check_won(self, marker):
    for row in self.board:
      if abs(sum(row)) == 3:
        self.active = False
        self.winner = marker
    
    for i in range(0,3):
      if abs(sum(self.board[:,i])) == 3:
        self.active = False
        self.winner = marker

    diag = 0
    anti_diag = 0
    for i in range(0,3):
      diag += self.board[i,i]
      anti_diag += self.board[i,2-i]
    
    if abs(diag) == 3:
      self.active = False
      self.winner = marker
    elif abs(anti_diag) == 3:
      self.active = False
      self.winner = marker
    


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
    self.check_won(marker)
    if not self.active:
      print("Game won by player {}".format(self.winner))


game = tic_tac_toe()
game.place(1,(0,0))
game.place(1,(0,1))
game.place(1,(0,2))
game.draw()

