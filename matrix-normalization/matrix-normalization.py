import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    matrix = np.asarray(matrix)
    
    match norm_type: 
        case "l1":
            ord = 1
        case "l2":
            ord = 2
        case "max":
            ord = np.inf

    if(axis is None):
        if ord == 1:
            norm = np.sum(np.abs(matrix))

        elif ord == 2:
            norm = np.sqrt(np.sum(np.abs(matrix)**2))

        elif ord == np.inf:
            norm = np.max(np.abs(matrix))
    else: 
        norm = np.linalg.norm(matrix, ord=ord, axis=axis, keepdims = True)
    
    norm = np.where(norm == 0, 1.0, norm)

    return matrix / norm