# Chapter 15.3 example 1

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import dblquad
from scipy.optimize import fsolve
from scipy.interpolate import interp1d

# I tackle the problem in cartesian coordinates
def first_attempt():

    def f1(x, y):
        return x**2 + y**2 - 1

    def f2(x, y):
        return x**2 + y**2 - 4


    x_left = -2
    x_right = 2

    y_bot = 0
    y_top = 2

    x1 = np.linspace(x_left, x_right, 5000)
    y1 = []
    for x in x1:
        y = fsolve(f1, x0=0.5, args=(x))[0]
        y1.append(y)


    x2 = np.linspace(x_left, x_right, 5000)
    y2 = []
    for x in x2:
        y = fsolve(f2, x0=0.5, args=(x))[0]
        y2.append(y)

    f1_interp = interp1d(x1, y1, kind='linear', fill_value="extrapolate")
    f2_interp = interp1d(x2, y2, kind='linear', fill_value="extrapolate")

    x_inner_left = fsolve(f1_interp, x0=-1)[0]
    x_inner_right = fsolve(f1_interp, x0=1)[0]

    x_outer_left = fsolve(f2_interp, x0=-1)[0]
    x_outer_right = fsolve(f2_interp, x0=1)[0]

    print(x_inner_left, x_inner_right, x_outer_left, x_outer_right)

    # def integrand(y, x):
    #     test1 = f1_interp(x)
    #     test2 = f2_interp(x)

    #     if(y >= test1) and (y <= test2):
    #         return 3*x + 4*y**2
    #     else:
    #         return 0

    def integrand(y, x):
        return 3*x + 4*y**2

    # Outer integral limits: x from 0 to 1
    # result, error = dblquad(
    #     integrand,
    #     x_left, x_right,         # x limits
    #     y_bot, y_top,
    # )

    result, error = dblquad(
        integrand,
        x_left, x_right,         # x limits
        f1_interp, f2_interp,
    )

    print(result)

# I try to use polar coordinates
def second_attempt():

    def integrand(theta, r):
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return (3*x + 4 * y**2) * r

    r_min = 1
    r_max = 2

    def theta_lower(r):
        return 0

    def theta_upper(r):
        return np.pi

    result, error = dblquad(
        integrand,
        r_min,
        r_max,
        theta_lower,
        theta_upper
    )

    print(result)

# Expected answer: 23.561944901923447

# first_attempt()
second_attempt()
