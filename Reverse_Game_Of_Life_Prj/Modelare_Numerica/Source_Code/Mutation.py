import numpy as np

class Mutate:
    def mutate(self, field, switch_frac=0.1):
        """ Inplace mutation of the provided field """
        a = np.random.binomial(1, switch_frac, size=(20, 20)).astype('bool')
        field[a] += 1
        field[a] %= 2
        return field

    def crossover(self, mom, dad):
        """ Take two parents, return two children, interchanging half of the allels of each parent randomly """
        select_mask = np.random.binomial(1, 0.5, size=(20, 20)).astype('bool')
        child1, child2 = np.copy(mom), np.copy(dad)
        child1[select_mask] = dad[select_mask]
        child2[select_mask] = mom[select_mask]
        return child1, child2