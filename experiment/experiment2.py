import sympy as sp
import math
from pprint import pprint

# a = 
# [
#     {
#         "t": 0,
#         "s": 0,
#         "B_deg": 0,
#         "e_t_uvec": (-0.0, 1.0),
#         "e_n_uvec": (-1.0, -0.0),
#     },
#     {
#         "t": 1,
#         "s": 30,
#         "B_deg": 30,
#         "B_rad": math.deg2rad(B_deg)
#         "e_t_uvec": (-0.5, 0.866),
#         "e_n_uvec": (-0.866, -0.5),
#     },
# ]

# table = {
#     "t": [0, 1, 2, 3],
#     "s": [0, 30, 45, 60],
#     "B_deg": [0, 30, 45, 60],
# }

def make_row(t, B_deg):
    B_rad = math.radians(B_deg)
    rho = 1

    return {
        "t": t,
        "Beta_deg": B_deg,
        "Beta_rad": B_rad,
        "s": rho*B_rad,
        # "dBeta":
        # "e_t_uvec": (-math.sin(B_rad), math.cos(B_rad)),
        # "e_n_uvec": (-math.cos(B_rad), -math.sin(B_rad)),
    }

rows = [
    make_row(t=0, B_deg=0),
    make_row(t=1, B_deg=30),
    make_row(t=2, B_deg=45),
    make_row(t=3, B_deg=60),
]


pprint(rows)
