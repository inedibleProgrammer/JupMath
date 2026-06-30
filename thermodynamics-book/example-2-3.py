import numpy as np


def pounds_to_kg(pounds):
    return pounds * 0.453592

def btu_per_lb_to_joule_per_kg(btu_lb):
    return btu_lb * 2326

def ft3_to_m3(ft3):
    return ft3 * 0.0283168

def ft_per_s2_to_m_per_s2(ft_per_s2):
    return ft_per_s2 * 0.3048

def lbf_per_in2_to_pa(lbf_per_in2):
    return lbf_per_in2 * 6894.76

def ft2_to_m2(ft2):
    return ft2 * 0.092903

A_piston_m2 = ft2_to_m2(1)
m_air_kg = pounds_to_kg(0.6)
m_piston_kg = pounds_to_kg(100)
du_air_joule_per_kg = btu_per_lb_to_joule_per_kg(18)
P_atm_pa = lbf_per_in2_to_pa(14.7)

dV_m3 = ft3_to_m3(1.6)
g_m_per_s2 = ft_per_s2_to_m_per_s2(32)

def part_a():
    # Balance the forces and solve
    P_air_pa = (A_piston_m2 * P_atm_pa + m_piston_kg * g_m_per_s2)/(A_piston_m2)

    # dV_m3 is the result of the integral and the difference
    W_air_surroundings = P_air_pa * dV_m3

    # Specific internal energy to normie internal energy
    dU_joules = du_air_joule_per_kg * m_air_kg

    dQ_joules = dU_joules + W_air_surroundings
    print(dQ_joules)


def part_b():
    pass


part_a()

