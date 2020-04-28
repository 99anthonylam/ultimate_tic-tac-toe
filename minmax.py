import numpy as np
import math
import random
import copy
from tic_tac_toe import *
from player import *
from ultimate_ttt import *

class minmax():
    def __init__(self, depth = 3):
        self.depth = depth

    def algorithm(self, board, currentPlayer, positions):
        mustBlock = False
        bestScore = -10001
        bestPlay = None
        hValue = -10000

        for tile in positions:
            deepCopy = copy.deepcopy(board)
            print(deepCopy)
            pos = int(tile % 10)  # e.g. 9
            game = int((tile - pos) / 10)  # e.g. 3
            deepCopy.last_move = pos
            deepCopy.board[game - 1].place(currentPlayer, pos)
            hValue = self.recursive(deepCopy, currentPlayer, currentPlayer*-1, 3, -20000, 20000)
            if hValue >= bestScore:
                bestPlay = tile
                bestScore = hValue
        print("The AI would like to play tile " + str(bestPlay))
        return bestPlay


    def recursive(self, board, marker, currentPlayer, depth, a, b):
        alpha = a
        beta = b
        possibleMoves = board.getPossibleActions()
        print(possibleMoves)
        if depth != 0:
            if currentPlayer == marker: #AI seeks to maximize score
                score = -10000  # substitute for INTEGER.MIN_VALUE
                if score != 10000:
                    for i in possibleMoves:
                        print("The current MAX considered index is " + str(i))
                        if board.instantWin(currentPlayer, i):
                            alpha = 10000
                            score = alpha
                            return score
                        else:
                            pos = int(i % 10)  #try out the move
                            game = int((i - pos) / 10)
                            board.last_move = pos
                            board.board[game - 1].place(currentPlayer, pos)
                            score = max(score, self.recursive(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                            if (score > alpha):
                                alpha = score
                            board.emptyTile(i)
                        if (alpha >= beta):
                            break
                return alpha

            else:  #AI seeks to minimize score on opponent's turn
                score = 10000
                if score != -10000:
                    for i in possibleMoves:
                        print("The current MIN considered index is " + str(i))
                        if board.instantWin(currentPlayer, i):
                            beta = -10000
                            score = beta
                            return score
                        else:
                            pos = int(i % 10)  #try out the move
                            game = int((i - pos) / 10)
                            board.last_move = pos
                            board.board[game - 1].place(currentPlayer, pos)
                            score = min(score, self.recursive(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                            if (score < beta):
                                beta = score
                            board.emptyTile(i)
                        if beta <= alpha:
                            break
                return beta
        else:  # depth is zero, time for heuristics
            # usedPositions = board.contrastCompare( board)
            heuristicScore = board.heuristics(marker) - board.heuristics(marker*-1)
            # heuristicScore = board.heuristics(marker)
            return heuristicScore



                            # board.last_move = pos
                            # print("Looking at " + str(game) + str(pos))
                            # board.draw()
                            # board.place()

