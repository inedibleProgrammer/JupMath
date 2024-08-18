# Calculus and Statistics
import numpy as np
from matplotlib import pyplot as plt

# integrals and derivatives

x = np.linspace(1, 10, 100)
y = 1/x**2 * np.sin(x)
dydx = np.gradient(y, x)
y_int = np.cumsum(y) * (x[1] - x[0])

plt.plot(x, y)
plt.plot(x, dydx)
plt.plot(x, y_int)
plt.show()
