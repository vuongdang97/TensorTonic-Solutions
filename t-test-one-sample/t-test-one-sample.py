import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.asarray(x)
    n = x.shape[0]
    s = np.sqrt(1/(n - 1))*np.linalg.norm(x - np.mean(x), ord = 2)
    if s == 0:
        if(np.mean(x) != mu0):
            return np.inf
        else: 
            t = 0
    else: 
        t = (np.mean(x) - mu0)/(s/np.sqrt(n))
    return float(t)    