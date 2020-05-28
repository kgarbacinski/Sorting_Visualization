from constants import WINDOW_WIDTH, WINDOW_HEIGHT, ARRAY_SIZE

from run import draw_rects

import random

class SortingAlgorithm():
    def __init__(self, algorithm_name):
        self._name = algorithm_name
        self._rand_array = random.sample(range(WINDOW_HEIGHT), ARRAY_SIZE)

    @property
    def rand_array(self):
        return self._rand_array

    #For updating array size
    @rand_array.setter
    def rand_array(self, value=WINDOW_HEIGHT):
        self._rand_array = random.sample(range(value), ARRAY_SIZE)

    def run(self):
        self.sort()

class BubbleSort(SortingAlgorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def sort(self):
        for i in range (len(self._rand_array)):
            for j in range(len(self._rand_array) - i - 1):
                if(self._rand_array[j] > self._rand_array[j + 1]):
                    self._rand_array[j], self._rand_array[j + 1] = self._rand_array[j + 1], self._rand_array[j]

            draw_rects(self, self._rand_array[j], self._rand_array[j + 1])
