import math

class State:
    def __init__(self):
        # None for now
        self.board = None
        self.playerNo = None
        self.visitCount = None
        self.winScore = None

    # getAllPossibleStates()

    # randomPlay()

class Node:
    def __init__(self):
        self.state = None
        self.parent = None
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

class UCT:
    def getValUCT(total_visits, win_score, visit):
        if (visit == 0):
            return float("inf")
        else:
            return (win_score/visit) + (1.41 * math.sqrt((math.log(total_visits)/ visit)))
    
    def findBest(node):
        parentVisit = node.state.visitCount
        return max([getValUCT(parentVisit,x.state.winScore, x.state.visitCount) for x in node.getChildArray])


def selectNode(root):
    while (len(root.children) != 0) :
        node = UCT.findBest(root)
    return node

def expandNode(node):
    possibleStates = node.getstate().getAllPossibleStates()
    for state in possibleStates:
        newNode = Node()
        newNode.state = state
        newNode.parent = node
        # newNode.state.playerNo = node.state.opponent
        node.children.append(newNode)

def backPropogation(node, playerNo):
    tempNode = node
    while (tempNode != None):
        tempNode.state.visitCount += 1
        if (tempNode.state.playerNo == playerNo) {
            tempNode.state.winScore + 10
        }
        tempNode = tempNode.parent
