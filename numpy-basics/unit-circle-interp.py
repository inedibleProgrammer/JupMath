import numpy as np
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Define the implicit function for the unit circle
def unit_circle_eq(y, x):
    return x**2 + y**2 - 1

# Define x-values in the valid domain for a unit circle
x_vals = np.linspace(-1, 1, 200)
y_vals = []

# Use fsolve to find the upper half (positive y)
for x in x_vals:
    y = fsolve(unit_circle_eq, x0=0.5, args=(x))[0]
    y_vals.append(y)

y_vals = np.array(y_vals)

# Create interpolation function for upper half of circle
f_upper = interp1d(x_vals, y_vals, kind='linear', fill_value='extrapolate')

# Evaluate interpolated function
print(f"f_upper(0.5) = {f_upper(0.5)}")

# Optional: plot the result
x_test = np.linspace(-1, 1, 200)
y_test = f_upper(x_test)

plt.plot(x_vals, y_vals, label='Original points (fsolve)', alpha=0.5)
plt.plot(x_test, y_test, label='Interpolated', linestyle='--')
plt.gca().set_aspect('equal')
plt.title("Upper Half of Unit Circle from fsolve + interp1d")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
