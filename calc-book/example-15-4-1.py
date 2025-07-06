
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import dblquad
from scipy.optimize import fsolve
from scipy.interpolate import interp1d

def first_attempt():
    def integrand(y, x):
        return x * y

    x_min = 0
    x_max = 1

    def y_min(x):
        return 1-x

    def y_max(x):
        return 1

    result, error = dblquad(
        integrand,
        x_min,
        x_max,
        y_min,
        y_max,
    )

    print(result)

# expected answer: 0.20833333333333334
first_attempt()
