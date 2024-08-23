# Ch 15.1 example 1

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2, 100)
y = np.linspace(0, 2, 100)
xv, yv = np.meshgrid(x, y)
z = 16 - xv**2 - 2*yv**2
# print(xv)
# print(z)
ans = np.trapz(np.trapz(z, y, axis=0), x, axis=0)

print(ans)

