__author__ = 'fred'

import numpy as np
from scipy import optimize
from io import BytesIO

from scipy.optimize import leastsq as lsq

data = """0	10.7211538462	0.3372167807
50	10.045045045	0.3141423395
107	10.0267857143	0.3123132646
165	8.3759398496	0.2587336329
215	7.0891719745	0.2172391352
330	6.4540229885	0.1961323762
520	5.3142857143	0.1610792422
770	3.9363957597	0.1187560548"""


def logistic_fun(x, n_0, x_0, a):
    return n_0*(1+np.exp(-a*x_0))/(1 + np.exp(a*(x-x_0)))


def expo_fun(x, n_0, a):
    return n_0 * np.exp(a*x)

def main():
    npdata = np.genfromtxt(BytesIO(data.encode()))
    data_x, data_y = npdata[:, 0], npdata[:, 1]
    data_x *= 1e-6
    ps, es = optimize.curve_fit(logistic_fun, data_x, data_y)
    print(ps, "\n", es)
    print()
    ps, es = optimize.curve_fit(expo_fun, data_x, data_y)
    print(ps, "\n", es)
    pass


if __name__ == '__main__':
    main()