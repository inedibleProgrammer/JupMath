# A car of mass m is on an icy driveway inclined at an angle u as in
# Figure 5.11a.

# I took numbers from a different problem and put them here and
# verified that it works
import math
from scipy.optimize import fsolve

# m = 1000
# t1 = 45
# t2 = 90 - t1
# t1r = math.radians(t1)
# t2r = math.radians(t2)
# g = 9.80

# def first_solution():
#     denom = (math.sin(t1r) + (math.cos(t1r)*math.sin(t2r)/math.cos(t2r)))

#     a = g/denom
#     Fnorm = m * a * math.cos(t1r)/math.cos(t2r)

#     print(a)
#     print(Fnorm)



def second_solution():

    m = 1000
    t1 = -60
    t2 = 30
    t1r = math.radians(t1)
    t2r = math.radians(t2)
    g = 9.80

    def equations(vars):
        a, Fn = vars
        eq1 = m*a*math.cos(t1r) - Fn*math.cos(t2r)
        eq2 = m*a*math.sin(t1r) + m*g - Fn*math.sin(t2r)
        return [eq1, eq2]

    a, Fn = fsolve(equations, (6, 6000))

    print(a, Fn)

second_solution()

