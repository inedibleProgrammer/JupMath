import sympy as sp

x, y = sp.symbols('x y', real=True)
t = sp.symbols('t', real=True)

P_xy = x**2
Q_xy = -x*y

f_t = sp.cos(t)
g_t = sp.sin(t)

F_vec_xy = sp.Matrix([P_xy, Q_xy])
r_vec_t = sp.Matrix([f_t, g_t])

D_f_t = sp.diff(f_t, t)
D_g_t = sp.diff(g_t, t)

# Calculate the Jacobian Matrix (velocity vector r'(t))
jacobian_matrix = sp.Matrix([D_f_t, D_g_t])

# --- SOLUTION ---
# substitute r_vec_t into F_vec_xy
# We map x to r_vec_t[0] (which is f_t) and y to r_vec_t[1] (which is g_t)
F_vec_r_t = F_vec_xy.subs({x: r_vec_t[0], y: r_vec_t[1]})

# Calculate F(r(t)) dot r'(t)
work_integrand = F_vec_r_t.dot(jacobian_matrix)

# Integrate from 0 to pi/2 for the quarter circle
work_done = sp.integrate(work_integrand, (t, 0, sp.pi/2))

print("F evaluated at r(t):")
sp.pprint(F_vec_r_t)
print(f"\nIntegrand (F dot r'): {sp.simplify(work_integrand)}")
print(f"Total Work Done: {work_done}")
