import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    row = len(A)
    col = len(A[0])

    output = np.zeros((col, row))
    for i in range(row):
        for j in range(col):
            output[j, i] = A[i][j]
    return output
    

