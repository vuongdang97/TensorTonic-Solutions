import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    X = X - np.mean(X, axis = 0)
    sigma = X.T @ X
    sigma = sigma / (X.shape[0] - 1)
    return sigma