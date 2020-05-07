import numpy as np
import math

class tic_tac_toe:
  def __init__(self, id):
    self.id = id
    self.board = np.zeros((3,3)).astype(int)
    self.active = True
    self.winner = None
  
  def map_to_xo(self,val):
    if val == 0:
      return ' '
    elif val == 1:
      return 'X'
    elif val == -1:
      return 'O'
  
  def checkVictory(self):
    def updateWinner(self,marker):
      self.active = False
      self.winner = marker
    self.active = True
    self.winner = None
    for row in self.board:  # markers: 1 -> X, -1 -> O
      if (sum(row)) == 3:
        updateWinner(self, 1)
      elif sum(row) == -3:
        updateWinner(self, -1)
    
    for i in range(0,3):
      if (sum(self.board[:,i])) == 3:
        updateWinner(self, 1)
      elif (sum(self.board[:,i])) == -3:
        updateWinner(self, -1)

    if (sum(self.board.diagonal())) == 3:
      updateWinner(self, 1)
    elif(sum(self.board.diagonal())) == -3:
      updateWinner(self, -1)
  
    if (sum(np.fliplr(self.board).diagonal())) == 3:
      updateWinner(self, 1)
    elif (sum(np.fliplr(self.board).diagonal())) == -3:
      updateWinner(self, -1)

    if not np.any(self.board==0):
      self.active = False

  def draw(self):
    for i, row in enumerate(self.board):
      row = list(map(self.map_to_xo,row))
      print(" {} | {} | {}".format(row[0],row[1],row[2]))
      if i == 2:
        break
      print("-----------")
    
  def place(self, marker, move):
    row = int((move-1)/3)
    col = (move-1)%3
    self.board[row][col] = marker
    self.checkVictory()

  def empty(self, move):
    row = int((move-1)/3)
    col = (move-1)%3
    self.board[row][col] = 0

  def checkDoubles(self, currentPlayer):
    numOfDoubles = 0
    if currentPlayer == 1:
      for row in self.board:
        if (sum(row)) == 2:
          numOfDoubles += 1

      for i in range(0, 3):
        if (sum(self.board[:, i])) == 2:
          numOfDoubles += 1

      if (sum(self.board.diagonal())) == 2:
        numOfDoubles += 1

      if (sum(np.fliplr(self.board).diagonal())) == 2:
        numOfDoubles += 1

    elif currentPlayer == -1:
      for row in self.board:
        if (sum(row)) == -2:
          numOfDoubles += 1

      for i in range(0, 3):
        if (sum(self.board[:, i])) == -2:
          numOfDoubles += 1

      if (sum(self.board.diagonal())) == -2:
        numOfDoubles += 1

      if (sum(np.fliplr(self.board).diagonal())) == -2:
        numOfDoubles += 1
    return numOfDoubles
