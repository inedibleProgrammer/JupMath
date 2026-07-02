import numpy as np
from fractions import Fraction

# 1. Define the matrix using Fraction objects
# We use dtype=object so NumPy doesn't force them back into decimals
A = np.array([
    [Fraction(1), Fraction(3), Fraction(3), Fraction(13), Fraction(16)],
    [Fraction(0), Fraction(0), Fraction(-3), Fraction(-9), Fraction(-12)],
    [Fraction(-4), Fraction(-12), Fraction(-8), Fraction(-42), Fraction(-50)]
], dtype=object)

print("Original Matrix:")
print(A)
print("-" * 20)

