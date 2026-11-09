import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    cdf = math.exp(-lam)
    pmf = math.exp(-lam)
    for i in range(1, k +1):
        pmf = pmf*lam/i
        cdf = cdf + pmf

    return {"pmf" : pmf, "cdf": cdf}