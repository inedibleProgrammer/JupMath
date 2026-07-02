import sympy as sp
import math

def get_wave_number_1(lambda_):
    return (2*math.pi)/lambda_

def get_wave_number_2(omega, velocity):
    return omega/velocity


f_Hz = 2.0
A_m = 0.075
v_m_per_s = 12.0

# Part A:
# Find omega, T, lambda, wave number k


omega_rad_per_s = 2 * math.pi * f_Hz
T_s = 1/f_Hz
lambda_m = v_m_per_s/f_Hz
k1 = get_wave_number_1(lambda_m)
k2 = get_wave_number_2(omega_rad_per_s, v_m_per_s)
print(omega_rad_per_s, T_s, lambda_m, k1, k2)

# Part B:

def wave_function(x, t):
    term1 = x/lambda_m
    term2 = t/T_s
    twopi = 2 * math.pi
    return A_m * math.cos(twopi * (term1 - term2))

# This shows that the string is at rest?
print(wave_function(0, 0))

# This shows the -ve cosine form at x=3
print(wave_function(3, 0))


