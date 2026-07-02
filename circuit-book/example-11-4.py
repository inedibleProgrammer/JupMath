import cmath
import math
import sympy as sp


i0 = complex(4, 0)

z1 = complex(20, 0)
z2 = complex(0, 10)
z3 = complex(0, -5)

v4 = cmath.rect(60, math.radians(30))

n3 = v4

y1 = 1/z1
y2 = 1/z2
y3 = 1/z3

n2 = (-(y3 * n3) - i0) / (-y2-y3)

print(n2)


i3 = (n2 - n3)/z3

i3_mag, i3_phase = cmath.polar(i3)

print(i3_mag, math.degrees(i3_phase))

