from Modelare_Numerica.Source_Code.Mutation import Mutate
from Modelare_Numerica.Source_Code.Fitness import Fitness
from Modelare_Numerica.Source_Code.Selection import Selector
from Modelare_Numerica.Source_Code.Evolution import Evolution
import numpy as np

class Solve:
    def __init__(self, display):

        self.display = display
        self.mutant = Mutate()
        self.fitness = Fitness()
        self.selector = Selector()
        self.evolution = Evolution()

    def solve(self, target, delta, population_size, no_generations):
        """
            :param target: 20x20 array that represents field in stopping condition
            :param delta: number of steps to revert
            :param n_generations: number of evolution generations. Overrides initialization value if specified
            :return: 20x20 array that represents the best start field found and associated fitness value
        """
        best_gen = 0 # Keep track of best generation performance
        population = self.fitness.generate_population(population_size)
        best_score_vector = []
        for generation in range(no_generations):
            population = self.evolution.evolve(population, target, delta, self.display)
            score_list = self.fitness.score_population(population, target, delta) # Recompute the new generation score
            sorted_indices = np.argsort(score_list)[::-1] # Sort score_list
            best_score_index = sorted_indices[0] # Get index of best score
            score1 = score_list[best_score_index]
            if score1 > best_gen:
                best_gen = score1
                print("Generation ", generation, " reached a new best: ", best_gen, "!!")
            else:
                print("Generation ", generation, ": ", score1)
            if generation == 0:
                self.display.plot_result(population[best_score_index], "21", "GA solution start")

            self.display.update_title(generation)
            best_score_vector.append(best_gen)
        self.display.create_performance_graph(best_score_vector)
        return best_score_vector


