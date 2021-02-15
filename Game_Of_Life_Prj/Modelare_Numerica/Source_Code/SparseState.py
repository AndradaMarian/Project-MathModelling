import copy


class SparseSetState:
    def __init__(self, grid):
        self.grid = grid

    def copy(self):
        return SparseSetState(copy.copy(self.grid))

    def get_neighbours(self, elem, max_size):
        # Returns the neighbours of a live cell if they lie within the bounds of the grid specified by max_size
        l = []
        if elem[0] - 1 >= 0:
            l.append((elem[0] - 1, elem[1]))
        if elem[0] - 1 >= 0 and elem[1] - 1 >= 0:
            l.append((elem[0] - 1, elem[1] - 1))
        if elem[0] - 1 >= 0 and elem[1] + 1 < max_size:
            l.append((elem[0] - 1, elem[1] + 1))
        if elem[1] - 1 >= 0:
            l.append((elem[0], elem[1] - 1))
        if elem[1] - 1 >= 0 and elem[0] + 1 < max_size:
            l.append((elem[0] + 1, elem[1] - 1))
        if elem[1] + 1 < max_size:
            l.append((elem[0], elem[1] + 1))
        if elem[0] + 1 < max_size:
            l.append((elem[0] + 1, elem[1]))
        if elem[1] + 1 < max_size and elem[0] + 1 < max_size:
            l.append((elem[0] + 1, elem[1] + 1))
        return l

    def equals(self, other):
        if other is None:
            return False
        return self.grid == other.grid

    def apply_rules(self, rules, max_size):
        # Calls the actual rules and provides them with the grid and the neighbour function
        self.grid = rules.apply_rules(self.grid, max_size, self.get_neighbours)
        return self