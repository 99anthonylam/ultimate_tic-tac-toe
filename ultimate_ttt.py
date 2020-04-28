import numpy as np
import math
import random
from tic_tac_toe import *
from player import *

# boards and squares are interpreted with the following NUMPAD system:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |

class ultimate_ttt:
    def __init__(self):
        self.board = [tic_tac_toe() for _ in range(9)]
        self.active = True
        self.winner = None
        self.players = [player() for x in range(2)]
        self.players[0].configureMarker(1)
        self.players[1].configureMarker(2)

    def checkVictory(self, marker):
        g1, g2, g3, g4, g5, g6, g7, g8, g9 = self.board
        # Check Rows
        if (marker == g1.winner == g2.winner == g3.winner):
            self.active = False
            self.winner = marker
        elif (marker == g4.winner == g5.winner == g6.winner):
            self.active = False
            self.winner = marker
        elif (marker == g7.winner == g8.winner == g9.winner):
            self.active = False
            self.winner = marker
        # Check Columns
        elif (marker == g1.winner == g4.winner == g7.winner):
            self.active = False
            self.winner = marker
        elif (marker == g2.winner == g5.winner == g8.winner):
            self.active = False
            self.winner = marker
        elif (marker == g3.winner == g6.winner == g9.winner):
            self.active = False
            self.winner = marker
        # Check Diagonals
        elif (marker == g1.winner == g5.winner == g9.winner):
            self.active = False
            self.winner = marker
        elif (marker == g3.winner == g5.winner == g7.winner):
            self.active = False
            self.winner = marker

    def draw(self):
        dummy = tic_tac_toe()
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
    
    def isValid(self, move, last_move):
        pos = int(move%10) 
        game = int((move-pos)/10) 
        if pos < 1 or pos > 9:
            return (False,"Out of bounds")
        if game < 1 or game > 9:
            return (False, "Out of bounds")
        row = int((pos-1)/3)
        col = (pos-1)%3

        if self.board[game-1].active:
            if game != last_move and last_move != None:
                return (False, "Not in correct game")
            if self.board[game-1].board[row][col] != 0:
                return (False, "Spot is taken")
        else:
            return (False, "Game has been won")
        return (True,None)

    def play(self):
        player = 1
        last_move = None
        while (self.active):
            print("Player {}, your marker is {}".format(player, tic_tac_toe.map_to_xo(self,player)))
            move = int(input("Enter your move (e.g. 39 for the bottom right corner of game 3): "))
            while (self.isValid(move, last_move)[0] == False):
                print("Your move is not valid - {}".format(self.isValid(move, last_move)[1]))
                move = int(input("Enter your move (e.g. 39 for the bottom right corner of game 3): "))
            pos = int(move%10) #e.g. 9
            game = int((move-pos)/10) #e.g. 3
            last_move = pos
            self.board[game-1].place(player, pos)
            self.draw()
            if self.checkVictory(player):
                print("Game has been won!")

            player *= -1

game = ultimate_ttt()
game.play()

