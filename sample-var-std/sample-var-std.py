import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x)
    mean = np.sum(x)/len(x)
    x = x - mean
    x = np.square(x)
    variance = float(np.sum(x)/(len(x) - 1))

    return {"variance": variance, "standard_deviation": float(np.sqrt(variance))}