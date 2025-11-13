import sympy as sp


# Define symbols
s = sp.symbols('s')
t = sp.symbols('t', real=True)
# R1, C2 = sp.symbols('R1 C2', positive=True)
N1, N2 = sp.symbols('N1 N2')

R1 = 5
C2 = sp.Rational(1, 10)

z1 = R1
z2 = 1/(s*C2)
# Wolfram Alpha:
# N1 = (10 * s) / (s**2 + 16)
N1_t = 1
N1 = sp.laplace_transform(N1_t, t, s)[0]
# N1 = sp.Rational(1) / s

eq1 = sp.Eq((N1 - N2)/z1 - N2/z2, 0)

# Solve the system
solution = sp.solve([eq1], (N2), dict=True)

N2_s = solution[0][N2]

print(N2_s)


N2_t = sp.inverse_laplace_transform(N2_s, s, t)
print(N2_t)
print(f"RC: {R1 * C2}")

N2_function = sp.lambdify([t], N2_t, "numpy")

print(N2_function(3))
