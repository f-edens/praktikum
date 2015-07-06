__author__ = 'fred'

import numpy as np


def komma_to_float(col_names):
    return {n: lambda x: float(x.replace(",", ".")) for n in col_names}


col_name_xy = ("x", "y")
col_name_xyerr = ("x", "y", "err")


class Data:
    def __init__(self, indata, col_names=("x", "y", "xerr", "yerr"), skip_lines=0, converters=None):
        self.col_names = {name: i for i, name in enumerate(col_names)}

        if not converters:
            self.data_source = np.genfromtxt(indata, skiprows=skip_lines)
        #                                             converters={i: komma_to_float for i in col_names})
        else:
            self.data_source = np.genfromtxt(indata, skip_header=skip_lines, converters=converters)#, names=col_names)

    def __getattr__(self, item):
        if item in self.col_names:
            return self.data_source[:, self.col_names[item]]
