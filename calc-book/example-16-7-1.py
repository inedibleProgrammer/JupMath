def using_manual():
    import sympy as sp

    x, y, z = sp.symbols('x y z', real=True)
    phi, theta = sp.symbols('phi theta', real=True)

    f = x**2  # Your original function f(x,y,z)

    # 1. Define r(phi, theta)
    r_vec = sp.Matrix([
        sp.sin(phi) * sp.cos(theta),
        sp.sin(phi) * sp.sin(theta),
        sp.cos(phi)
    ])

    # This effectively gives you f(r_vec)
    f_param = f.subs({
        x: r_vec[0],
        y: r_vec[1],
        z: r_vec[2]
    })

    print("f param")
    print(f_param)

    D_phi_r_vec = sp.diff(r_vec, phi)
    D_theta_r_vec = sp.diff(r_vec, theta)

    # 2. Cross product (returns a vector)
    normal_vec = D_phi_r_vec.cross(D_theta_r_vec)

    # 3. Scaling factor (the magnitude of the cross product)
    # This is equivalent to your sqrt(det(J.T * J)) method
    scaling_factor = sp.simplify(normal_vec.norm())

    print(f"Normal Vector: {normal_vec}")
    print(f"Scaling factor (dS): {scaling_factor}") # Should be sin(phi)

    integrand = f_param * scaling_factor

    result = sp.integrate(integrand, (phi, 0, sp.pi), (theta, 0, 2*sp.pi))
    print("result: \n")
    print(result)

def using_jacobian():
    import sympy as sp

    phi, theta = sp.symbols('phi theta', real=True)

    # 1. Define r(phi, theta)
    r = sp.Matrix([
        sp.sin(phi) * sp.cos(theta),
        sp.sin(phi) * sp.sin(theta),
        sp.cos(phi)
    ])

    # 2. Calculate the Jacobian Matrix J
    J = r.jacobian([phi, theta])

    # 3. Calculate the scaling factor: sqrt(det(J.T * J))
    scaling_factor = sp.simplify(sp.sqrt((J.T * J).det()))

    # 4. Set up the integral for x^2 dS
    f = (sp.sin(phi) * sp.cos(theta))**2
    integrand = f * scaling_factor

    # 5. Integrate from 0 to pi (phi) and 0 to 2pi (theta)
    result = sp.integrate(integrand, (phi, 0, sp.pi), (theta, 0, 2*sp.pi))

    print(f"Scaling Factor: {scaling_factor}")
    print(f"Final Result: {result}")

def using_metric_determinant():
    import sympy as sp

    # 1. Define symbols
    phi, theta = sp.symbols('phi theta', real=True)

    # 2. Define the parametric vector r(phi, theta)
    r = sp.Matrix([
        sp.sin(phi) * sp.cos(theta),
        sp.sin(phi) * sp.sin(theta),
        sp.cos(phi)
    ])

    # 3. Calculate tangent vectors (partial derivatives)
    r_phi = sp.diff(r, phi)
    r_theta = sp.diff(r, theta)

    # 4. Calculate the Metric Tensor g
    # g_11 g_12
    # g_21 g_22
    g11 = r_phi.dot(r_phi)
    g12 = r_phi.dot(r_theta)
    g21 = r_theta.dot(r_phi)
    g22 = r_theta.dot(r_theta)

    g = sp.Matrix([[g11, g12], [g21, g22]])

    # 5. Calculate the square root of the metric determinant (sqrt(det(g)))
    # This is the scaling factor for dS
    metric_det = g.det()
    sqrt_g = sp.simplify(sp.sqrt(metric_det)) 

    # 6. Define the function f(x, y, z) = x^2 in terms of parameters
    f = (sp.sin(phi) * sp.cos(theta))**2

    # 7. Set up and solve the integral: Integral of f * sqrt_g d_phi d_theta
    integrand = f * sqrt_g
    result = sp.integrate(integrand, (phi, 0, sp.pi), (theta, 0, 2*sp.pi))

    print(f"Scaling factor (sqrt(g)): {sqrt_g}")
    print(f"Final Integral Result: {result}")


# using_jacobian()
using_manual()
