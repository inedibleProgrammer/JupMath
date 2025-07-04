import numpy as np


def using_vectors():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    dot_product = np.dot(v1, v2)
    cross_product = np.cross(v1, v2)
    magnitude_v1 = np.linalg.norm(v1)
    unit_v1 = v1 / np.linalg.norm(v1)

    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle_rad = np.arccos(cos_theta)


def cross_product_unit_vectors():

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    v1_mag = np.linalg.norm(v1)
    v2_mag = np.linalg.norm(v2)

    v1_unit = v1 / v1_mag
    v2_unit = v2 / v2_mag

    cross_product = np.cross(v1, v2)
    cross_product_2 = v1_mag * v2_mag * np.cross(v1_unit, v2_unit)
    print(cross_product)
    print(cross_product_2)


# using_vectors()
cross_product_unit_vectors()

