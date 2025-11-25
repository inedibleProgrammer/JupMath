# https://www.circuitbread.com/tutorials/operational-amplifier-op-amp-practice-problems

# V1 N004 0 0.5
# R1 N001 N004 10k
# R2 N002 N001 25k
# V2 N003 N005 15
# V3 N005 N006 15
# XU1 0 N001 N003 N006 N002 level1 Avol=1Meg GBW=10Meg Vos=0 En=0 Enk=0 In=0 Ink=0 Rin=500Meg


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import sympy as sp


N2, N3, N4 = sp.symbols("N2 N3 N4")





