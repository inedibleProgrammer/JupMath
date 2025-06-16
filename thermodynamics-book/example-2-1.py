import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from scipy.optimize import fsolve


def expansion_function_A(P, V):
    return P*(V**1.5) - 0.09486832980505139


p_values = np.linspace(0, 5, 100)

v_values = []

for p in p_values:
    v_values.append(fsolve(expansion_function_A, 0.5, args=(p))[0])

# k is the same all the time:
# >>> k0 = 3 * (0.1**1.5)
# >>> k0
# 0.09486832980505139
# >>> k1 = 1.06*(0.2**1.5)
# >>> k1
# 0.0948092822459911
# >>> 3*(0.1/0.2)**1.5
# 1.0606601717798214
# >>> k1 = 1.0606601717798214*(0.2**1.5)
# >>> k1
# 0.0948683298050514
plt.plot(p_values, np.array(v_values))
#plt.axis('equal')
plt.xlim(0, 0.3)
plt.show()
