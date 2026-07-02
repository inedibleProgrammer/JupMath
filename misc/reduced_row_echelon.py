
def first_attempt():
    import numpy as np

    # Define the matrix
    # R1: [2, -9, -21]
    # R2: [1,  6,  12]
    A = np.array([
        [2, -9, -21],
        [1,  6,  12]
    ], dtype=float) # Use float to avoid integer rounding issues

    print(A)

    # 1. Perform the operation: -2*R2 + R1 -> R2
    # A[0] = R1
    # A[1] = R2
    A[1] = -2 * A[1] + A[0]
    print(A)

    # 2. 1/2R1 -> R1
    A[0] = 1/2 * A[0]
    print(A)

    # 3. -1/21R2 -> R2
    A[1] = -1/21*A[1]
    print(A)

    # 4. 4.5R2 + R1 -> R1
    A[0] = 4.5*A[1] + A[0]
    print(A)

def second_attempt():
    import numpy as np
    from fractions import Fraction

    # 1. Define the matrix using Fraction objects
    # We use dtype=object so NumPy doesn't force them back into decimals
    A = np.array([
        [Fraction(2), Fraction(-9), Fraction(-21)],
        [Fraction(1), Fraction(6),  Fraction(12)]
    ], dtype=object)

    print("Original Matrix:")
    print(A)
    print("-" * 20)

    # 1. Perform the operation: -2*R2 + R1 -> R2
    A[1] = -2 * A[1] + A[0]
    print("Step 1: -2*R2 + R1 -> R2")
    print(A)
    print("-" * 20)

    # 2. 1/2R1 -> R1
    A[0] = Fraction(1, 2) * A[0]
    print("Step 2: 1/2*R1 -> R1")
    print(A)
    print("-" * 20)

    # 3. -1/21R2 -> R2
    A[1] = Fraction(-1, 21) * A[1]
    print("Step 3: -1/21*R2 -> R2")
    print(A)
    print("-" * 20)

    # 4. 4.5R2 + R1 -> R1 (4.5 is Fraction(9, 2))
    A[0] = Fraction(9, 2) * A[1] + A[0]
    print("Step 4 (Final RREF): 9/2*R2 + R1 -> R1")
    print(A)

# first_attempt()
second_attempt()

