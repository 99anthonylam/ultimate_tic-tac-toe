from UTTT import *
import copy
import random

class State:
    def __init__(self):
        self.game = UTTT()
        self.player = 1
        self.visitCount = 0
        self.winScore = 0
    
    def getAllPossibleStates(self):
        # New game
        if self.game.last_move is None:
            availPos = [x for x in range(11,100)]
        
        # Active game
        elif self.game.board[(self.game.last_move % 10) -1].active:
            temp = self.game.board[(self.game.last_move % 10) -1].board.flatten()
            availPos = np.argwhere(temp==0).flatten() + ((self.game.last_move % 10) * 10) + 1

        # Active game, TTT just won
        else:
            temp = [x for x in self.game.board if x.active]
            availPos = []
            for x in temp:
                temp = x.board.flatten()
                temp = np.argwhere(temp==0).flatten() + (x.id * 10) + 1
                availPos.extend(temp)

        # Generate states
        possibleStates = []
        for pos in availPos:
            cell = int(pos % 10)
            grid = int((pos - cell) / 10)
            # row, col = int((cell-1)/3), (cell-1)%3
            tempState = State()
            tempState.game = copy.deepcopy(self.game)
            tempState.player = self.player * -1
            tempState.game.board[grid-1].place(self.player, cell)
            tempState.game.last_move = pos
            possibleStates.append(tempState)
        return possibleStates
    
    def randomPlay(self):
        action = random.choice(self.getAllPossibleStates()).game.last_move
        cell = int(action % 10)
        grid = int((action - cell) / 10)
        self.game.board[grid-1].place(self.player, grid)