from Modelare_Numerica.Source_Code.Stepper import Stepper
from Modelare_Numerica.Source_Code.SparseRules import SparseSetRules
from Modelare_Numerica.Source_Code.SparseState import SparseSetState
from Modelare_Numerica.Source_Code.Solver import Solve
from Modelare_Numerica.Source_Code.Fitness import Fitness
from Modelare_Numerica.Source_Code.Display import Display

from Modelare_Numerica.Source_Code.Configuration_Board import The_Board_Builder

# 1. Init board
# Y,X
board3 = {(2,2,"Toad"),(2,15,"Block"),(4,17,"Block"),
          (13,2),(19,10),(14,15,"Block"),(16,17,"Block")}

board_builded = The_Board_Builder().parse_grid(board3)#(board1) # Either given board formation, it is process and converted
                                                # to corresponding dots
board = The_Board_Builder().create_board(board_builded)

# 2. Run it ~5 cycles to "warm up"
warm_up = 5

# Custom board
#init_board, target_board = Fitness().generate_problem(board, warm_up)

# Default board
init_board, target_board = Fitness().generate_problem_default(warm_up)

display = Display(20)
display.plot_result(init_board,"11","Target start")
display.plot_result(target_board,"12","Target end")

# 3. Use end state of warm up as target in solver
population_size = 200
no_generations = 100
delta = 0
solver = Solve(display)
performance = solver.solve(target_board, delta,population_size,no_generations)

#print(time.time()-t)
input("Press Enter to continue...") # Wait for user input to end program
exit()

