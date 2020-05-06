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
        self.minmaxAgent = None
        self.minmaxAgent2 = None

    def checkVictory(self, marker):  # checks if the game has ended
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

        elif self.getPossibleActions() == []:
            # print("No moves left!")
            self.active = False

    def draw(self):  # prints out board in console
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
    
    def getPossibleActions(self):  # self-explanatory, returns an array of possible tiles to play
        if self.last_move == None:
            return [x for x in range(11,100)]
        elif self.board[self.last_move-1].active:
            temp = self.board[self.last_move-1].board.flatten()
            return np.argwhere(temp==0).flatten() + (self.last_move * 10) + 1
        else:
            temp = [game for game in self.board if game.active]
            ans = []
            for game in temp:
                temp = game.board.flatten()
                temp = np.argwhere(temp==0).flatten() + (game.id * 10) + 1
                ans.extend(temp)
            return ans

    def emptyTile(self, move):  # called to remove a marker from a tile during minmax lookahead iterations
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
        if last_move != None and self.board[last_move-1].active == False:
            if self.board[game-1].board[row][col] != 0:
                return (False, "Spot is taken")
            return (True, None)

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


            # comment the following out to remove minMax
            chosenTile = self.minmaxAgent.algorithm(self, player*-1, self.getPossibleActions())
            pos = int(chosenTile%10) #e.g. 9
            game = int((chosenTile-pos)/10) #e.g. 3
            self.last_move = pos
            self.board[game-1].place(player*-1, pos)
            if self.checkVictory(player*-1):
                print("Game has been won!")
            self.draw()


            # player *= -1

    def instantWin(self, currentPlayer):
        self.checkVictory(currentPlayer)
        # print("We are currently looking for player {} and we think that the winner is {}".format(str(currentPlayer),str(self.winner)))
        # print("The board is {}".format(str(not self.active)) )
        return self.winner == currentPlayer

    def heuristics(self, currentPlayer):
        center_spots = [51, 52, 53, 54, 55, 56, 57, 58, 59, 15, 25, 35, 45, 65, 75, 85, 95]  # high value tile locations
        corner_boards = [0, 2, 6, 8]  # small tic tac toe boards
        score = 0
        positions = self.allTilesbyPlayer(currentPlayer)
        # print("Currently looking at player " + str(currentPlayer) + " with positions " + str(positions))
        for int in range(1,10):  # to iterate through the boards
            self.board[int-1].checkVictory()
            if self.board[int-1].winner == currentPlayer:
                score += 10  # points for winning a small board
                if int-1 in corner_boards:  # if the small game is a corner game, extra points
                    score += 4
                elif int-1 == 4:  # if small game is the center game, even more points
                    score += 11
            numberOfDoubles = self.board[int-1].checkDoubles(currentPlayer)  # points for having two out of three tiles for a small board win
            score += numberOfDoubles*2
        for play in positions:
            if play in center_spots:  # just if the spot itself is valuable
                score += 3
                if play == 55:
                    score += 3

        return score

    def allTilesbyPlayer(self, player):
        temp = [game for game in self.board]
        ans = []
        for game in temp:
            temp = game.board.flatten()
            temp = np.argwhere(temp == player).flatten() + (game.id * 10) + 1
            ans.extend(temp)
        return ans

    def twoHumanPlay(self):
        player = 1
        while (self.active):
            print("Player {}, your marker is {}".format(player, tic_tac_toe.map_to_xo(self, player)))
            while True:
                try:
                    move = int(input("Enter your move {}: ".format(self.nextMoveHelper())))
                    break
                except (ValueError):
                    print("Please input a valid int")

            while (self.isValid(move, self.last_move)[0] == False):
                print("Your move is not valid - {}".format(self.isValid(move, self.last_move)[1]))
                move = int(input("Enter your move {}: ".format(self.nextMoveHelper())))
            pos = int(move % 10)  # e.g. 9
            game = int((move - pos) / 10)  # e.g. 3
            self.last_move = pos
            self.board[game - 1].place(player, pos)
            self.draw()
            self.checkVictory(player)
            if self.winner == player:
                print("Game has been won by player {}!".format(player))
            elif self.active == False:
                print("No one won!")
        player *= -1

    def oneHumanPlay(self):
        print("Type 1 to go first, 2 to go second.")
        while True:
            try:
                choice = int(input("Enter your decision: "))
                if choice in [1, 2]:
                    break
            except (ValueError):
                print("Please input a valid int")

        if choice == 1:  # human go first
            player = 1
            while (self.active):
                print("Player {}, your marker is {}".format(player, tic_tac_toe.map_to_xo(self, player)))
                while True:
                    try:
                        move = int(input("Enter your move {}: ".format(self.nextMoveHelper())))
                        break
                    except (ValueError):
                        print("Please input a valid int")

                while (self.isValid(move, self.last_move)[0] == False):
                    print("Your move is not valid - {}".format(self.isValid(move, self.last_move)[1]))
                    move = int(input("Enter your move {}: ".format(self.nextMoveHelper())))
                pos = int(move % 10)  # e.g. 9
                game = int((move - pos) / 10)  # e.g. 3
                self.last_move = pos
                self.board[game - 1].place(player, pos)
                self.draw()
                self.checkVictory(player)
                if self.winner == player:
                    print("Game has been won by the player!")
                elif self.active == False:
                    print("No one won!")

                # comment the following out to remove minMax
                chosenTile = self.minmaxAgent.algorithm(self, player * -1, self.getPossibleActions())
                pos = int(chosenTile % 10)  # e.g. 9
                game = int((chosenTile - pos) / 10)  # e.g. 3
                self.last_move = pos
                self.board[game - 1].place(player * -1, pos)
                self.checkVictory(player * -1)
                if self.winner == (player * -1):
                    print("Game has been won by the AI!")
                elif self.active == False:
                    print("No one won!")
                self.draw()

        else:  # AI go first
            player = -1
            while (self.active):
                chosenTile = self.minmaxAgent.algorithm(self, player * -1, self.getPossibleActions())
                pos = int(chosenTile % 10)  # e.g. 9
                game = int((chosenTile - pos) / 10)  # e.g. 3
                self.last_move = pos
                self.board[game - 1].place(player * -1, pos)
                self.checkVictory(player * -1)
                if self.winner == (player * -1):
                    print("Game has been won by the AI!")
                elif self.active == False:
                    print("No one won!")
                self.draw()


                print("Player {}, your marker is {}".format(player, tic_tac_toe.map_to_xo(self, player)))
                while True:
                    try:
                        move = int(input("Enter your move {}: ".format(self.nextMoveHelper())))
                        break
                    except (ValueError):
                        print("Please input a valid int")

                while (self.isValid(move, self.last_move)[0] == False):
                    print("Your move is not valid - {}".format(self.isValid(move, self.last_move)[1]))
                    move = int(input("Enter your move {}: ".format(self.nextMoveHelper())))
                pos = int(move % 10)  # e.g. 9
                game = int((move - pos) / 10)  # e.g. 3
                self.last_move = pos
                self.board[game - 1].place(player, pos)
                self.draw()
                self.checkVictory(player)
                if self.winner == player:
                    print("Game has been won by the player!")
                    break
                elif self.active == False:
                    print("No one won!")
                    break

    def twoAIPlay(self):
        player = 1
        chosenTile = random.choice(self.getPossibleActions())  # start off with one random choice from both sides
        pos = int(chosenTile % 10)  # e.g. 9
        game = int((chosenTile - pos) / 10)  # e.g. 3
        self.last_move = pos
        self.board[game - 1].place(player, pos)

        chosenTile = random.choice(self.getPossibleActions())
        pos = int(chosenTile % 10)  # e.g. 9
        game = int((chosenTile - pos) / 10)  # e.g. 3
        self.last_move = pos
        self.board[game - 1].place(player * -1, pos)

        while (self.active):
            chosenTile = self.minmaxAgent.algorithm(self, player, self.getPossibleActions())
            pos = int(chosenTile % 10)  # e.g. 9
            game = int((chosenTile - pos) / 10)  # e.g. 3
            self.last_move = pos
            self.board[game - 1].place(player, pos)
            self.checkVictory(player)
            if self.winner == player:
                self.draw()
                print("Game has been won by the first AI!")
                break
            elif self.active == False:
                self.draw()
                print("No one won!")
                break
            # self.draw()

            chosenTile = self.minmaxAgent2.algorithm(self, player * -1, self.getPossibleActions())
            # print(str(chosenTile))
            pos = int(chosenTile % 10)  # e.g. 9
            game = int((chosenTile - pos) / 10)  # e.g. 3
            self.last_move = pos
            self.board[game - 1].place(player * -1, pos)
            self.checkVictory(player * -1)
            if self.winner == (player * -1):
                self.draw()
                print("Game has been won by the second AI!")
                break
            elif self.active == False:
                self.draw()
                print("No one won!")
                break
            # self.draw()

    def setupGame(self):  # called at beginning of main.py for configuration
        choice = None
        difficulty = None
        print("How many players?")
        print("1: Two Human Players")
        print("2: One Human, One AI")
        print("3: Two AI Players")
        while True:  # choosing player types
            try:
                choice = int(input("Enter your choice: "))
                if choice in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice.")
            except (ValueError):
                print("Please input a valid int")

        if choice == 2:  #one AI
            print("What difficulty would you like? Please choose a difficulty setting from 1-3. Three is the most difficult.")
            while True:
                try:
                    difficulty = int(input("Enter your choice: "))
                    if difficulty in [1, 2, 3]:
                        difficulty -= 1  # converts into depth setting
                        self.minmaxAgent = minmax(difficulty)
                        break
                    else:
                        print("Invalid choice.")
                except (ValueError):
                    print("Please input a valid int")

        elif choice == 3:  # two AI
            print("What difficulty would you like? Please type a two-digit number with 1-3 in the tens and ones place. For example, 33 will have the two hardest setting AI playing eachother.")
            while True:  # choosing player types
                try:
                    difficulty = int(input("Enter your choice: "))
                    if difficulty in [11, 12, 13, 21, 22, 23, 31, 32, 33]:
                        self.minmaxAgent = minmax((difficulty // 10) - 1)  # converts the tens place digit to a depth setting
                        self.minmaxAgent2 = minmax((difficulty % 10)  - 1)  # converts the ones place digit to a depth setting
                        break
                    else:
                        print("Invalid choice. Please choose one of " + str([11, 12, 13, 21, 22, 23, 31, 32, 33]))
                except (ValueError):
                    print("Please input a valid int")
        return (choice)

    def quickStart1(self):
        self.minmaxAgent = minmax(2)
        self.minmaxAgent2 = minmax(2)
        self.twoAIPlay()

    def quickStart2(self):
        self.minmaxAgent = minmax(1)
        self.minmaxAgent2 = minmax(2)
        self.twoAIPlay()


