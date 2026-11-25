import numpy as np

def vector_norm_3d(v: list) -> float | np.ndarray:
    """
    Returns a float or a NumPy array.
    """
    # Write code here
    v =  np.asarray(v)
    sum = np.sum(v**2, axis = -1)
    sum = np.sqrt(sum)
    return sum
    