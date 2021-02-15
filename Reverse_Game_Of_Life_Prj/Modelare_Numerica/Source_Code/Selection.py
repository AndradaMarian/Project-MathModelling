import numpy as np

class Selector:
    def selection(self, population, scores, retain_frac=0.8, retain_random=0.05):
        """
        Apply selection operator to the population
        :param population: list of candidate solutions
        :param scores: list of score associated with each individual
        :param retain_frac: percent of top individuals to retain
        :param retain_random: chance of retaining sub-optimal individuals in the population
        """
        retain_len = int(len(scores) * retain_frac)
        sorted_indices = np.argsort(scores)[::-1]
        population = [population[idx] for idx in sorted_indices]
        selected = population[:retain_len]
        leftovers = population[retain_len:]

        for gene in leftovers:
            if np.random.rand() < retain_random:
                selected.append(gene)
        return selected