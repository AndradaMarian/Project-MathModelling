import numpy as np
from Modelare_Numerica.Source_Code.Stepper import Stepper



class Fitness:

    def __init__(self):
        self.stepper = Stepper()

    def fitness(self,start_field, end_field, delta):
        """
        Calculate fitness for particular candidate (start configuration of the field)
        :param start_field: candidate (start configuration)
        :param end_field: target (stop configuration)
        :param delta: number of steps to proceed before comparing to stop configuration
        :return: value in range [0, 1] that indicates fractions of cells that match their state
        """
        candidate = self.stepper.make_move(start_field, moves=delta)
        return (candidate == end_field).sum() / 400

    def score_population(self,population, target, delta):
        """
        Apply fitness function for each gene in a population
        :param population: list of candidate solutions
        :param target: 20x20 array that represents field in stopping condition
        :param delta: number of steps to revert
        :return: list of scores for each solution
        """
        return [self.fitness(gene, target, delta) for gene in population]

    def generate_population(self, size, random_state=-1):
        """
        Generating initial population of individual solutions
        :return: initial population as a list of 20x20 arrays
        """
        if random_state != -1:
            np.random.seed(random_state)
        initial_states = np.split(np.random.binomial(1, 0.5, (20 * size, 20)).astype('uint8'), size)
        return [self.stepper.make_move(state, 5) for state in initial_states]

    def generate_problem(self, board, warm_up_steps):
        return board, self.stepper.make_move(board, warm_up_steps)

    def generate_problem_default(self, warm_up_steps):
        """ Generates example problem """
        np.random.seed(42)

        board = np.random.binomial(1, 0.01, (20, 20)).astype('uint8')
        # toad
        board[2, 3:6] = 1
        board[3, 2:5] = 1
        # glider 1
        board[9, 5:8] = 1
        board[8, 7] = 1
        board[7, 6] = 1
        # glider 2
        board[16, 3:6] = 1
        board[15, 5] = 1
        board[14, 4] = 1
        # beacon 1
        board[2:4, 14:16] = 1
        board[4:6, 16:18] = 1
        # beacon 2
        board[14:16, 14:16] = 1
        board[16:18, 16:18] = 1
        return board, self.stepper.make_move(board, warm_up_steps)