from tic_tac_toe import *
from ultimate_ttt import *
# public class Node {
#     Node parent:
#     List<Node> children
# }

if __name__ == "__main__":
    game = ultimate_ttt()
    # game.draw()
    # game.draw2()
    game.play()
    # print(len(game.boards))

# class Node:
#     @abstractmethod
#     def find_children(self):
#         # used to find all possible moves from the current board state
#         return set()
#
#     @abstractmethod
#     def find_Rchild(self):
#         # find random move from current board state
#
#     @abstractmethod
#     def is_done(self):
#         # returns True if game is done or can't go anywhere from current board state i.e no more children
#         return True
#
# class MCTS:
#     def __init__(self, weight=1):
#         self.wins = 0 # value of the node (# wins from this node)
#         self.visits = 0 # number of times visited this node
#         self.children = dict() # children of each node
#         self.weight = 1
#
#     def choose(self, node):
#         # Choose which successor of node to go to. (Next move in game)
#         if node.is_done(): # game done so no move can be done
#             raise RuntimeError(f"N/A")
#
#         if node not in self.children:
#             return node.find_Rchild()
#
#         return max(self.children[node], key=score)
#
#     def value(n): # calculates value of the node
#         if self.visits(n) == 0:
#             return float("-inf") # avoid moves not seen
#         return self.wins[n] / self.visits[n] # average weight
#
#     def find_Rchild(self.board): # picks one random child of current node
#         if self.board.checkVictory(player):
#             return None
#         # [code] picks a random move from the possible children (empty moves)
#
#     def find_child(self.board): # finds all child of current node
#         if self.board.checkVictory(player):
#             return set()
#         # [code] enumerates through all possible moves from current node (step) and makes a move
#
#     def rollout(self, node): # adds more to the tree basically
#         path = self.find(node)
#         # [code] set the path of the leaf node (
#         self.expand(leaf) # expand from the leaf node i.e add all the possible moves to the tree from the leaf
#         val = self.simulate(leaf) # tells what the value (# wins/#times passsed) from the node selected i.e win chance from the current move
#         self.backpropagate(path,val) # updates path w/# of wins from the leaf node
#
#     def selection(self, node): # used to find an unexplored descendent of the node
#         path = []
#         while True:
#             path.append(node)
#             if node not in self.children or not self.children[node]: # node not explored
#                 return path
#             # [code] if unexplored then append path from unexplored node (move) and return path
#             node = self.UCT(node) # go another layer
#
#     def UCT(self, node): # finds child of node that balances exploration and exploitation
#         # makes sure all children of node are expanded i.e all moves listed in tree
#         assert all(n in self.children for n in self.children[node])
#
#         def UCT_helper(n, node):
#             return self.wins[n] / self.visits[n] + self.weight * math.sqrt(math.log(self.visits(node)) / self.visits[n])
#
#         return max(self.children[node], key=UCT_helper())
#
#     def backpropagate(path, reward):
#         # sends the # of wins back up to the ancestor node of the current node
#         for node in reversed(path):
#             self.wins[node] += reward
#             self.visits[node] += 1
#
#     def expand(self, node):
#         if node in self.children:
#                 return # already expanded so don't need to expand
#         self.children[node] = node.find_child()
#
#     def simulate(self, node):