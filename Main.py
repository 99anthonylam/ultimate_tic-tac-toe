from tic_tac_toe import *
from ultimate_ttt import *
# public class Node {
#     Node parent:
#     List<Node> children
# }

if __name__ == "__main__":
    # THIS SECTION FOR TESTING PURPOSES ONLY
    # firstWins = 0
    # secondWins = 0
    # noWins = 0
    # for _ in range (50):
    #     game = ultimate_ttt()
    #     game.quickStart1()  # for testing purposes, two AI of difficulty 3 play against each other
    #     if game.winner == 1:
    #         firstWins += 1
    #     elif game.winner == -1:
    #         secondWins += 1
    #     else:
    #         noWins += 1
    #     print("")
    # print("The first AI won {} times, the second AI won {}, {} ties".format(str(firstWins), str(secondWins), str(noWins)))
    # game.quickStart2()  # for testing purposes, first AI has difficulty 2, second AI has difficulty 3
    # ******COMMENT OUT ABOVE FOR NORMAL GAMEPLAY

    # ******EVERYTHING BELOW THIS SHOULD BE UNCOMMENTED FOR NORMAL GAMEPLAY
    game = ultimate_ttt()
    choice = game.setupGame()  # as defined, 1 is human players only, 2 is one AI, 3 is two AI
    if choice == 1:
        game.twoHumanPlay()
    elif choice == 2:
        game.oneHumanPlay()
    else:
        game.twoAIPlay()