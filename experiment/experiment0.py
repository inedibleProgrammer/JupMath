import numpy as np
from matplotlib import pyplot as plt

arr = np.array([1, 2, 3])
print(arr)
print(type(arr))

arr = np.array([[1,2,3], [4,5,6]])
print(arr)

x = np.linspace(0, 1, 100)
plt.plot(x, x**2)
plt.show()
