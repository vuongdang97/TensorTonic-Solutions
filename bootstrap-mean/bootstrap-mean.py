import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    x = np.asarray(x)
    rng = np.random.default_rng(seed)

    index = rng.integers(0, x.size, size = (n_bootstrap, x.size))
    bootstrap_sample = x[index]
    bootstrap_mean = bootstrap_sample.mean(axis = 1)
    alpha = (1 - ci)/2
    lower, upper = np.quantile(bootstrap_mean, [alpha, 1 - alpha])
    return {"bootstrap_mean": np.mean(bootstrap_mean), "lower": lower, "upper": upper}
    