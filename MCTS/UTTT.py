import numpy as np
import math
import random
import code
from TTT import *

class UTTT:
    def __init__(self):
        self.board = [TTT(i) for i in range(1,10)]
        self.status = 2
        self.last_move = None

    def checkVictory(self):
        g1, g2, g3, g4, g5, g6, g7, g8, g9 = self.board

        # Check rows
        if (None != g1.winner == g2.winner == g3.winner):
            self.status = g1.winner
            return self.status
        elif (None != g4.winner == g5.winner == g6.winner):
            self.status = g4.winner
            return self.status
        elif (None != g7.winner == g8.winner == g9.winner):
            self.status = g7.winner
            return self.status

        # Check columns
        elif (None != g1.winner == g4.winner == g7.winner):
            self.status = g1.winner
            return self.status
        elif (None != g2.winner == g5.winner == g8.winner):
            self.status = g2.winner
            return self.status
        elif (None != g3.winner == g6.winner == g9.winner):
            self.status = g3.winner
            return self.status

        # Check diagonals
        elif (None != g1.winner == g5.winner == g9.winner):
            self.status = g1.winner
            return self.status
        elif (None != g3.winner == g5.winner == g7.winner):
            self.status = g3.winner
            return self.status

        # Still active
        if [game for game in self.board if game.active]:
            self.status = 2
            return 2

        # Check for tie    
        tie_flag = True
        temp = [game for game in self.board if game.active]
        for game in temp:
            if np.any(game.board==0):
                tie_flag = False
        if (tie_flag):
            self.status = 0

        return self.status

    def draw(self):
        dummy = TTT(1)
        g1, g2, g3, g4, g5, g6, g7, g8, g9 = self.board
        for i in range(3):
            t1 = list(map(dummy.map_to_xo, g1.board[i]))
            t2 = list(map(dummy.map_to_xo, g2.board[i]))
            t3 = list(map(dummy.map_to_xo, g3.board[i]))
            print(" {} | {} | {} || {} | {} | {} || {} | {} | {} ".format(t1[0], t1[1], t1[2], t2[0], t2[1], t2[2],t3[0], t3[1], t3[2]))
            if i == 2:
                print("=====================================")
                break
            print("-----------||-----------||-----------")
        for i in range(3):
            t1 = list(map(dummy.map_to_xo, g4.board[i]))
            t2 = list(map(dummy.map_to_xo, g5.board[i]))
            t3 = list(map(dummy.map_to_xo, g6.board[i]))
            print(" {} | {} | {} || {} | {} | {} || {} | {} | {} ".format(t1[0], t1[1], t1[2], t2[0], t2[1], t2[2],t3[0], t3[1], t3[2]))
            if i == 2:
                print("=====================================")
                break
            print("-----------||-----------||-----------")
        for i in range(3):
            t1 = list(map(dummy.map_to_xo, g7.board[i]))
            t2 = list(map(dummy.map_to_xo, g8.board[i]))
            t3 = list(map(dummy.map_to_xo, g9.board[i]))
            print(" {} | {} | {} || {} | {} | {} || {} | {} | {} ".format(t1[0], t1[1], t1[2], t2[0], t2[1], t2[2],t3[0], t3[1], t3[2]))
            if i == 2:
                break
            print("-----------||-----------||-----------")
    
    def isValid(self, move):
        pos = int(move%10) 
        game = int((move-pos)/10) 
        if pos < 1 or pos > 9:
            return (False,"Out of bounds")
        if game < 1 or game > 9:
            return (False, "Out of bounds")
        row = int((pos-1)/3)
        col = (pos-1)%3

        # Last game was won
        if self.last_move != None and not self.board[self.last_move%10-1].active and game != self.last_move//10:
            return (True, None)

        if self.board[game-1].active:
            if self.last_move != None and game != self.last_move%10:
                return (False, "Not in correct game")
            if self.board[game-1].board[row][col] != 0:
                return (False, "Spot is taken")
        else:
            return (False, "Game has been won")
        return (True,None)