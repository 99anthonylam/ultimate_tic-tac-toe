import numpy as np
import random
import math
import code
import copy

class Node:
    def __init__(self):
        self.state = State()
        self.parent = None
        self.children = []

class Tree:
    def __init__(self):
        self.root = Node()

class Board:
    def __init__(self):
        self.boardValues =  np.zeros((3,3)).astype(int)
        self.IN_PROGRESS = -1
        self.DRAW = 0
        self.P1 =1
        self.p2 =2 
    
    def checkStatus(self):
        for row in self.boardValues:
            if row[0]==row[1]==row[2]!=0:
                return row[0]
        
        for i in range(0,3):
            col = self.boardValues[:,i]
            if col[0]==col[1]==col[2]!=0:
                return col[0]

        if self.boardValues[0][0]==self.boardValues[2][2]==self.boardValues[1][1]!=0:
            return self.boardValues[0][0]
    
        if self.boardValues[0][2]==self.boardValues[2][0]==self.boardValues[1][1]!=0:
            return self.boardValues[0][2]
        
        if not np.any(self.boardValues==0):
            return 0

        return -1
    
    def getEmptyPositions(self):
        x = self.boardValues.flatten()
        return np.argwhere(x==0).flatten()+1

class State:
    def __init__(self):
        self.board = Board()
        self.playerNo = None
        self.visitCount = 0
        self.winScore = 0
    
    def getAllPossibleStates(self):
        possibleStates = []
        availPos = self.board.getEmptyPositions()
        for pos in availPos:
            row = int((pos-1)/3)
            col = (pos-1)%3
            tempState = State()
            tempState.board = copy.deepcopy(self.board)
            tempState.playerNo = (3-self.playerNo)
            tempState.board.boardValues[row][col] = self.playerNo
            possibleStates.append(tempState)
        return possibleStates
    
    def randomPlay(self):
        action = random.choice(getAllPossibleStates(self))
        self.board[action-1] = 1

def expandNode(node, opponent):
    possibleStates = node.state.getAllPossibleStates()
    for state in possibleStates:
        newNode = Node()
        newNode.state = state
        newNode.parent = node
        newNode.state.playerNo = opponent
        node.children.append(newNode)

class MCTS:
    def __init__(self):
        self.WIN_SCORE = 10
        self.level = None
        self.opponent = None
    
    def findNextMove(board, playerNo):
        opponent = 3-playerNo
        tree = Tree()
        rootNode = tree.root
        rootNode.state.board = board
        rootNode.state.playerNo = opponent
        i = 0
        while (i < 100):
            promisingNode = selectPromisingNode(rootNode)
            if (promisingNode.state.board.checkStatus() == -1):
                expandNode(promisingNode, opponent)
            nodeToExplore = promisingNode
            if (len(promisingNode.children) >0):
                nodeToExplore = random.choice(promisingNode.children)
            playoutResult = simulateRandomPlayout(nodeToExplore, opponent)
            backPropogation(nodeToExplore, playoutResult)
            i+=1
        
        temp = [UCT.getValUCT(rootNode.state.visitCount,x.state.winScore, x.state.visitCount) for x in rootNode.children]
        winnerNode = rootNode.children[temp.index(max(temp))]

        tree.root = winnerNode
        return winnerNode.state.board

def selectPromisingNode(root):
    test_node = root
    while (len(test_node.children) != 0) :
        test_node = UCT.findBest(test_node)
    return test_node


class UCT:
    def getValUCT(total_visits, win_score, visit):
        if (visit == 0):
            return float("inf")
        else:
            return (win_score/visit) + (1.41 * math.sqrt((math.log(total_visits)/ visit)))
    
    def findBest(node):
        parentVisit = node.state.visitCount
        temp = [UCT.getValUCT(parentVisit,x.state.winScore, x.state.visitCount) for x in node.children]
        return node.children[temp.index(max(temp))]

def backPropogation(node, playerNo):
    tempNode = node
    while (tempNode != None):
        tempNode.state.visitCount += 1
        if (tempNode.state.playerNo == playerNo):
            tempNode.state.winScore += 10
        tempNode = tempNode.parent

def simulateRandomPlayout(node, opponent):
    tempNode = node
    tempState = tempNode.state
    boardStatus = tempState.board.checkStatus
    if (boardStatus == opponent):
        tempNode.parent.state.winScore = 0
        return boardStatus
    while (boardStatus == True):
        tempState.player = 3-tempState.player
        tempState.randomPlay()
        boardStatus = tempState.board.status
    return boardStatus
        
# Sim play

game = Board()
player = game.P1
for i in range(9):
    game = MCTS.findNextMove(game, player)
    print(game.boardValues)
    if (game.checkStatus() != -1):
        print(winStatus)
        break
    player = 3-player
    winStatus = game.checkStatus
