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

    def algorithm(self, board, currentPlayer, positions):
        mustBlock = False
        bestScore = -10001
        bestPlay = None
        global wValue
        wValue = -10000
        for tile in positions:
            deepCopy = copy.deepcopy(board)
            pos = int(tile % 10)  # e.g. 9
            game = int((tile - pos) / 10)  # e.g. 3
            deepCopy.last_move = pos
            print("What if we played here at {}? haha just kidding unless?".format(tile))
            deepCopy.board[game - 1].place(currentPlayer, pos)
            deepCopy.draw()
            if deepCopy.instantWin(currentPlayer, tile):
                return tile
            # elif mustBlock:
                # bestPlay = self.blockLocation
                # break
            wValue = self.recursive(deepCopy, currentPlayer, currentPlayer*-1, 0, -20000, 20000)
            print("the wValue of putting a tile at " + str(tile) + " is " + str(wValue))
            if wValue == -10000:
                mustBlock = True
            if wValue >= bestScore:
                print("********************************")
                print("Tile " + str(tile) + " offers " + str(wValue))
                bestPlay = tile
                bestScore = wValue
        print("The AI would like to play tile " + str(bestPlay) + " which has a best score of " + str(bestScore))
        return bestPlay


    def recursive(self, board, marker, currentPlayer, depth, a, b):
        print("Drawing as we enter the recursion")
        board.draw()
        alpha = a
        beta = b
        possibleMoves = board.getPossibleActions()
        # print(possibleMoves)
        if depth != 0:
            if currentPlayer == marker: #AI seeks to maximize score
                print("we're playing for ourselves now")
                print(possibleMoves)
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
                            print("how can we play off this?")
                            board.draw()
                            score = max(score, self.recursive(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                            if (score > alpha):
                                alpha = score
                            board.emptyTile(i)
                        if (alpha >= beta):
                            print("we're gonna break because {} is bigger than {}".format(alpha, beta))
                            break
                return alpha

            else:  #AI seeks to minimize score on opponent's turn
                score = 10000
                if score != -10000:
                    for i in possibleMoves:
                        # print(possibleMoves)
                        print("The current MIN considered index is " + str(i))
                        if board.instantWin(currentPlayer, i):
                            beta = -10000
                            score = beta
                            self.blockLocation = i
                            print("we have a code blue threat at position {}".format(i))
                            return score
                        else:
                            pos = int(i % 10)  #try out the move
                            game = int((i - pos) / 10)
                            board.last_move = pos
                            board.board[game - 1].place(currentPlayer, pos)
                            print("so we're gonna try putting down the opponent's marker at tile {}".format(i))
                            board.draw()

                            score = min(score, self.recursive(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                            if (score < beta):
                                beta = score
                            board.emptyTile(i)
                            print("What it looks like after emptying a tile")
                            board.draw()
                        if beta <= alpha:
                            break
                return beta
        else:  # depth is zero, time for heuristics
            # usedPositions = board.contrastCompare( board)
            print("positive score: " + str(board.heuristics(marker)) + " negative score from " + str(marker*-1) + ": " + str(board.heuristics(marker*-1)))
            heuristicScore = board.heuristics(marker) - board.heuristics(marker*-1)
            # heuristicScore = board.heuristics(marker)
            return heuristicScore



                            # board.last_move = pos
                            # print("Looking at " + str(game) + str(pos))
                            # board.draw()
                            # board.place()

