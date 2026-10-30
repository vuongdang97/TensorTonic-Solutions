import numpy as np

def normalize_3d(v: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as v.
    """
    # Write code here
    v = np.asarray(v, dtype = float)
    if(v.ndim!= 1):
        norms = np.linalg.norm(v, axis=1, keepdims=True)
    else: 
        norms = np.linalg.norm(v)
    print(norms)
    normalize = np.divide(v, norms, out=np.zeros_like(v), where=norms != 0)
    
    return normalize
            