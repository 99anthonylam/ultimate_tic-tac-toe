from tic_tac_toe import *
from ultimate_ttt import *
# public class Node {
#     Node parent:
#     List<Node> children
# }

if __name__ == "__main__":
    game = ultimate_ttt()
    #  COMMENT OUT THE QUICKSTARTS FOR NORMAL GAMEPLAY
    game.quickStart1()  # for testing purposes, two AI of difficulty 3 play against each other
    # game.quickStart2()  # for testing purposes, first AI has difficulty 2, second AI has difficulty 3

    #  EVERYTHING BELOW THIS SHOULD BE UNCOMMENTED FOR NORMAL GAMEPLAY
    # choice = game.setupGame()  # as defined, 1 is human players only, 2 is one AI, 3 is two AI
    # if choice == 1:
    #     game.twoHumanPlay()
    # elif choice == 2:
    #     game.oneHumanPlay()
    # else:
    #     game.twoAIPlay()