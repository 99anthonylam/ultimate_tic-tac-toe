from tic_tac_toe import *
from ultimate_ttt import *

if __name__ == "__main__":
    game = ultimate_ttt()
    # print(len(game.boards))

class Node:
    @abstractmethod
    def find_children(self):
        # used to find all possible moves from the current board state
        return set()

    @abstractmethod
    def find_Rchild(self):
        # find random move from current board state

    @abstractmethod
    def is_done(self):
        # returns True if game is done or can't go anywhere from current board state i.e no more children
        return True

class MCTS:
    def __init__(self, weight=1):
        self.wins = 0 # value of the node (# wins from this node)
        self.visits = 0 # number of times visited this node
        self.children = dict() # children of each node
        self.weight = weight

    def choose(self, node):
        # Choose which successor of node to go to. (Next move in game)
        if node.is_done(): # game done so no move can be done
            raise RuntimeError(f"N/A")

        if node not in self.children:
            return node.find_Rchild()

    def find_Rchild(self.board):
        if self.board.terminal:
            return None # game is done so no move can be done
        # [code] go through board
        # [code] make move