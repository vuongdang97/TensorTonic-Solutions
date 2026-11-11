import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    row = np.arange(len(y_true)).reshape(-1, 1)
    y_true = np.array(y_true).reshape(-1, 1)
    y_pred = np.array(y_pred)
    true_prob = y_pred[row, y_true]
    loss = -np.mean(np.log(true_prob))
    return loss