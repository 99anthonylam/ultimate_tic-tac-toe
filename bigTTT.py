import numpy as np
import math
from tic_tac_toe import *
from player import *

# boards and squares are interpreted with the following NUMPAD system:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |

class bigTTT:
    def __init__(self):
        self.boards = [tic_tac_toe() for x in range(9)]
        self.players = [player() for x in range(2)]
        self.players[0].configureMarker(1)
        self.players[1].configureMarker(-1)

    def checkVictory(self, marker):
        # check horizontals
        if ((self.boards[0].winner.equals(marker) and self.boards[1].winner.equals(marker) and self.boards[
            2].winner.equals(marker))
                or (self.boards[4].winner.equals(marker) and self.boards[5].winner.equals(marker) and self.boards[
                    6].winner.equals(marker))
                or (self.boards[7].winner.equals(marker) and self.boards[8].winner.equals(marker) and self.boards[
                    9].winner.equals(marker))
                # check columns
                or (self.boards[1].winner.equals(marker) and self.boards[4].winner.equals(marker) and self.boards[
                    7].winner.equals(marker))
                or (self.boards[2].winner.equals(marker) and self.boards[5].winner.equals(marker) and self.boards[
                    8].winner.equals(marker))
                or (self.boards[3].winner.equals(marker) and self.boards[6].winner.equals(marker) and self.boards[
                    9].winner.equals(marker))
                # diagonals
                or (self.boards[1].winner.equals(marker) and self.boards[5].winner.equals(marker) and self.boards[
                    9].winner.equals(marker))
                or (self.boards[3].winner.equals(marker) and self.boards[5].winner.equals(marker) and self.boards[
                    7].winner.equals(marker))):
            return True
