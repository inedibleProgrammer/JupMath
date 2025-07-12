# The same example as Zach Star
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define grid over complex s-plane
sigma = np.linspace(-2, 2, 400)   # Real part
omega = np.linspace(-2, 2, 400) # Imaginary part
Sigma, Omega = np.meshgrid(sigma, omega)
s = Sigma + 1j * Omega

# Define Laplace transform function F(s)
F = 1 / ((s + 1)**2 + 1)

# Calculate magnitude and phase
magnitude = np.abs(F)
phase = np.angle(F)

# Plot magnitude surface
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(121, projection='3d')
ax.set_zlim(0, 10)
ax.plot_surface(Sigma, Omega, magnitude, cmap='viridis')
ax.set_title('Magnitude |F(s)|')
ax.set_xlabel('Real(s) = a')
ax.set_ylabel('Imag(s) = w')
ax.set_zlabel('|F(s)|')

# Plot phase surface
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(Sigma, Omega, phase, cmap='twilight')
ax2.set_title('Phase arg(F(s))')
ax2.set_xlabel('Real(s) = a')
ax2.set_ylabel('Imag(s) = w')
ax2.set_zlabel('Phase (radians)')

plt.tight_layout()
plt.show()
