import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    Sigma = (X - np.mean(X, axis = 0)).T @ (X - np.mean(X, axis = 0)) / (X.shape[0] - 1)
    Var = np.sqrt(np.diag(Sigma))
    denominator = np.outer(Var, Var.T)

    return Sigma / denominator