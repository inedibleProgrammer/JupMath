import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Numerical Laplace Transform for complex s
def laplace_transform(f, s):
    # Integrate real and imaginary parts separately
    integrand_real = lambda t: np.real(f(t) * np.exp(-s * t))
    integrand_imag = lambda t: np.imag(f(t) * np.exp(-s * t))
    
    real_part, _ = quad(integrand_real, 0, np.inf, limit=100)
    imag_part, _ = quad(integrand_imag, 0, np.inf, limit=100)
    
    return real_part + 1j * imag_part
    
    
# Function f(t)
f = lambda t: np.exp(-2 * t)

# Try for several complex s values
t_vals = np.linspace(0, 10, 100)
# s_reals = complex(t, 0)
# s_imags = complex(0, t)
# s_vals = [1 + 0j, 2 + 1j, 3 + 2j, 1 - 1j]

F_reals = []
F_imags = []

for t in t_vals:
    s_real = complex(t, 0)
    s_imag = complex(0, t)
    F_real = laplace_transform(f, s_real)
    F_reals.append(F_real)
    F_imag = laplace_transform(f, s_imag)
    F_imags.append(F_imag)


# for s in s_reals:
    # F_num = laplace_transform(f, s)
    # F_exact = 1 / (s + 2)
    # print(f"s = {s:>7} -> Numeric: {F_num:.6f}, Exact: {F_exact:.6f}")


plt.plot(t_vals, F_reals)
plt.plot(t_vals, F_imags)
plt.grid(True)
plt.show()
