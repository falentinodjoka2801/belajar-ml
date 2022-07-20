import numpy as np
from util import get_data
from datetime import datetime
from sortedcontainers import SortedList
import operator
import matplotlib as plt

class KNN:
    def __init__(self, k):
        self.k  =   k

    def fit(self, x, y):
        self.x  =   x
        self.y  =   y

    def predict(self, x):
        #y adalah matrix nol yang ordonya sebanyak elemen x
        y   =   np.zeros(len(x))

        for j, k in enumerate(x):
            sl  =   SortedList()

            for l, m in enumerate(self.x):
                _distance   =   

