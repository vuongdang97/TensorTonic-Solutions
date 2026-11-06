import math
import numpy as np

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    # Write code here
    blur_h = np.linspace(0, size - 1, size).reshape(1, -1) - size//2
    blur_v = np.linspace(0, size - 1, size).reshape(-1, 1) - size//2
    blur_h = np.exp(-blur_h**2/(2*sigma**2))
    blur_v = np.exp(-blur_v**2/(2*sigma**2))
    result = np.kron(blur_h, blur_v)
    result = result/np.sum(result)
    result = result.tolist()

    return result
