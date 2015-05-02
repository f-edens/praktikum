#!/usr/bin/env python3

__author__ = 'fred'

from pythonUtils.data import Data
import numpy as np

source = "files/mess.data"
output_file = "files/mess_T_korrigiert.data"


def main():
    dat = Data(source, ("t", "x"))

    x_blocks = []
    first_x = 0
    last_x = 0
    last_t = 0

    for (t, x) in zip(dat.t[1:], dat.x[1:]):
        last_x += 1
        if t < last_t:
            x_blocks.append(dat.x[first_x:last_x])
            first_x = last_x
        last_t = t
    x_blocks.append(dat.x[first_x:last_x])
#   x_blocks[0] = x_blocks[0][::2]
#   x_blocks = [sub_list - min(sub_list) for sub_list in x_blocks]

    xdata = [item for sublist in x_blocks for item in sublist]

    with open(output_file, "w+") as out:
        t = 0
        delta_t = dat.t[2] - dat.t[0]
        for x in xdata:
            out.write("%f\t%f\n" % (t, x))
            t += delta_t * (1 + (t < 105))/4


if __name__ == '__main__':
    main()