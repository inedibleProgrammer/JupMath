
def first_attempt():
    import sympy as sp

    x, y, z, theta, rho, eps = sp.symbols('x y z theta rho eps', real=True)
    r, a, h = sp.symbols('r a h', real=True, positive=True)

    r_vec = sp.Matrix([
        r*sp.cos(theta),
        r*sp.sin(theta),
        0
    ])

    print(r_vec)
    print(' ')

    D_r_r_vec = sp.diff(r_vec, r)
    D_theta_r_vec = sp.diff(r_vec, theta)

    print(D_r_r_vec)
    print(D_theta_r_vec)
    print(' ')

    normal_vec = D_r_r_vec.cross(D_theta_r_vec)
    scaling_factor = sp.simplify(normal_vec.norm())

    print(normal_vec)
    print(scaling_factor)
    print(' ')

    P_vec = sp.Matrix([
        0,
        0,
        h
    ])

    R_prime_vec = P_vec - r_vec
    R_prime_vec_mag = sp.simplify(R_prime_vec.norm())
    print(R_prime_vec)
    print(R_prime_vec_mag)
    print(' ')

    integrand = sp.simplify((R_prime_vec / R_prime_vec_mag**3) * scaling_factor)
    integral_result = integrand.integrate((r, 0, a), (theta, 0, 2*sp.pi))
    result = integral_result * (rho/(4*sp.pi*eps))
    print(result)
    print(' ')

    E_infinite_sheet = result.limit(a, sp.oo)
    print(E_infinite_sheet)


first_attempt()
