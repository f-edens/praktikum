__author__ = 'fred'

import inspect
import numpy as np


class Error:
    def cumulate(self, *others):
        if len(others) > 1:
            return Error.cumulate(self.cumulate(others[0]), *others[1:])

        def newfunc(*args):
            value = args[0]
            params, errs = args[1::2], args[2::2]
            return self.__func(value, *(params[:self.__n_params] + errs[:self.__n_params])) \
                + others[0].__func(value, *(params[self.__n_params:] + errs[self.__n_params:]))

        return Error(newfunc)


    def __init__(self, func):
        params = inspect.getargspec(func)
        if len(params[0]) % 2 == 0:
            raise ValueError("Falsche anzahl der Parameter")
        else:
            self.__n_params = len(params[0])/2
        self.__func = lambda *args: func(*args)**2
        print()

    def __call__(self, *args):
        if 2*len(args) > self.__n_params:
            print("Warnung: zu viele Parameter")
        return np.sqrt(self.__func(*args))

linear = Error(lambda v, x, dx: v/x*dx)
square = Error(lambda v, x, dx: 2*v/x*dx)