import numpy as np
import math
import random
from tic_tac_toe import *
from player import *
from ultimate_ttt import *

class minmax():
    def __init__(self, depth = 3):
        self.depth = depth

    def recursive(self, board, marker, currentPlayer, depth, a, b):
        alpha = a
        beta = b
        temp = board.last_move
        possibleMoves = board.getPossibleActions()
        print(possibleMoves)
        if depth != 0:
            if currentPlayer == marker: #AI seeks to maximize score
                score = float('-inf')
                if score != float('inf'):
                    for i in possibleMoves:
                        if board.instantWin(currentPlayer, i):
                            alpha = float('inf')
                            score = alpha
                            return score
                        else:
                            pos = int(i % 10)  #try out the move
                            game = int((i - pos) / 10)
                            board[game - 1].place(currentPlayer, pos)
                            value = max(value, minmax(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                            if (value > alpha):
                                alpha = value
                            board.emptyTile(i)
                            # board.last_move = pos
                            # print("Looking at " + str(game) + str(pos))
                            # board.draw()
                            # board.place()

