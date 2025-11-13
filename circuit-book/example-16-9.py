import sympy as sp

# Define symbols
s, t = sp.symbols('s t')
# R1, R3, C2, L4 = sp.symbols('R1 R3 C2 L4', positive=True)
N2, N3 = sp.symbols('N2 N3')


r1 = 1
r2 = 1
l3 = 1
r4 = 1


z1 = r1
z2 = r2
z3 = l3 * s
z4 = r4
# N1 = 1/s
N1 = (8*s)/(s**2 + 4)

eq1 = sp.Eq((N1 - N2)/z1 - N2/z2 - (N2-N3)/z3, 0)

eq1 = sp.Eq((N1 - N2)/z1 - N2/z2 - (N2-N3)/z3, 0)
eq2 = sp.Eq((N2 - N3)/z3 - N3/z4, 0)

solution = sp.solve([eq1, eq2], (N2, N3), dict=True)


N3_s = solution[0][N3]
print(N3_s)


N3_t = sp.inverse_laplace_transform(N3_s, s, t)
print(N3_t)


