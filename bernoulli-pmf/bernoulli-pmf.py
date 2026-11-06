import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    pmf = [p if(bool == 1) else 1-p for bool in x ]
    return {"pmf": np.asarray(pmf), "mean": float(p), "variance": float(p*(1-p))}
    