import numpy as np
from Modelare_Numerica.Source_Code.Mutation import Mutate
from Modelare_Numerica.Source_Code.Fitness import Fitness
from Modelare_Numerica.Source_Code.Selection import Selector

class Evolution:

    def __init__(self):
        self.mutant = Mutate()
        self.fitness = Fitness()
        self.selector = Selector()
        self.first = False

    def evolve(self, population, target, delta, display, retain_frac=0.8, retain_random=0.05, mutate_chance=0.05):
        """
        Evolution step
        :param population: list or candidate solutions
        :param target: 20x20 array that represents field in stopping condition
        :param delta: number of steps to revert
        :param retain_frac: percent of top individuals to proceed into the next genetation
        :param retain_random: chance of retaining sub-optimal individual
        :param mutate_chance: chance of mutating the particular individual
        :param display: used for updating the plots
        :return: new generation of the same size
        """
        scores = self.fitness.score_population(population, target, delta)
        next_population = self.selector.selection(population, scores, retain_frac=retain_frac, retain_random=retain_random)
        best_score_index = scores.index(max(scores))
        if self.first is False:
            self.first = True
            display.plot_result(population[best_score_index], "21", "GA solution start")
        else:
            display.plot_result(population[best_score_index], "22", "GA solution running/end")

        # mutate everyone expecting for the best candidate
        for iteration, gene in enumerate(next_population):
            if np.random.rand() < mutate_chance:
                next_population[iteration] = self.mutant.mutate(gene)

        places_left = len(population) - len(next_population)
        children = []
        parent_max_idx = len(next_population) - 1
        while len(children) < places_left:
            mom_idx, dad_idx = np.random.randint(0, parent_max_idx, 2)
            if mom_idx != dad_idx:
                child1, child2 =  self.mutant.crossover(next_population[mom_idx], next_population[dad_idx])
                children.append(child1)
                if len(children) < places_left:
                    children.append(child2)
        next_population.extend(children)
        return next_population