from sympy import Matrix

# Define your matrix
A = Matrix([
    [1, 1, 2, 3],
    [2,  -2, 3, 1],
    [3, -1, 5, 4]
])

# Compute RREF
# .rref() returns a tuple: (the matrix, indices of pivot columns)
rref_matrix, pivots = A.rref()

print("Reduced Row Echelon Form:")
print(rref_matrix)
print(f"\nPivot Columns: {pivots}")
