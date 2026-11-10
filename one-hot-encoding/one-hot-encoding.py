import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    N = len(y)
    if num_classes is None: 
        K = max(y) + 1
    else: 
        K = num_classes
    matrix = np.zeros((N, K), dtype = float)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if(j == y[i]):
                matrix[i][j] = 1.0
    return matrix