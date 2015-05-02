__author__ = 'fred'

import numpy as np


class Data:
    def __init__(self, indata, col_names=("x", "y", "xerr", "yerr"), skip_lines=0):
        self.col_names = {name: i for i, name in enumerate(col_names)}

        self.data_source = np.genfromtxt(indata, skiprows=skip_lines)

    def __getattr__(self, item):
        if item in self.col_names:
            return self.data_source[:, self.col_names[item]]