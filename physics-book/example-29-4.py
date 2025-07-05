import numpy as np
import matplotlib.pyplot as plt

def uniform_magnetic_field():
    # Define the grid (2D space)
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    X, Y = np.meshgrid(x, y)

    # Uniform magnetic field pointing in +y direction
    Bx = np.zeros_like(X)
    By = np.ones_like(Y)  # or any constant like 3.0

    # Now Bx, By define the vector field
    plt.figure(figsize=(6, 6))
    plt.quiver(X, Y, Bx, By, color='blue', scale=20)
    plt.title("Uniform Magnetic Field in +y Direction")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# I think I learned that you should always use 3d vectors, because
# the cross product of 2-d vectors is a scalar
def first_attempt():
    # I am using made up numbers. The book answers this question purely algebraically
    # Parameters
    B_mag = 2.0 # Teslas
    I = 3 # Amps
    R = 1.0                      # Radius of semicircle
    n_points = 100              # Number of points per segment

    # 1. Straight line from left to right
    x1 = np.linspace(-R, R, n_points)
    y1 = np.zeros_like(x1)
    z1 = np.zeros_like(x1)
    t1 = np.arange(len(x1))

    dx1 = np.diff(x1)
    dy1 = np.diff(y1) # y is all 0, but doing this for consistency
    dz1 = np.diff(z1)
    ds1 = np.sqrt(dx1**2 + dy1**2)
    # print(x1.shape)
    # print(dx1.shape)
    arc_length_1 = np.concatenate(([0], np.cumsum(ds1)))

    dt1 = np.diff(t1)
    dxdt1 = dx1/dt1
    dydt1 = dy1/dt1
    dzdt1 = dz1/dt1
    dr_mag1 = np.sqrt(dxdt1**2 + dydt1**2)
    r1 = np.stack((x1, y1, z1), axis=1)
    dr1 = np.diff(r1, axis=0) # axis=0 makes a huge difference here
    drdt1 = np.stack((dxdt1, dydt1, dzdt1), axis=1)
    # print(r1)
    # print(drdt1)
    # Unit Tangent Vector T
    # Reshape transforms to a column vector
    # The -1 tells NumPy to automatically calculate that dimension based on the original array’s size.
    T1 = drdt1/dr_mag1.reshape(-1, 1)
    # print(T1)
    # print(dr_mag1)
    # print(dr_mag1.reshape(-1,1))


    # print(arc_length_1)

    # 2. Semicircle (top half, counterclockwise from right to left)
    theta = np.linspace(0, np.pi, n_points)
    x2 = R * np.cos(theta)
    y2 = R * np.sin(theta)
    z2 = np.zeros_like(x2)

    # Combine segments
    x = np.concatenate([x1, x2])
    y = np.concatenate([y1, y2])
    z = np.concatenate([z1, z2])

    dx = np.diff(x)
    dy = np.diff(y)
    ds = np.sqrt(dx**2 + dy**2)

    t = np.arange(len(x))
    dt = np.diff(t)

    Bx = np.full_like(t, 0)
    By = np.full_like(t, B_mag)
    Bz = np.full_like(t, 0)
    B = np.stack((Bx, By, Bz), axis=1)
    B1, B2 = np.split(B, 2)
    # print(B1)

    # Insert 0s in the beginning to make shapes work
    ds1_pad = np.insert(ds1, 0, 0)
    T1_pad = np.insert(T1, 0, [0, 0, 0], axis=0)
    dr1_pad = np.insert(dr1, 0, [0, 0, 0], axis=0)
    ds1_pad_reshape = ds1_pad.reshape(-1, 1)
    F1_cross = np.cross(T1_pad, B1)

    # F1 and F1_2 demonstrate that dr x B = T x B * ds
    F1 = I * np.cumsum(np.cross(T1_pad, B1) * ds1_pad_reshape)
    F1_2 = I * np.cumsum(np.cross(dr1_pad, B1))
    F1_expected = 2 * I * R * B_mag

    # print(r1)
    # print(T1)
    # print(r1)
    # print(dr1[0])
    # print(dr1[1])
    print(F1)
    print(F1_2)
    # print(T1_pad)
    # print(B1)
    # print(F1_cross)
    # print(F1_cross * ds1_pad_reshape)
    # print(np.cumsum(F1_cross * ds1_pad_reshape, axis=0))
    print(F1_expected)
    # print(np.cross(T1_pad, B1))
    # print(ds1_pad.shape)

    # Circumference of a semicircle is: πr + 2r
    arc_length = np.concatenate(([0], np.cumsum(ds)))
    # print(arc_length)





# uniform_magnetic_field()
first_attempt()


