# import sympy as sp

# t = sp.symbols('t', real=True)
# s = sp.symbols('s', complex=True)
# R, C, Vm, w = sp.symbols('R C Vm w', positive=True)
# N1, N2 = sp.symbols('N1 N2')

# z1 = R
# z2 = 1/(s*C)

# Vs = Vm * sp.cos(w*t)
# Vs_s = sp.laplace_transform(Vs, t, s)[0]
# N1 = Vs_s

# eq1 = sp.Eq((N1 - N2)/z1 - N2/z2, 0)

# solution = sp.solve([eq1], (N2), dict=True)

# N2_s = solution[0][N2]

# H_s = N2_s/Vs_s

# H_s_j = sp.simplify(H_s.subs(s, sp.I * w))


# print(Vs_s)
# print(eq1)
# print(solution[0][N2])
# print(H_s_j)


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
t = sp.symbols('t', real=True)
s = sp.symbols('s', complex=True)
R, C, Vm, w = sp.symbols('R C Vm w', positive=True)
N1, N2 = sp.symbols('N1 N2')

# Impedances
z1 = R
z2 = 1/(s*C)

# Input voltage in time domain
Vs = Vm * sp.cos(w * t)

# Laplace transform of input
Vs_s = sp.laplace_transform(Vs, t, s, noconds=True)

# Source node voltage in Laplace domain
N1 = Vs_s

# KCL equation
eq1 = sp.Eq((N1 - N2)/z1 - N2/z2, 0)

# Solve for N2(s)
solution = sp.solve(eq1, N2, dict=True)
N2_s = solution[0][N2]

# Transfer function: H(s) = N2(s) / Vs(s)
H_s = sp.simplify(N2_s / Vs_s)

# Substitute s = jw
H_s_j = H_s.subs(s, sp.I * w)
H_s_j = sp.simplify(H_s_j)

# Display results
print("Laplace Transform of input Vs(t):")
sp.pprint(Vs_s)
print("\nEquation:")
sp.pprint(eq1)
print("\nSolution for N2(s):")
sp.pprint(N2_s)
print("\nTransfer Function H(s):")
sp.pprint(H_s)
print("\nFrequency Response H(jw):")
sp.pprint(H_s_j)

print(H_s_j)

# Just use random values for graphing
H_s_j_withNums = H_s_j.subs({R: 1000, C: 1E-6})

print(H_s_j_withNums)

# Create functions for magnitude and phase
H_mag_func = sp.lambdify(sp.symbols('w'), sp.Abs(H_s_j_withNums), modules='numpy')
H_phase_func = sp.lambdify(sp.symbols('w'), sp.arg(H_s_j_withNums), modules='numpy')

# Define frequency range (e.g., 0.1 to 1000 rad/s)
# w_vals = np.logspace(-1, 3, 500)  # 0.1 to 1000 rad/s
w_vals = np.linspace(0, 10000, 2000)  # 0.1 to 1000 rad/s
mag_vals = H_mag_func(w_vals)
phase_vals = H_phase_func(w_vals)


plt.figure(figsize=(10, 6))

# Magnitude plot
plt.subplot(2, 1, 1)
# plt.semilogx(w_vals, 20 * np.log10(np.abs(mag_vals)))
plt.plot(w_vals, mag_vals)
plt.title('Bode Plot of H(jw)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both')

# # Phase plot
plt.subplot(2, 1, 2)
# # plt.semilogx(w_vals, np.degrees(phase_vals))
plt.plot(w_vals, phase_vals)
plt.xlabel('Frequency w (rad/s)')
plt.ylabel('Phase (degrees)')
plt.grid(True, which='both')

plt.tight_layout()
plt.show()
