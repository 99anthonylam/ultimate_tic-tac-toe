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
                        # else:

