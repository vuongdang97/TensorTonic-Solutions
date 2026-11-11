import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    p = np.asarray(p)
    q = np.asarray(q)

    positive = p > 0
    q = np.clip(q[positive], eps, None)
    log = np.log(p[positive]/ q)

    return float(np.sum(p[positive]*log))
    