import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 5, 100)
# f = x**2

# dx = np.gradient(x)
# dy = np.gradient(f)

# dydx = dy/dx


# d2y = np.gradient(dy)
# # dx2 = np.gradient(dx)
# dx2 = dx**2

# d2ydx2 = d2y/dx2

# plt.plot(x, d2ydx2)
# plt.show()



x = np.linspace(0, 5, 100)
f = x**2

f_x = np.gradient(f, x)
f_xx = np.gradient(f_x, x)

f_x_2idx = np.argmin(np.abs(f_x - 4))

plt.plot(x, f_xx)
plt.show()

