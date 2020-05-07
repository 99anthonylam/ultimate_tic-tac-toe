# Ultimate Tic-Tac-Toe 

## Introduction
For our CS591 Game Theory project, we implemented Minimax with Alpha-beta pruning and Monte Carlo Tree Search to determine the age old question of two player games applied to Ultimate Tic-Tac-Toe: Should you go first or second? 

Helpful game rules and illustrations can be found [here](https://ultimate-t3.herokuapp.com/rules).

## Usage

In order to run and play against our agents, clone the git repo and run the respective drivers located in `./MCTS/driver.py` for MCTS and `./Main.py` for Minimax. Customization and play parameters can be found in their respective file comments.

**For MCTS:**

Running `driver.py` provides 3 options: pitting MCTS against Minimax, pitting MCTS against itself, and playing against the MCTS agent.

The main parameters are the scores assigned to winning and losing found in line 65 and 77 of `./MCTS/agent.py`. Setting the loss value to be a higher value when abs()'d makes the AI play defensively - avoiding losing. The parameter for number of iterations to run MCTS can be found in line 87 if `./MCTS/agent.py`. This is by default set to 1000, however, adjusting the value can increase performance speed at a trade off for accurateness of predicting optimal moves. Lower iterations allows for less computations but less in depth analysis. Likewise, higher values do the reverse.

**For Minimax:**


&nbsp;


Have fun!

-Jake, Danny, and Anthony
