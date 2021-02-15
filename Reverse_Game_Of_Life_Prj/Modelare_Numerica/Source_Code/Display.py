from scipy.sparse import coo_matrix
import matplotlib.pyplot as plt
import numpy as np
import time


class Display:
    def __init__(self, max_size):
        plt.ion()
        self.fig = plt.figure()
        self.fig.set_size_inches(10.5, 10.5)
        self.ax11 = self.fig.add_subplot(221, facecolor='black')
        self.line11 = None
        self.ax12 = self.fig.add_subplot(222, facecolor='black')
        self.line12 = None
        self.ax21 = self.fig.add_subplot(223, facecolor='black')
        self.line21 = None
        self.ax22 = self.fig.add_subplot(224, facecolor='black')
        self.line22 = None
        self.max_size = max_size
        self.first = None
        self.fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

    def update_title(self,text):
        self.fig.suptitle('Generation: ' + str(text), fontsize=14, fontweight='bold')

    def plot_result(self, matrix, subplot_no, text):
        x, y = np.nonzero(matrix)
        if subplot_no == "22":
            if not self.first:  # Workaround to intialize the first plot and prepare the specific struct for further iterations
                self.first = True
                self.line22=self.first_figure(x, y, self.ax22, text)
            else:
                self.update_figure(x, y, self.line22)
        if subplot_no == "11":
            self.line11 =self.first_figure(x, y, self.ax11, text)
        if subplot_no == "12":
            self.line12 =self.first_figure(x, y, self.ax12, text)
        if subplot_no == "21":
            self.line21 =self.first_figure(x, y, self.ax21, text)

    def plot_coo_matrix(self, m, ax, text):
        if not isinstance(m, coo_matrix):
            m = coo_matrix(m)
        ax.set_xlim(0, m.shape[1])
        ax.set_ylim(0, m.shape[0])
        ax.set_title(text)
        ax.set_aspect('equal')
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.invert_yaxis()
        ax.set_xticks([])
        ax.set_yticks([])
        return ax

    def proc_state(self, state):
        x = []
        y = []
        for point in state:
            x.append(point[0])
            y.append(point[1])
        return x, y

    def first_figure(self, x, y, ax, text):
        matrix = coo_matrix((np.ones(len(x)), (x, y)), shape=(self.max_size, self.max_size))
        self.plot_coo_matrix(matrix, ax, text)
        line, = ax.plot(matrix.col, matrix.row, 's', color='white', ms=10)
        return  line

    def update_figure(self, x, y, line):
        line.set_xdata(y)
        line.set_ydata(x)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def delay_interval(self, var):
        time.sleep(var)

    def create_performance_graph(self, data_vector):
        self.chart, self.ax_chart = plt.subplots()
        self.chart.set_size_inches(10.5, 10.5)
        self.chart.suptitle("Accuary evolution")
        self.ax_chart.plot(data_vector, color='blue', ms=5)




