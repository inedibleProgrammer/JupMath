# from sympy import symbols, Function, laplace_transform
import sympy as sp

t = sp.symbols('t', real=True)
s = sp.symbols('s', complex=True)
R, C = sp.symbols('R C', positive=True)
Vs = sp.Function('Vs')(t)
# Vs_t = sp.exp(-t)
u = sp.Heaviside(t)
Vc = sp.Function('Vc')(t)

eq = sp.Eq((Vs * u)/R - C*sp.diff(t),0)

# r = sp.laplace_transform(y.diff(t,2)+2*y.diff(t,1)+3*y,t,s)
r = sp.laplace_transform(eq.lhs, t, s)

# substitution dictionary with zero-initial condition
# sd = {y.diff(t, i).subs(t, 0): 0 for i in range(2)}

sd = {
    Vc.subs(t, 0): 0,
    Vc.diff(t).subs(t, 0): 0,
    R: 1,
    C: 1,
    # Vs: sp.exp(-t),
}

print(sd)
print(r)
print(r[0])
q0 = r[0].subs(sd)
print(q0)

q1 = sp.inverse_laplace_transform(q0, s, t)
print(q1)

q2 = sp.inverse_laplace_transform(r[0], s, t)
print(q2)
