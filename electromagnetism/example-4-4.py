import sympy as sp

# Symbols
t = sp.symbols('t', real=True) # Parameter (angle phi)
b = sp.symbols('b', real=True, positive=True) # Radius of ring
h = sp.symbols('h', real=True) # Height of observation point P
eps0 = sp.symbols('epsilon_0')
rho_L = sp.symbols('rho_L')

# 1. Define r_vec(t) - Position on the ring
r_vec_t = sp.Matrix([b * sp.cos(t), b * sp.sin(t), 0])

# 2. Find D_t_r_vec(t) - The Jacobian/Velocity vector
D_t_r_vec = sp.diff(r_vec_t, t)

# 3. Define the distance vector R' from ring to observation point P(0,0,h)
# R' = P - r(t)
P = sp.Matrix([0, 0, h])
R_prime_vec = P - r_vec_t

# 4. Magnitude of R' (distance squared)
R_prime_mag_sq = sp.simplify(R_prime_vec.dot(R_prime_vec))
R_prime_mag = sp.simplify(R_prime_vec.norm())

# 5. Scaling factor (Jacobian magnitude for arc length ds)
# This is sqrt( J.T * J )
D_t_L = sp.simplify(sp.sqrt(D_t_r_vec.dot(D_t_r_vec)))
D_t_L_2 = sp.simplify(sp.sqrt(r_vec_t[0]**2 + r_vec_t[1]**2))


print(D_t_L)
print(D_t_L_2)

integrand = (rho_L * R_prime_vec * D_t_L)/(4*sp.pi*eps0*R_prime_mag**3)

# print("Position vector r(t):")
# sp.pprint(r_vec_t)

# print("\nDerivative D_t_r_vec(t):")
# sp.pprint(D_t_r_vec)

# print(f"\nScaling factor (D_t_L): {D_t_L}")
# print(f"Distance squared (R'^2): {R_prime_mag_sq}")

result = sp.integrate(integrand, (t, 0, sp.pi))

print(result)


