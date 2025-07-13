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

