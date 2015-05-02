#!/usr/bin/env python3
__author__ = 'fred'

from pythonUtils.data import Data
import numpy as np

source = "files/mess.data"
output_file = "files/fft.data"


def fft(xdata, ydata):
    return np.fft.rfftfreq(len(ydata), xdata[1] - xdata[0]), \
        abs(np.fft.rfft(ydata))


def main():
    dat = Data(source, ("x", "y"))
    y_vals = dat.y
    x_vals = np.arange(0, (dat.x[1] - dat.x[0]) * (len(y_vals)), dat.x[1] - dat.x[0])

    # x_vals = np.arange(0, 100, 1./20)
    # y_vals = np.sin(2*np.pi * 3.048 * x_vals) +1

    fft_xvals, fft_vals = fft(x_vals, y_vals)
    # fft_vals = np.fft.rfft(y_vals)
    # fft_xvals = np.fft.rfftfreq(len(y_vals), (x_vals[1] - x_vals[0]))

    with open(output_file, "w+") as out:
        for (x, y) in zip(fft_xvals, fft_vals):
            out.write("%f\t%f\n" % (x, abs(y)))
    print()


if __name__ == '__main__':
    main()