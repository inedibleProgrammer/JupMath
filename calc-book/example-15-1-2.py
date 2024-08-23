# Ch 15.1 example 2

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import dblquad

x = np.linspace(-1, 1, 1000)
y = np.linspace(-2, 2, 1000)
xv, yv = np.meshgrid(x, y)
z = np.sqrt(1 - xv**2)
# print(xv)

ans1 = np.trapezoid(np.trapezoid(z, y, axis=0), x, axis=0)
print(ans1)
print(2 * np.pi) # The true answer
integrand = lambda y, x: np.sqrt((1 - x**2))
ans2, error = dblquad(integrand, -1, 1, -2, 2)
print(ans2, error)

