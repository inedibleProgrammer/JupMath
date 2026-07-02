import sympy as sp

def first():
    # Symbols
    tau, t, ti, a = sp.symbols("tau t ti a")

    # Function f(tau)
    f = sp.Function("f")

    # Left-hand side: integral of a dτ from ti to t
    acceleration_lhs = sp.integrate(a, (tau, ti, t))

    # Right-hand side: integral of f''(tau) dτ from ti to t
    acceleration_rhs = sp.integrate(sp.diff(f(tau), tau, 2), (tau, ti, t))

    # Equation lhs = rhs
    velocity = sp.Eq(acceleration_lhs, acceleration_rhs)

    # Plug in ti = 0 and a = g = -9.81
    velocity_subbed = velocity.subs({
        ti: 0,
        a: -9.81,
        f(0): 0
    })

    print("lhs =", acceleration_lhs)
    print("rhs =", acceleration_rhs)
    print("velocity =", velocity)

    print("velocity subbed with ti=0 and a=-9.81:")
    print(velocity_subbed)

    #print(velocity_subbed.lhs)
    #print(velocity_subbed.rhs)
    velocity_lhs = sp.integrate(velocity_subbed.lhs, (tau, ti, t))
    velocity_rhs = sp.integrate(velocity_subbed.rhs, (tau, ti, t))

    position = sp.Eq(velocity_lhs, velocity_rhs)

    position_subbed = position.subs({
        ti: 0,
        a: -9.81,
        f(0): 0
    })

    print(velocity_lhs)
    print(velocity_rhs)
    print("Position subbed: ")
    print(position_subbed)

def second():
    # Symbols
    tau, t, ti, a = sp.symbols("tau t ti a")

    # Function f
    f = sp.Function("f")
    f_prime = sp.diff(f(t), t)
    f_double_prime = sp.diff(f_prime, t)

    # -----------------------------
    # Step 1: integrate acceleration
    # -----------------------------

    # Integral of a dτ from ti to t
    acceleration_lhs = sp.integrate(a, (tau, ti, t))

    # Integral of f''(τ) dτ from ti to t
    # acceleration_rhs = sp.integrate(sp.diff(f(tau), tau, 2), (tau, ti, t))
    acceleration_rhs = sp.integrate(f_double_prime, (tau, ti, t))

    velocity_eq = sp.Eq(acceleration_lhs, acceleration_rhs)

    print("After first integration:")
    print(velocity_eq)

    # Solve this equation for f'(t)
    velocity_expr = sp.solve(velocity_eq, sp.diff(f(t), t))[0]

    velocity_eq_solved = sp.Eq(sp.diff(f(t), t), velocity_expr)

    print("\nVelocity equation:")
    print(velocity_eq_solved)

    # -----------------------------
    # Step 2: integrate velocity
    # -----------------------------

    # To integrate velocity from ti to t, rewrite velocity as a function of tau.
    # Replace t with tau in the velocity expression.
    velocity_tau = velocity_expr.subs(t, tau)

    # Integral of f'(τ) dτ from ti to t
    position_lhs = sp.integrate(sp.diff(f(tau), tau), (tau, ti, t))

    # Integral of velocity(τ) dτ from ti to t
    position_rhs = sp.integrate(velocity_tau, (tau, ti, t))

    position_eq = sp.Eq(position_lhs, position_rhs)

    print("\nAfter second integration:")
    print(position_eq)

    # Solve for f(t)
    position_expr = sp.solve(position_eq, f(t))[0]

    position_eq_solved = sp.Eq(f(t), sp.simplify(position_expr))

    print("\nPosition equation:")
    print(position_eq_solved)

    # -----------------------------
    # Substitute ti = 0 and a = -9.81
    # -----------------------------

    velocity_gravity = velocity_eq_solved.subs({
        ti: 0,
        a: -9.81
    })

    position_gravity = position_eq_solved.subs({
        ti: 0,
        a: -9.81
    })

    print("\nVelocity with ti=0 and a=-9.81:")
    print(velocity_gravity)

    print("\nPosition with ti=0 and a=-9.81:")
    print(position_gravity)

def second_with_tf():
    # Symbols
    t, ti, tf, a = sp.symbols("t ti tf a")

    # Function
    f = sp.Function("f")

    # Derivatives with respect to t
    f_prime = sp.diff(f(t), t)
    f_double_prime = sp.diff(f(t), t, 2)

    # -----------------------------
    # Step 1: integrate acceleration
    # -----------------------------

    acceleration_lhs = sp.integrate(a, (t, ti, tf))
    acceleration_rhs = sp.integrate(f_double_prime, (t, ti, tf))

    velocity_eq = sp.Eq(acceleration_lhs, acceleration_rhs)

    print("After first integration, bounded ti to tf:")
    print(velocity_eq)

    # Replace tf with t so the final time is called t
    velocity_eq = velocity_eq.subs(tf, t)

    print("\nAfter replacing tf with t:")
    print(velocity_eq)

    # Solve for f'(t)
    velocity_expr = sp.solve(velocity_eq, sp.diff(f(t), t))[0]
    velocity_eq_solved = sp.Eq(sp.diff(f(t), t), velocity_expr)

    print("\nVelocity equation:")
    print(velocity_eq_solved)

    # -----------------------------
    # Step 2: integrate velocity
    # -----------------------------

    # For the second definite integral, again integrate from ti to tf
    # using t as the integration variable.
    position_lhs = sp.integrate(sp.diff(f(t), t), (t, ti, tf))

    # velocity_expr is written in terms of t, so this is okay
    position_rhs = sp.integrate(velocity_expr, (t, ti, tf))

    position_eq = sp.Eq(position_lhs, position_rhs)

    print("\nAfter second integration, bounded ti to tf:")
    print(position_eq)

    # Replace tf with t
    position_eq = position_eq.subs(tf, t)

    print("\nAfter replacing tf with t:")
    print(position_eq)

    # Solve for f(t)
    position_expr = sp.solve(position_eq, f(t))[0]
    position_eq_solved = sp.Eq(f(t), sp.simplify(position_expr))

    print("\nPosition equation:")
    print(position_eq_solved)

    # Gravity case
    velocity_gravity = velocity_eq_solved.subs({
        ti: 0,
        a: -9.81
    })

    position_gravity = position_eq_solved.subs({
        ti: 0,
        a: -9.81
    })

    print("\nVelocity with ti=0 and a=-9.81:")
    print(velocity_gravity)

    print("\nPosition with ti=0 and a=-9.81:")
    print(position_gravity)

# second()
second_with_tf()

