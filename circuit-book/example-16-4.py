import sympy as sp

# Define symbols
s, t = sp.symbols('s t')
R1, R3, C2, L4 = sp.symbols('R1 R3 C2 L4', positive=True)
N2, N3 = sp.symbols('N2 N3')

z1 = R1
z2 = 1/(s*C2)
z3 = R3
z4 = s*L4
N1 = 1/s

eq1 = sp.Eq((N1 - N2)/z1 - N2/z2 - (N2-N3)/z3, 0)
eq2 = sp.Eq((N2 - N3)/z3 - N3/z4, 0)

# Solve the system
solution = sp.solve([eq1, eq2], (N2, N3), dict=True)
sp.pprint(solution)
print(solution)
print(solution[0])
# print(solution[1])


# Extract N3 from the solution
N3_s = solution[0][N3]

# Define numerical values
values = {R1: 1, R3: 5, C2: 1/3, L4: 1}

# Substitute values into Laplace-domain solution
N3_s_numeric = N3_s.subs(values)

print("N3(s) with values substituted:")
sp.pprint(N3_s_numeric)

# Show symbolic Laplace-domain result
print("\nN3(s) =")
sp.pprint(N3_s)

# Compute inverse Laplace transform
N3_t = sp.inverse_laplace_transform(N3_s_numeric, s, t)
print("\nInverse Laplace Transform of N3(t) =")
sp.pprint(N3_t)
print(N3_t)
