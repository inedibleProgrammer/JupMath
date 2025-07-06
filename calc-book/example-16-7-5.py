import numpy as np
from scipy.integrate import dblquad

# Define the integrand in Cartesian coordinates
def integrand(y, x):
    return 4 * x * y + 1 - x**2 - y**2

# Limits of integration:
# Integrate over the unit disk x^2 + y^2 <= 1
# We'll define y-limits as functions of x to stay in Cartesian

def y_lower(x):
    return -np.sqrt(1 - x**2)

def y_upper(x):
    return np.sqrt(1 - x**2)

# x goes from -1 to 1
result, error = dblquad(integrand, -1, 1, y_lower, y_upper)

print(f"Surface integral = {result:.6f}")
