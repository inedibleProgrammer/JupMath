import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import sympy as sp

vref = 3.3
N = 12
lsb = vref / (2**N)
lsb_half = lsb/2


# V1 N1 0 PULSE(0 1.65 0 1ps 1ns 1 0 1)
# R1 N2 N1 200
# C2 N2 0 1000p
# R3 N3 N2 5000
# C4 N3 0 4p



N2, N3 = sp.symbols("N2 N3")
N2_dot, N3_dot = sp.symbols("N2_dot N3_dot")


radc = 5E3
cadc = 4E-12

R3 = radc
C4 = cadc
RC_adc = R3 * C4


R1 = 200
C2 = 1000E-12 # 1000pF
RC_source = R1 * C2

print(f"RC_adc: {RC_adc}, 5*RC_adc: {5*RC_adc}")
print(f"RC_source: {RC_source}, 5*RC_source: {5*RC_source}")

N1 = 1.65

eq1 = sp.Eq((N1-N2)/R1 - C2*N2_dot - (N2-N3)/R3, 0)
eq2 = sp.Eq((N2-N3)/R3 - C4*N3_dot, 0)

solution = sp.solve([eq1, eq2], (N2_dot, N3_dot), dict=True)
print(solution[0][N2_dot])
print(solution[0][N3_dot])

N2_dot_sln = solution[0][N2_dot]
N3_dot_sln = solution[0][N3_dot]


ode_func_numeric = sp.lambdify(
    (N2, N3),
    (N2_dot_sln, N3_dot_sln),
    modules='numpy'
)


V0 = [3.3, 0.0]  # [N2_initial, N3_initial]
t_span = (0, 0.000001) # Time span for the simulation (0 to 1.0 seconds)


def rc_ode_system(t, Y):
    V_N2, V_N3 = Y

    derivs = ode_func_numeric(V_N2, V_N3)

    return np.array(derivs)



solution = solve_ivp(
    rc_ode_system,
    t_span,
    V0,
    t_eval=np.linspace(t_span[0], t_span[1], 1000)
)

time = solution.t
V_N2 = solution.y[0]
V_N3 = solution.y[1]

N1_high = N1 + lsb_half
N1_low = N1 - lsb_half


print("math done")

plt.plot(time, V_N2)
plt.plot(time, V_N3)
plt.show()

