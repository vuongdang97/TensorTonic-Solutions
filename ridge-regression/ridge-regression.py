import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    I = np.eye(X.shape[1], dtype = float)
    w = X.T @ X + lam * I
    w = np.linalg.inv(w)
    w = w @ X.T @ y
    return list(w)