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
        self.board = [tic_tac_toe() for x in range(9)]
        self.won = False
        self.players = [player() for x in range(2)]
        self.players[0].configureMarker(1)
        self.players[1].configureMarker(2)

    def checkVictory(self, marker):
        # check horizontals
        if ((self.boards[0].winner.equals(marker) and self.boards[1].winner.equals(marker) and self.boards[
            2].winner.equals(marker))
                or (self.boards[4].winner.equals(marker) and self.boards[5].winner.equals(marker) and self.boards[
                    6].winner.equals(marker))
                or (self.boards[7].winner.equals(marker) and self.boards[8].winner.equals(marker) and self.boards[
                    9].winner.equals(marker))
                # check columns
                or (self.boards[1].winner.equals(marker) and self.boards[4].winner.equals(marker) and self.boards[
                    7].winner.equals(marker))
                or (self.boards[2].winner.equals(marker) and self.boards[5].winner.equals(marker) and self.boards[
                    8].winner.equals(marker))
                or (self.boards[3].winner.equals(marker) and self.boards[6].winner.equals(marker) and self.boards[
                    9].winner.equals(marker))
                # diagonals
                or (self.boards[1].winner.equals(marker) and self.boards[5].winner.equals(marker) and self.boards[
                    9].winner.equals(marker))
                or (self.boards[3].winner.equals(marker) and self.boards[5].winner.equals(marker) and self.boards[
                    7].winner.equals(marker))):
            return True

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
            return False
        if game < 1 or game > 9:
            return False
        row = int((pos-1)/3)
        col = (pos-1)%3
        if self.board[game-1].board[row][col] != 0:
            return False
        if self.board[game-1].active:
            if game != last_move and last_move != None:
                return False
        return True



    def play(self):
        player = 1
        last_move = None
        while (not self.won):
            print("Player {}, your marker is {}".format(player, tic_tac_toe.map_to_xo(self,player)))
            move = int(input("Enter your move (e.g. 39 for the bottom right corner of game 3): "))
            pos = int(move%10) #e.g. 9
            game = int((move-pos)/10) #e.g. 3
            while (self.isValid(move, last_move) == False):
                print("Your move is not valid. Make sure it is between 11 and 99, is in a valid position, and is in the grid as forced by last player")
                move = int(input("Enter your move (e.g. 39 for the bottom right corner of game 3): "))
            last_move = pos
            self.board[game-1].place(player, pos)
            self.draw()
            if self.checkVictory():
                print("Game has been won!")

            if player == 1:
                player = 2
            else:
                player = 1

game = ultimate_ttt()
game.play()

