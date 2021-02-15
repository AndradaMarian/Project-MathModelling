from Modelare_Numerica.Source_Code.Game import Game
from Modelare_Numerica.Source_Code.SparseRules import SparseSetRules
from Modelare_Numerica.Source_Code.SparseState import SparseSetState
import time
from Modelare_Numerica.Source_Code.Configuration_Board import The_Board_Builder


MAX_ITER = 1500 # Number of game cycles
MAX_SIZE = 50 # The NxN matrix

board1 = {(39, 40),(39, 41),(40, 39),(40, 40),(41, 40)} # The board can be given as dots

board2 = {(10,10,"Glider"),(39, 40, "Block"),(15,15, "Bee-hive"),(20,20,"Blinker"),
          (10, 30, "Toad"),(25, 25, "Eater"), (25, 40, "Loaf"), (15, 40, "LWSS"),
          (5, 40, "Boat")} # Or as figures and X_start & Y_start - check Configuration_Board.py

board_builded = The_Board_Builder().parse_grid(board2)#(board1) # Either given board formation, it is process and converted
                                                # to corresponding dots

rules = SparseSetRules() # Instantiate rule class; For a better performance, a sparse board was chosen as to iterate
                        #  only over the points of interest and not the whole board
game = Game(SparseSetState(board_builded), rules,MAX_SIZE) # instantiate  game class according to the rules, matrix_size and Sparse
t = time.time() # Runtime
time_delay = 0.2
game.run_game(MAX_ITER, time_delay) # Play the game according max no iterations and the time delay between frames


print(time.time()-t)
input("Press Enter to continue...") # Wait for user input to end program