from scipy.sparse import coo_matrix
import matplotlib.pyplot as plt
import numpy as np
import time


class Display:
    def __init__(self, max_size):
        plt.ion()
        self.fig = plt.figure()
        self.ax = None
        self.line = None
        self.max_size = max_size

    def plot_coo_matrix(self, m, fig):
        if not isinstance(m, coo_matrix):
            m = coo_matrix(m)
        ax = fig.add_subplot(111, facecolor='black')
        ax.set_xlim(0, m.shape[1])
        ax.set_ylim(0, m.shape[0])
        ax.set_aspect('equal')
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.invert_yaxis()
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        # ax.plot(m.col, m.row, 's', color='white', ms=2)
        return ax

    def proc_state(self, state):
        x = []
        y = []
        for point in state:
            x.append(point[0])
            y.append(point[1])
        return x, y

    def first_figure(self, x, y):
        matrix = coo_matrix((np.ones(len(x)), (x, y)), shape=(self.max_size, self.max_size))
        self.ax = self.plot_coo_matrix(matrix, self.fig)
        self.line, = self.ax.plot(matrix.col, matrix.row, 's', color='white', ms=2)

    def update_figure(self, x, y):
        self.line.set_xdata(x)
        self.line.set_ydata(y)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def delay_interval(self, var):
        time.sleep(var)






