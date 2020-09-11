import numpy as np
from scipy.signal import convolve2d


class GameOfLife(object):
    def __init__(self, petri_dish, size):
        self.kernel = [[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]]
        self.size = size
        self.state = petri_dish.state

    def apply_rules(self):
        neighborhood = convolve2d(self.state, self.kernel, 'same')
        birth = (neighborhood == 3) & (self.state == 0)
        survive = ((neighborhood == 2) | (neighborhood == 3)) & (self.state == 1)
        result_state = np.zeros(shape=self.size, dtype=int)
        result_state[birth | survive] = 1
        self.state = result_state
        return result_state
