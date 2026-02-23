from sympy import symbols, Eq, linsolve, Matrix

# 1. Define your 6 variables
x1, x2, x3, x4, x5, x6 = symbols('x1 x2 x3 x4 x5 x6')

# 2. Define the equations based on your matrix rows
# Row 1: 1x1 + 5x2 - 5x3 - 4x4 + 1x5 - 9x6 = -2
eq1 = Eq(x1 + 5*x2 - 5*x3 - 4*x4 + x5 - 9*x6, -2)

# Row 2: 1x4 + 3x5 - 8x6 = 3
eq2 = Eq(x4 + 3*x5 - 8*x6, 3)

# Row 3: 1x5 + 5x6 = -5
eq3 = Eq(x5 + 5*x6, -5)

# 3. Solve the system
sol = linsolve([eq1, eq2, eq3], (x1, x2, x3, x4, x5, x6))

print("General Solution (x1, x2, x3, x4, x5, x6):")
print(sol)
