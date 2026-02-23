# Problem on falstad.com/circuit
# $ 1 0.000005 10.20027730826997 34 5 43 5e-11
# r -32 96 96 96 0 5
# r 96 96 224 96 0 8
# r 96 160 32 160 0 1
# r 96 160 160 160 0 1
# r -32 224 224 224 0 10
# v 32 160 -32 160 0 0 40 12 0 0 0.5
# v 160 160 224 160 0 0 40 9 0 0 0.5
# w 224 96 224 160 0
# w 224 160 224 224 0
# w -32 160 -32 224 0
# w -32 160 -32 96 0
# w 96 160 96 96 0

import sympy as sp



r1 = 5
r2 = 1
r3 = 10
r4 = 1
r5 = 8
v0 = 12
v6 = 9


i1, i2, i3, i4, i5 = sp.symbols('i1, i2, i3, i4, i5')

l1 = sp.Eq( i5*r5 + v6 + i4*r4, 0 )
l2 = sp.Eq( -i1*r1 - i2*r2 - v0, 0 )
l3 = sp.Eq( v0 + i2*r2 - i4*r4 -v6 + i3*r3, 0 )
n0 = sp.Eq( i1 - i2 + i3, 0 )
n2 = sp.Eq( i5 - i4 - i3, 0 )

solution = sp.solve([l1, l2, l3, n0, n2], (i1, i2, i3, i4, i5), dict=True)


# -1.97156398104265
# -2.14218009478673
# -0.170616113744076
# -0.848341232227488
# -1.01895734597156

sp.pprint(solution[0][i1].evalf())
sp.pprint(solution[0][i2].evalf())
sp.pprint(solution[0][i3].evalf())
sp.pprint(solution[0][i4].evalf())
sp.pprint(solution[0][i5].evalf())



