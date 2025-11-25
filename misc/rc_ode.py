import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import sympy as sp

# --- 1. Symbolic Setup (Using SymPy) ---
# Define symbolic variables for the components and voltages
V_N1, V_N2, R1, C = sp.symbols('V_N1, V_N2, R1, C')
# Define the derivative of V_N2 (the term we need to solve for)
V_N2_prime = sp.Symbol("V_N2_prime")

# Your differential equation (set equal to zero)
# Equation: (V(N1) - V(N2))/R1 - V'(N2)*C = 0
equation = (V_N1 - V_N2) / R1 - V_N2_prime * C

print("--- Symbolic Derivation ---")
print(f"Original Equation (Equation = 0): {equation}")

# Solve the equation for the derivative V_N2_prime
# The result is a list of solutions, so we take the first element [0]
solution_expr = sp.solve(equation, V_N2_prime)[0]

print(f"Solved for V'(N2) (Rate of Change): {solution_expr}")

# --- 2. Create Numerical Function ---
# SymPy's lambdify converts the symbolic expression into a fast NumPy function.
# The inputs to the final function must be in the order required by solve_ivp: (t, Y)
# Y contains V_N2 (the state variable).
# We also need to define the parameters (V_N1, R1, C) which will be constant.
# The `modules='numpy'` ensures the resulting function is NumPy-compatible.
ode_func_numeric = sp.lambdify(
    (V_N2, V_N1, R1, C), # Variables in the symbolic solution
    solution_expr,       # The symbolic expression V_N2_prime
    modules='numpy'      # Use NumPy for fast computation
)

# --- 3. Numerical Parameters for Simulation ---
P_V_N1 = 5.0      # V(N1): Source Voltage (Volts)
P_R1 = 1000.0     # R1: Resistance (Ohms)
P_C = 100e-6      # C: Capacitance (Farads, 100 µF)
P_tau = P_R1 * P_C

# Time span and initial conditions
t_span = (0, 5 * P_tau)
V_initial = [0.0] # V(N2): Initial capacitor voltage

# --- 4. ODE Function for solve_ivp ---
# solve_ivp requires a function with the signature f(t, Y)
def rc_ode_system(t, Y):
    # Y is the state vector, Y[0] is the current capacitor voltage (V_N2)
    V_C = Y[0]

    # Call the SymPy-generated numerical function
    # Note: t is ignored by our equation, but passed by solve_ivp
    dV_C_dt = ode_func_numeric(V_C, P_V_N1, P_R1, P_C)

    return [dV_C_dt]

# --- 5. Solving and Plotting ---
solution = solve_ivp(
    rc_ode_system,
    t_span,
    V_initial,
    t_eval=np.linspace(t_span[0], t_span[1], 500)
)

time = solution.t
V_C = solution.y[0]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, V_C, label=r'$V_{C}$ (Voltage across $V(N2)$)', linewidth=3, color='forestgreen')
plt.axhline(P_V_N1, color='r', linestyle=':', label=f'Source Voltage ({P_V_N1}V)')
plt.title('Single RC Circuit Solved via SymPy and solve_ivp', fontsize=16)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Capacitor Voltage (V)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='dotted', alpha=0.6)
plt.show()

print(f"\nFinal V(N2) voltage after {t_span[1]:.3f}s: {V_C[-1]:.3f} V")
