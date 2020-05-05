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
        self.blockLocation = None

    def algorithm(self, board, marker, positions):
        mustBlock = False
        bestScore = -99999
        bestPlay = None
        global wValue
        wValue = -99999
        for tile in positions:
            deepCopy = copy.deepcopy(board)
            pos = int(tile % 10)  # e.g. 9
            game = int((tile - pos) / 10)  # e.g. 3
            deepCopy.last_move = pos
            # print("What if we played here at {}? haha just kidding unless?".format(tile))
            deepCopy.board[game - 1].place(marker, pos)
            if deepCopy.instantWin(marker):
                # print("detecting instant win potential")
                return tile
            # deepCopy.draw()
            wValue = self.recursive(deepCopy, marker, marker*-1, self.depth, -20000, 20000)
            # print("the wValue of putting a tile at " + str(tile) + " is " + str(wValue))
            # print(board.getPossibleActions())
            if wValue >= bestScore:
                # print("********************************")
                # print("Tile " + str(tile) + " offers " + str(wValue))
                bestPlay = tile
                bestScore = wValue
        # print("The AI of " + str(marker) + " would like to play tile " + str(bestPlay) + " which has a best score of " + str(bestScore))
        return bestPlay


    def recursive(self, board, marker, currentPlayer, depth, a, b):
        alpha = a
        beta = b
        possibleMoves = board.getPossibleActions()
        # print(possibleMoves)
        if depth != 0:
            if currentPlayer == marker: #AI seeks to maximize score
                # print("we're playing for ourselves now")
                # print(possibleMoves)
                score = -10000  # substitute for INTEGER.MIN_VALUE
                if score != 10000:
                    for i in possibleMoves:
                        # print("Considering I use tile " + str(i))
                        pos = int(i % 10)  #try out the move
                        game = int((i - pos) / 10)
                        board.last_move = pos
                        board.board[game - 1].place(currentPlayer, pos)
                        # print("we try to put down tile " + str(i))
                        # board.draw()
                        if board.instantWin(currentPlayer):
                            # print("Detecting a friendly instant win")
                            alpha = 10000
                            score = alpha
                            return score
                        score = max(score, self.recursive(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                        if (score > alpha):
                            alpha = score
                        board.emptyTile(i)
                        if (alpha > beta):
                            # print("we're gonna break because {} is bigger than {}".format(alpha, beta))
                            break
                return alpha

            else:  #AI seeks to minimize score on opponent's turn
                score = 10000
                if score != -10000:
                    for i in possibleMoves:
                        # print(possibleMoves)
                        # print("Considering the enemy uses tile " + str(i))
                        pos = int(i % 10)  #try out the move
                        game = int((i - pos) / 10)
                        board.last_move = pos
                        board.board[game - 1].place(currentPlayer, pos)
                        # print("so we're gonna try putting down the opponent's marker at tile {}".format(i))
                        # board.draw()
                        if board.instantWin(currentPlayer):
                            beta = -10000
                            score = beta
                            # print("we have a code blue threat at position {}".format(i))
                            return score
                        score = min(score, self.recursive(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                        if (score < beta):
                            beta = score
                        board.emptyTile(i)
                        # print("What it looks like after emptying a tile")
                        # board.draw()
                        if beta < alpha:
                            break
                return beta
        else:  # depth is zero, time for heuristics
            # usedPositions = board.contrastCompare( board)
            # print("positive score: " + str(board.heuristics(marker)) + " negative score from " + str(marker*-1) + ": " + str(board.heuristics(marker*-1)))
            heuristicScore = board.heuristics(marker) - board.heuristics(marker*-1)
            # heuristicScore = board.heuristics(marker)
            return heuristicScore



                            # board.last_move = pos
                            # print("Looking at " + str(game) + str(pos))
                            # board.draw()
                            # board.place()

