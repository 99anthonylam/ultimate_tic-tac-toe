from UTTT import *
from agent import *
from State import *

Game = UTTT()
player = 0

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

print("Game has been won by marker {}".format(Game.checkVictory()))