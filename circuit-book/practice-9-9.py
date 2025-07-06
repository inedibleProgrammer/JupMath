import cmath
import math



def using_phasors():
    w = 10
    z1 = 4
    L2 = 0.2
    z2 = complex(0, w * L2)
    y1 = 1/z1
    y2 = 1/z2
    N1 = cmath.rect(20, math.radians(30))

    N2 = (-y1 * N1)/(-y1 - y2)
    print(N2)
    N2_mag_t = cmath.polar(N2)[0]
    N2_phase_t = math.degrees(cmath.polar(N2)[1])
    print(N2_mag_t, N2_phase_t)

    i1 = N2/z2
    i1_mag_t = cmath.polar(i1)[0]
    i1_phase_t = math.degrees(cmath.polar(i1)[1])
    print(i1_mag_t, i1_phase_t)

def using_convolution():
    

# using_phasors()
using_convolution()



