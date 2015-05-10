__author__ = 'fred'

import numpy as np


def komma_to_float(input):
    return float(input.replace(",", "."))


col_name_xy = ("x", "y")
col_name_xyerr = ("x", "y", "err")


class Data:
    def __init__(self, indata, col_names=("x", "y", "xerr", "yerr"), skip_lines=0, converters=None):
        self.col_names = {name: i for i, name in enumerate(col_names)}

        if not converters:
            self.data_source = np.genfromtxt(indata, skiprows=skip_lines,
                                             converters=[komma_to_float for _ in col_names])
        else:
            self.data_source = np.genfromtxt(indata, skiprows=skip_lines, converters=converters)

    def __getattr__(self, item):
        if item in self.col_names:
            return self.data_source[:, self.col_names[item]]