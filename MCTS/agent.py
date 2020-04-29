import numpy as np
import random
import math
import copy
from State import *

# Utility Classes
class Node:
    def __init__(self):
        self.state = State()
        self.parent = None
        self.children = []

class Tree:
    def __init__(self):
        self.root = Node()


class UCT:
    def getValUCT(total_visits, win_score, visit):
        if (visit == 0):
            return float("inf")
        else:
            return (win_score / visit) + (1.41 * math.sqrt((math.log(total_visits) / visit)))

    def findBest(node):
        parentVisit = node.state.visitCount
        temp = [UCT.getValUCT(parentVisit, x.state.winScore, x.state.visitCount) for x in node.children]
        return node.children[temp.index(max(temp))]

# Helper methods

# MCTS on current game (class UTTT) and for player's turn
def findNextMove(board, player):
    # return child node for this particular root with best/highest score, returns root node if no children
    def selectPromisingNode(root):
        def findBest(node):
            def getUCTVal(totalVisits, winScore, visit):
                if (visit == 0):
                    return float("inf")
                else:
                    return (winScore/visit) + (1.41 * math.sqrt((math.log(totalVisits)/ visit)))
            
            temp = [getUCTVal(node.state.visitCount, x.state.winScore, x.state.visitCount) for x in node.children]
            print(temp)
            return node.children[temp.index(max(temp))]

        temp_node = root
        while(len(temp_node.children) != 0):
            temp_node = findBest(temp_node)
        return temp_node

    # add all possible next states (with player's new move) as children nodes
    def expandNode(node, opponent):
        node.state.player = player
        possibleStates = node.state.getAllPossibleStates()
        for state in possibleStates:
            newNode = Node()
            newNode.state = state
            newNode.parent = node
            newNode.state.player = opponent
            node.children.append(newNode)

    def simulateRandomPlayout(node, opponent):
        tempNode = copy.deepcopy(node)
        tempState = tempNode.state
        tempStatus = tempState.game.checkVictory
        if (tempStatus == opponent):
            tempNode.parent.state.winScore = -9999
            return tempStatus
        while (tempStatus == 2):
            tempState.player *= -1
            tempState.randomPlay()
            tempStatus = tempState.game.checkVictory
        return tempStatus
    
    def backPropogation(node, player):
        while (node != None):
            node.state.visitCount += 1
            if (node.state.player == player):
                node.state.winScore += 10000
            node = node.parent
            
    opponent = player * -1
    tree = Tree()
    rootNode = tree.root
    rootNode.state.game = board
    rootNode.state.player = opponent
    i = 0
    while (i < 50):
        # Select phase
        promisingNode = selectPromisingNode(rootNode)
        # Expand phase for active game
        if (promisingNode.state.game.checkVictory() == 2):
            # print("drawing promising node state")
            # promisingNode.state.game.draw()
            # print("end")
            expandNode(promisingNode, opponent)
        # Simulate phase
        nodeToExplore = promisingNode
        if (len(promisingNode.children) > 0):
            nodeToExplore = random.choice(promisingNode.children)
        playoutResult = simulateRandomPlayout(nodeToExplore, opponent)
        # Update phase
        backPropogation(nodeToExplore, playoutResult)
        i+=1
    
    temp = [UCT.getValUCT(rootNode.state.visitCount, x.state.winScore, x.state.visitCount) for x in rootNode.children]
    print(temp)
    winnerNode = rootNode.children[temp.index(max(temp))]

    tree.root = winnerNode
    return winnerNode.state.game
