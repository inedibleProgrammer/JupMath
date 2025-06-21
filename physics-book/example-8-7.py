import math
from scipy.optimize import fsolve
from scipy.integrate import quad

# Acceleration: 3.2333 m/s/s
# Normal force: 25.4611 N
# Net force along ramp: 9.700 N
# Final velocity at bottom of ramp: 2.543 m/s
def first_solution():

    m = 3
    t1 = 30
    t2 = -t1
    t3 = t2
    t4 = 90 - abs(t2)
    t5 = 180 - abs(t3)
    t6 = -90
    t1r = math.radians(t1)
    t2r = math.radians(t2)
    t3r = math.radians(t3)
    t4r = math.radians(t4)
    t5r = math.radians(t5)
    t6r = math.radians(t6)
    Ff = 5
    g = 9.80
    yi = 0.5
    yf = 0

    def force_equations(vars):
        a, Fn = vars
        eq1 = m*a*math.cos(t2r) - Ff*math.cos(t5r) - Fn*math.cos(t4r)
        eq2 = m*a*math.sin(t2r) - Ff*math.sin(t5r) - m*g*math.sin(t6r) - Fn*math.sin(t4r)
        return [eq1, eq2]

    a, Fn = fsolve(force_equations, (6, 20))

    def pos_equation(vars):
        t = vars
        eq1 = 0.5*a*math.sin(t2r) * t * t + yi
        return eq1

    tf = fsolve(pos_equation, 2)

    def vel_equation(t):
        return a*math.sin(t2r) * t

    vyf = vel_equation(tf)
    vmag = vyf/math.sin(t2r)

    # 3.2333333333333347 25.4611468712625 [0.78648376] [2.54296415]
    print(a, Fn, tf, vmag)

first_solution()
