import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    N = len(y_true)
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    MSE = 1/N*np.linalg.norm(y_pred - y_true)**2

    return MSE