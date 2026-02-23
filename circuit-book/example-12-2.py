import cmath
import math
import sympy as sp

# Apparently, the neutral point is 0v and you don't even need nodal
# analysis. It's as simple as Ia = Va/Za, etc.
def first_attempt():
    z3 = complex(5, -2)
    z4 = complex(10, 8)
    z5 = complex(5, -2)
    z6 = complex(10, 8)
    z7 = complex(10, 8)
    z8 = complex(5, -2)
    z9 = z3 + z4
    z10 = z5 + z6
    z11 = z8 + z7

    v1 = cmath.rect(110, 0)
    v2 = cmath.rect(110, math.radians(-120))
    v0 = cmath.rect(110, math.radians(-240))

    n1 = sp.symbols('n1')

    node1 = sp.Eq( (v1-n1)/z9 + (v2-n1)/z10 + (v0-n1)/z11, 0 )

    solution = sp.solve([node1], (n1), dict=True)

    # sp.pprint(solution[0][n1].evalf())
    print(solution[0][n1].evalf())

    i1 = v1/z9
    i1_ph = cmath.polar(i1)[1]
    
    print(cmath.polar(i1))
    print(math.degrees(i1_ph))

    i2 = v2/z10
    i2_ph = cmath.polar(i2)[1]

    print(cmath.polar(i2))
    print(math.degrees(i2_ph))

    i0 = v0/z11
    i0_ph = cmath.polar(i0)[1]

    print(cmath.polar(i0))
    print(math.degrees(i0_ph))

    



first_attempt()
