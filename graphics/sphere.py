import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_sphere_mesh(radius=1, num_lat=20, num_lon=40):
    phi = np.linspace(0, np.pi, num_lat)
    theta = np.linspace(0, 2 * np.pi, num_lon)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    vertices = np.stack((x, y, z), axis=-1).reshape(-1, 3)

    # Create triangle indices
    triangles = []
    for i in range(num_lon - 1):
        for j in range(num_lat - 1):
            idx = lambda i, j: i * num_lat + j
            a = idx(i, j)
            b = idx(i + 1, j)
            c = idx(i + 1, j + 1)
            d = idx(i, j + 1)
            triangles.append([a, b, c])
            triangles.append([a, c, d])
    triangles = np.array(triangles)
    return vertices, triangles

def triangle_area(a, b, c):
    ab = b - a
    ac = c - a
    return 0.5 * np.linalg.norm(np.cross(ab, ac), axis=-1)

def compute_surface_area(vertices, triangles):
    a = vertices[triangles[:, 0]]
    b = vertices[triangles[:, 1]]
    c = vertices[triangles[:, 2]]
    areas = triangle_area(a, b, c)
    return np.sum(areas)

# Generate mesh
vertices, triangles = generate_sphere_mesh(radius=1, num_lat=100, num_lon=100)

# Compute surface area
surface_area = compute_surface_area(vertices, triangles)

print(f"Computed Surface Area: {surface_area}")
print(f"Analytical Area of Unit Sphere: {4 * np.pi}")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=1)
plt.show()
