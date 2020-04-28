import numpy as np
import math
import random
import code
from tic_tac_toe import *
from player import *
from minmax import *

# boards and squares are interpreted with the following NUMPAD system:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |

class ultimate_ttt:
    def __init__(self):
        self.board = [tic_tac_toe(i) for i in range(1,10)]
        self.active = True
        self.winner = None
        self.last_move = None
        self.players = [player() for x in range(2)]
        self.players[0].configureMarker(1)
        self.players[1].configureMarker(2)
        self.minmaxAgent = minmax()

    def checkVictory(self, marker):
        g1, g2, g3, g4, g5, g6, g7, g8, g9 = self.board
        # Check Rows
        if (None != g1.winner == g2.winner == g3.winner):
            self.active = False
            self.winner = marker
        elif (None != g4.winner == g5.winner == g6.winner):
            self.active = False
            self.winner = marker
        elif (None != g7.winner == g8.winner == g9.winner):
            self.active = False
            self.winner = marker
        # Check Columns
        elif (None != g1.winner == g4.winner == g7.winner):
            self.active = False
            self.winner = marker
        elif (None != g2.winner == g5.winner == g8.winner):
            self.active = False
            self.winner = marker
        elif (None != g3.winner == g6.winner == g9.winner):
            self.active = False
            self.winner = marker
        # Check Diagonals
        elif (None != g1.winner == g5.winner == g9.winner):
            self.active = False
            self.winner = marker
        elif (None != g3.winner == g5.winner == g7.winner):
            self.active = False
            self.winner = marker

    def draw(self):
        dummy = tic_tac_toe(1)
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
    
    def getPossibleActions(self):
        if self.last_move == None:
            return [x for x in range(11,100)]
        elif self.board[self.last_move-1].active:
            temp = self.board[self.last_move-1].board.flatten()
            return np.argwhere(temp==0).flatten() + (self.last_move * 10) + 1
        else:
            temp = [game for game in self.board if game.active]
            ans =  []
            for game in temp:
                temp = game.board.flatten()
                temp = np.argwhere(temp==0).flatten() + (game.id * 10) + 1
                ans.extend(temp)
            return ans

    def emptyTile(self, move):
        pos = int(move % 10)  # e.g. 9
        game = int((move - pos) / 10)  # e.g. 3
        self.board[game - 1].empty(pos)
        self.board[game - 1].active = True

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

    def nextMoveHelper(self):
        if self.last_move is None or self.board[self.last_move-1].active is False:
            return "anywhere (_ _). For example, 39 will place your marker in the bottom right tile of the top right tic tac toe."
        else:
            switcher = {1: "in the top-left (1_)",
                        2: "in the top-center (2_)",
                        3: "in the top-right (3_)",
                        4: "in the center-left (4_)",
                        5: "in the center (5_)",
                        6: "in the center-right (6_)",
                        7: "in the bottom-left (7_)",
                        8: "in the bottom-center (8_)",
                        9: "in the bottom-right (9_)"}
            return switcher.get(self.last_move)


    def play(self):
        player = 1
        while (self.active):
            print("Player {}, your marker is {}".format(player, tic_tac_toe.map_to_xo(self,player)))
            while True:
                try:
                    move = int(input("Enter your move {}: ".format(self.nextMoveHelper())))
                    break
                except (ValueError):
                    print("Please input a valid int")

            while (self.isValid(move, self.last_move)[0] == False):
                print("Your move is not valid - {}".format(self.isValid(move, self.last_move)[1]))
                move = int(input("Enter your move {}: ".format(self.nextMoveHelper())))
            pos = int(move%10) #e.g. 9
            game = int((move-pos)/10) #e.g. 3
            self.last_move = pos
            self.board[game-1].place(player, pos)
            self.draw()
            if self.checkVictory(player):
                print("Game has been won!")
            chosenTile = self.minmaxAgent.algorithm(self, player*-1, self.getPossibleActions())
            pos = int(chosenTile%10) #e.g. 9
            game = int((chosenTile-pos)/10) #e.g. 3
            self.board[game-1].place(player*-1, pos)
            self.draw()


            player *= -1

    def instantWin(self, currentPlayer, move):
        won = False
        pos = int(move % 10)  # e.g. 9
        game = int((move - pos) / 10)  # e.g. 3
        if self.board[game - 1].active is False:  # small field is already won so don't bother
            return False
        self.board[game - 1].place(currentPlayer, pos)
        self.checkVictory(currentPlayer)
        self.emptyTile(move)
        if self.active is False:  # reverting changes from the previous checkVictory call
            won = True
            self.active = True
            self.winner = None
        return won

    def contrastCompare(self, old, new):
        oldTiles = old.getPossibleActions()
        newTiles = new.getPossibleActions()
        print("we are comparing " + (str(oldTiles)) + " and " + str(newTiles))
        output = []
        for tile in newTiles:
            if tile not in oldTiles:
                output.add(tile)
        return output


    def heuristics(self, currentPlayer):
        center_spots = [51, 52, 53, 54, 55, 56, 57, 58, 59, 15, 25, 35, 45, 65, 75, 85, 95]  # high value tile locations
        corner_boards = [1, 3, 7, 9]  # small tic tac toe boards
        score = 0
        positions = self.allTilesbyPlayer(currentPlayer)
        for play in positions:
            pos = int(play % 10)  # e.g. 9
            game = int((play - pos) / 10)  # e.g. 3
            self.board[game - 1].place(currentPlayer, pos)
            if self.board[game-1].winner == currentPlayer:
                score += 5
                if game-1 in corner_boards:  # if the small game is a corner game, extra points
                    score += 3
                elif game-1 == 5:  # if small game is the center game, even more points
                    score += 10
            self.emptyTile(play)
            if play in center_spots:  # just if the spot itself is valuable
                score += 3
        print("Calculated score for moves " + str(positions) + " is " + str(score))
        return score

    def allTilesbyPlayer(self, player):
        temp = [game for game in self.board]
        ans = []
        for game in temp:
            temp = game.board.flatten()
            temp = np.argwhere(temp == player).flatten() + (game.id * 10) + 1
            ans.extend(temp)
        return ans


