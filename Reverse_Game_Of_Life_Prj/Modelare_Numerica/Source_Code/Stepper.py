import numpy as np


class Stepper:

    def __init__(self):
        self.M = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        """
        * * *
        * x *  - workaround for faster indexing
        * * *
        """


    def calc_neighs(self, field, i, j):
        """ Calculate number of neighbors alive (assuming square field) """
        neighs = 0
        n = len(field)
        for m in self.M:
            row_idx = m[0] + i
            col_idx = m[1] + j
            if (0 <= row_idx < n) and (0 <= col_idx < n):
                if row_idx >= 20 or col_idx >= 20: # Don't over index
                   continue
                value = field[row_idx][col_idx]
                if value.any():
                    neighs += 1
        return neighs

    def make_move(self, field, moves=1):
        """ Make a move forward according to Game of Life rules """
        n = len(field)
        cur_field = field
        for _ in range(moves):
            new_field = np.zeros((n, n), dtype='uint8')
            for i in range(n):
                for j in range(n):
                    neighs = self.calc_neighs(cur_field, i, j)
                    if i >= 20 or j >= 20: # Don't over index
                        continue
                    value = cur_field[i][j]
                    if value.any() and neighs == 2:
                        new_field[i][j] = 1
                    if neighs == 3:
                        new_field[i][j] = 1
            cur_field = new_field
        return cur_field




















































































