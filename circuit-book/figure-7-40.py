import sympy as sp

# Define time and symbols
t = sp.symbols('t', real=True, positive=True)
s = sp.symbols('s')
R, C = sp.symbols('R C', positive=True)
Vc = sp.Function('Vc')(t)  # Voltage across capacitor

# Step input u(t) = 1 for t >= 0
u = sp.Heaviside(t)

# Define the KVL differential equation
eq = sp.Eq(R * C * sp.diff(Vc, t) + Vc, u)

eq3 = sp.Eq(R * C * sp.diff(Vc, t) + Vc - u, 0)

eq1 = sp.laplace_transform(eq.lhs, t, s)
eq2 = sp.laplace_transform(eq.rhs, t, s)

eq4 = sp.laplace_transform(eq3.lhs, t, s)

solution2 = sp.simplify(eq4)
solution3 = sp.inverse_laplace_transform(solution2, s, t)
# print(solution2)
print(solution3)

#print(eq1)
# print(eq2)

# Solve the ODE with initial condition Vc(0) = 0
solution = sp.dsolve(eq, Vc, ics={Vc.subs(t, 0): 0})

# Display result
# print("Step response Vc(t) =")
# sp.pprint(solution.rhs)
print(solution)
