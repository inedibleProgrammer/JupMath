# This magically works. I had chat gpt generate this
import numpy as np
import math
import matplotlib.pyplot as plt

# Stehfest coefficients
def stehfest_coefficients(N):
    assert N % 2 == 0, "N must be even"
    V = np.zeros(N)
    for k in range(1, N + 1):
        summation = 0
        for j in range(int((k + 1) / 2), min(k, N // 2) + 1):
            num = j**(N//2) * math.factorial(2*j)
            den = (math.factorial(N//2 - j) *
                   math.factorial(j) *
                   math.factorial(j - 1) *
                   math.factorial(k - j) *
                   math.factorial(2*j - k))
            summation += num / den
        V[k - 1] = (-1)**(k + N//2) * summation
    return V

# Gaver-Stehfest inverse Laplace
def gaver_stehfest(F, t, N=10):
    V = stehfest_coefficients(N)
    ln2 = np.log(2)
    total = 0.0
    for k in range(1, N + 1):
        s = k * ln2 / t
        total += V[k - 1] * F(s)
    return ln2 / t * total
    
    
# Define Laplace-domain function
def F(s):
    return 1 / (s + 2)

# Evaluate at multiple time values
t_vals = np.linspace(0.1, 5, 100)
f_numeric = [gaver_stehfest(F, t, N=10) for t in t_vals]
f_exact = np.exp(-2 * t_vals)

# Plot comparison
plt.plot(t_vals, f_numeric, label='Gaver-Stehfest (numerical)')
plt.plot(t_vals, f_exact, '--', label='Exact $e^{-2t}$')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Inverse Laplace Transform via Gaver-Stehfest')
plt.legend()
plt.grid(True)
plt.show()
