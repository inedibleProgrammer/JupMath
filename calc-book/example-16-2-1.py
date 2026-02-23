import sympy as sp

# 1. Setup Symbols
theta = sp.symbols('theta', real=True)

# 2. Define Coordinate Functions (Transformation)
# For the unit circle x^2 + y^2 = 1
g = sp.cos(theta) 
h = sp.sin(theta)

# 3. Calculate Derivatives (D_theta notation)
D_theta_g = sp.diff(g, theta) # dx/dtheta = -sin(theta)
D_theta_h = sp.diff(h, theta) # dy/dtheta = cos(theta)

# 4. Assemble the Jacobian Matrix (J)
# This vector represents the tangent to the curve
jacobian_matrix = sp.Matrix([D_theta_g, D_theta_h])

# 5. Calculate the scaling factor D_theta_L where s = L(theta)
# jtj is J^T * J, which is (dx/dtheta)^2 + (dy/dtheta)^2
jtj = jacobian_matrix.T * jacobian_matrix

# D_theta_L is the magnitude of the Jacobian (the arc length derivative)
D_theta_L = sp.simplify(sp.sqrt(jtj[0]))
scaling_factor = sp.simplify(sp.sqrt(jtj[0]))

# 6. Define the Integrand: (2 + x^2 * y)
# We substitute x = g and y = h, then multiply by the differential ds = D_theta_L * dtheta
integrand = (2 + (g**2 * h)) * scaling_factor

# 7. Integrate over the upper half of the unit circle (0 to pi)
result = sp.integrate(integrand, (theta, 0, sp.pi))

print("Jacobian Matrix (J):")
sp.pprint(jacobian_matrix)
print(jacobian_matrix)
print(f"\nD_theta_g: {D_theta_g}")
print(f"D_theta_h: {D_theta_h}")
print(f"D_theta_L (Scaling Factor): {D_theta_L}")
print(f"\nFinal Integral Result: {result}")


# This stuff works
# import sympy as sp

# s = sp.symbols('s', real=True, positive=True)
# x, y = sp.symbols('x y', real=True)
# theta = sp.symbols('theta', real=True)

# # x = g(theta) = cos(theta)
# x_expr = sp.cos(theta)

# # y = h(theta) = sin(theta)
# y_expr = sp.sin(theta)

# # D_theta(g) = -sin(theta)
# dx_dtheta = sp.diff(x_expr, theta)

# # D_theta(h) = cos(theta)
# dy_dtheta = sp.diff(y_expr, theta)

# # The Jacobian Matrix for a parameterized curve is the vector of partial derivatives
# # with respect to the parameter(s).
# jacobian_matrix = sp.Matrix([dx_dtheta, dy_dtheta])

# # Verification of our previous math:
# jtj = jacobian_matrix.T * jacobian_matrix
# scaling_factor = sp.simplify(sp.sqrt(jtj[0]))

# print("Jacobian Matrix (J):")
# print(jacobian_matrix)

# print("\nJ^T * J:")
# print(jtj)

# print(f"\nScaling factor (ds/dtheta): {scaling_factor}")
