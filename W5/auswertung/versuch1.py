__author__ = 'fred'

from scipy import optimize as opt
import numpy as np

from pythonUtils import data

input_file = "ar.data"


def main():
    dat = data.Data(input_file, col_names=["x", "xerr", "y", "yerr"])
    x = dat.x
    y = dat.y
    fits, errs = opt.curve_fit(lambda x, a, b: a * x + b, x, y)
    print(str(np.asmatrix(errs) * np.asmatrix(fits).transpose()))
    with open(input_file + ".fit", "w+") as out_file:
        out_file.write(str(fits) + "\n")
        out_file.write(str(errs))


if __name__ == '__main__':
    main()
