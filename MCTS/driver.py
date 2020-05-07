import code
import sys, os
sys.path.append(os.path.join(sys.path[0], '..'))
import ultimate_ttt
import tic_tac_toe
import minmax
from UTTT import *
from agent import *
from State import *

# Helper to link our game modules for option 1
def link_boards(UTTT, ult_ttt):
    for i,game in enumerate(UTTT.board):
        for j, row in enumerate(game.board):
            ult_ttt.board[i].board[j] = row

choice = int(input("Type 1 to pit MTCS against Minimax, 2 to watch MCTS vs MCTS, 3 to play against MCTS: "))
while (choice != 1 and choice != 2):
    choice = int(input("Input must be 1,2 or 3: "))

if (choice == 1):
    st = State()
    Game = st.game
    player = 1
    while (Game.checkVictory() == 2):
        if (player < 0):
            print("Minimax Agent")
            temp = ultimate_ttt.ultimate_ttt()
            link_boards(Game, temp)
            temp.minmaxAgent = minmax.minmax(3)
            # code.interact(local=dict(globals(), **locals()))
            temp.last_move = (Game.last_move%10)
            chosenTile = temp.minmaxAgent.algorithm(temp, player, temp.getPossibleActions())
            pos= int(chosenTile % 10)
            game =  int((chosenTile - pos) / 10)
            Game.board[game - 1].place(player, pos)
            Game.last_move = chosenTile
            player *= -1

        else:
            print("MCTS Agent")
            Game = findNextMove(Game, player)
            player *= -1

        Game.draw()
        print("@!$@!#$@!#$@!#$@!#$!@#$!@#$@!#$@!#$@!")

    print("Game has been won by marker {}".format(tic_tac_toe.tic_tac_toe.map_to_xo(tic_tac_toe.tic_tac_toe,Game.checkVictory())))

elif (choice == 2):
    Game = UTTT()
    player = 1
    while (Game.checkVictory() == 2):
        Game = findNextMove(Game, player)
        Game.draw()
        print("@!$@!#$@!#$@!#$@!#$!@#$!@#$@!#$@!#$@!")
        player *= -1
    Game.draw()
    if Game.status == 0:
        print("Game resulted in a tie")
    elif Game.status == 1:
        print("Agent 1 has won!")
    else:
        print("Agent 2 has won!")

elif (choice == 3):
    player = 0
    Game = UTTT()
    print("Initializing game against MCTS agent")
    print("Flipping a coin!")

    if (random.randint(1,2) == 1):
        player = 1
        print("Heads!, you play first")
    else:
        print("Tails :(, the agent will play first")
        player = -1
        Game = findNextMove(Game, player)
        Game.draw()
        player = 1

    while (Game.checkVictory() == 2):
        if player == -1:
            print("Agent's turn to play!")
            Game = findNextMove(Game, player)
        else:
            if Game.last_move:
                print(f"Agent just played {Game.last_move}")
            print("Player {}, your marker is {}".format(player, Game.board[0].map_to_xo(player)))
            move = int(input("Enter your move (e.g. 39 for the bottom right corner of game 3): "))
            while (Game.isValid(move)[0] == False):
                print("Your move is not valid - {}".format(Game.isValid(move)[1]))
                move = int(input("Enter your move (e.g. 39 for the bottom right corner of game 3): "))
            pos = int(move%10) #e.g. 9
            game = int((move-pos)/10) #e.g. 3
            Game.last_move = move
            Game.board[game-1].place(player, pos)

        Game.draw()
        player *= -1

    print("Game has been won by marker {}".format(tic_tac_toe.tic_tac_toe.map_to_xo(tic_tac_toe.tic_tac_toe,Game.checkVictory())))

