# Example 2.10 - Not a Bad Throw for a Rookie!

import numpy as np
from matplotlib import pyplot as plt

vi = 20
hi = 50
g = -9.81

# t is an array of 1000 equally spaced time values between 0 and 5
t = np.linspace(0, 5, 1000)

# t*0 returns an array of size t with all 0s
acceleration = t*0 + g
# print(acceleration)
# velocity is the integral of acceleration
velocity = np.cumsum(acceleration) * (t[1] - t[0]) + vi
# position is the integral of velocity
position = np.cumsum(velocity) * (t[1] - t[0]) + hi

# B. Find the maximum height of the stone
position_max = np.max(position)

# A. Calculate the time at which the stone reaches its maximum height
print(t[position == position_max])

# C. Determine the velocity of the stone when it returns to the height from which it was thrown

print(velocity[(position < hi + 0.05) * (position > hi - 0.05)])
# print(position)

# D. Find the velocity and position of the stone at t = 5.00s
print(position[t == 5])
print(velocity[t == 5])


# Plots

plt.plot(t, acceleration)
plt.plot(t, velocity)
plt.plot(t, position)
plt.show()


