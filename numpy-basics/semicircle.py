import numpy as np
import matplotlib.pyplot as plt

def make_semicircle():
    # Parameters
    R = 1.0                      # Radius of semicircle
    n_points = 100              # Number of points per segment

    # 1. Straight line from left to right
    x1 = np.linspace(-R, R, n_points)
    y1 = np.zeros_like(x1)

    # 2. Semicircle (top half, counterclockwise from right to left)
    theta = np.linspace(0, np.pi, n_points)
    x2 = R * np.cos(theta)
    y2 = R * np.sin(theta)

    # 3. Return straight line (right to left, bottom again)
    # x3 = np.linspace(R, -R, n_points)
    # y3 = np.zeros_like(x3)

    # Combine segments
    # x = np.concatenate([x1, x2, x3])
    # y = np.concatenate([y1, y2, y3])
    x = np.concatenate([x1, x2])
    y = np.concatenate([y1, y2])

    # Plot
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'b-', lw=2)
    plt.axis('equal')
    plt.title("Closed Loop: Straight Line + Semicircle")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

make_semicircle()
