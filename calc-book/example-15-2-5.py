# Chapter 15.2 example 5

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import dblquad


# Define the integrand: sin(y^2)
def integrand(y, x):
    return np.sin(y**2)

# y-limits: from x to 1
def y_lower(x):
    return x

def y_upper(x):
    return 1

# Outer integral limits: x from 0 to 1
result, error = dblquad(
    integrand,
    0, 1,         # x limits
    y_lower,
    y_upper
)

print(f"Result of integral: {result:.8f}")
print(f"Estimated error:   {error:.2e}")
