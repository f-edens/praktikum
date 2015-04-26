__author__ = 'fred'

import numpy as np
from scipy import optimize
from io import BytesIO

from scipy.optimize import leastsq as lsq

data = """0	10.4791248606	0.3480304704
50	9.8030160595	0.3249560292
107	9.7847567288	0.3231269543
165	8.1339108641	0.2695473226
215	6.847142989	0.228052825
330	6.211994003	0.206946066
520	5.0722567288	0.171892932
770	3.6943667742	0.1295697446"""


data_pb = """0	8.9811115104	0.2972302496
5	5.0032540334	0.1700432809
10	3.0248331846	0.1091601283
15	1.8822953388	0.0727996721
20	1.0670191931	0.0500643354
"""

def logistic_fun(x, n_0, x_0, a):
    return n_0*(1+np.exp(-a*x_0))/(1 + np.exp(a*(x-x_0)))


def expo_fun(x, n_0, a):
    return n_0 * np.exp(a*x)


def main():
    npdata = np.genfromtxt(BytesIO(data_pb.encode()))
    data_x, data_y = npdata[:, 0], npdata[:, 1]
    #data_x *= 1e-6
    # ps, es = optimize.curve_fit(logistic_fun, data_x, data_y)
    # print(ps, "\n", es)
    # print()
    ps, es = optimize.curve_fit(expo_fun, data_x, data_y)
    print(ps, "\n", es)
    pass


if __name__ == '__main__':
    main()