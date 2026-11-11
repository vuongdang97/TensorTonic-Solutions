import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.asarray(x)
    max_ele = np.max(x, axis = -1, keepdims = True)
    x = x-max_ele
    x = np.exp(x)
    x = x / np.sum(x, axis = -1, keepdims = True)
    return x