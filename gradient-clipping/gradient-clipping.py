import numpy as np

def clip_gradients(g: list, max_norm: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as g.
    """
    # Write code here
    g = np.asarray(g)
    norm_g = np.linalg.norm(g)
    if(norm_g > max_norm):
        g = g*max_norm/norm_g
    return g