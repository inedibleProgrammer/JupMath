# Question 3

# Flower Petal

import numpy as np
from matplotlib import pyplot as plt


# r(theta) = 1 + 3/4 sin(3 theta) for 0 <= theta <= 2pi

# 1. Make a plot of the flower

num_points = 1000
theta_max = 2*np.pi
theta = np.linspace(0, theta_max, num_points)
r = 1 + 3/4*np.sin(3*theta)
x = r*np.cos(theta)
y = r*np.sin(theta)

# plt.plot(theta, r)
plt.plot(x, y)
plt.show()


# 2. Compute the area using the calculus formula A = integral(1/2 r**2dtheta, 0, 2pi)

# This was my solution
area_int = 1/2* np.cumsum(r**2) * (theta[1] - theta[0])
area = area_int[-1] - area_int[0]
print("My area: " + str(area))

# Mr. P Solver's solution
area_2 = 1/2 * np.sum(r**2) * (theta[1] - theta[0]) # he used sum not np.sum
print("P Solver Area: " + str(area_2))

# 3. Compute the arclength using the calculus formula
drdtheta = np.gradient(r, theta)
integrand = np.sqrt((r**2 + drdtheta**2)) * (theta[1] - theta[0])
arclength = np.sum(integrand)
print(arclength)



