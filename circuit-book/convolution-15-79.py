import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the two functions
def x(t):
    return 4*np.exp(-t)

def h(t):
    return 5*np.exp(-2*t)

# Define convolution function using quad
def convolution(t):
    integrand = lambda tau: x(tau) * h(t - tau)
    result, _ = quad(integrand, 0, t)
    return result

# Evaluate over a range of t values
t_vals = np.linspace(0, 10, 200)
conv_vals = [convolution(t) for t in t_vals]

expected = 20*(np.exp(-t_vals) - np.exp(-2*t_vals))

# Plot the result
plt.plot(t_vals, conv_vals, label='x * h')
plt.plot(t_vals, expected)
plt.grid(True)
plt.show()
