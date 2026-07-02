import sympy as sp
import math
from pprint import pprint
import matplotlib.pyplot as plt

t_col = [0, 1, 2, 3]
r_vec = [
    sp.Matrix([1, 0]),
    sp.Matrix([3**0.5/2, 0.5]),
    sp.Matrix([2**0.5/2, 2**0.5/2]),
    sp.Matrix([0.5, 3**0.5/2]),
]
dr_vec = [sp.Matrix([0, 0])]
Beta_deg_col = [0, 30, 45, 60]
Beta_rad_col = []
s_col = [0]
dBeta_rad_col = [0]
rho = 1


for t in t_vals:
    Beta_rad_col.append(math.radians(Beta_deg_col[t]))

    if(t > 0):
        s_col.append(Beta_rad_col[t])
        dBeta_rad_col.append(Beta_rad_col[t] - Beta_rad_col[t-1])
        dr_vec.append(r_vec[t] - r_vec[t-1])

# print(Beta_rad_col)
# print(s_col)
print(dBeta_rad_col)
pprint(dr_vec)


# Plot r_vec as a curve
x_vals = [float(r[0]) for r in r_vec]
y_vals = [float(r[1]) for r in r_vec]

plt.plot(x_vals, y_vals, marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("r_vec curve")
plt.axis("equal")
plt.grid(True)
plt.show()


# Notes
# e_t_uvec == v_uvec
