from constants import WINDOW_WIDTH, WINDOW_HEIGHT, ARRAY_SIZE
from run import draw_rects

import random

class SortingAlgorithm():
    def __init__(self, algorithm_name, complexity):
        self._name = algorithm_name
        self._complexity = complexity
        self._rand_array = random.sample(range(WINDOW_HEIGHT), self._complexity)

    @property
    def rand_array(self):
        return self._rand_array

    #For updating array size
    @rand_array.setter
    def rand_array(self, value=WINDOW_HEIGHT):
        self._rand_array = random.sample(range(value), self._complexity)

    def run(self):
        self.sort()

class BubbleSort(SortingAlgorithm):
    def __init__(self, complexity):
        super().__init__("BubbleSort", complexity)

    def sort(self):
        for i in range (len(self._rand_array)):
            for j in range(len(self._rand_array) - i - 1):
                if(self._rand_array[j] > self._rand_array[j + 1]):
                    self._rand_array[j], self._rand_array[j + 1] = self._rand_array[j + 1], self._rand_array[j]

                draw_rects(self, self._complexity, self._rand_array[j], self._rand_array[j + 1])

class QuickSort(SortingAlgorithm):
    def __init__(self, complexity):
        super().__init__("QuickSort", complexity)

    def partition(self,start, end):
        x = self._rand_array[end]
        i = start - 1
        for j in range(start, end + 1, 1):
            if self._rand_array[j] <= x:
                i += 1
                if i < j:
                    self._rand_array[i], self._rand_array[j] = self._rand_array[j], self._rand_array[i]
                    draw_rects(self, self._complexity, self._rand_array[i], self._rand_array[j])

        return i

    def sort(self, start=0, end=None):
        if end is None:
            end = self._complexity - 1

        if start < end:
            pivot = self.partition(start,end)
            self.sort(start, pivot-1)
            self.sort(pivot+1, end)

class InsertionSort(SortingAlgorithm):
    def __init__(self, complexity):
        super().__init__("InsertionSort", complexity)

    def sort(self):
        for i in range(len(self._rand_array) - 2, -1, -1):
            key = self._rand_array[i]
            j = i + 1

            while (j < len(self._rand_array)) and (key > self._rand_array[j]):
                self._rand_array[j], self._rand_array[j - 1] = self._rand_array[j-1], self._rand_array[j]
                j += 1

                draw_rects(self, self._complexity)

            self._rand_array[j - 1] = key

            draw_rects(self, self._complexity)




