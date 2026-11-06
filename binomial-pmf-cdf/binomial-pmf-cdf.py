import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    cdf = 0
    for i in range(k):
        cdf += math.comb(n, i)*p**i*(1 - p)**(n - i)
    pmf = math.comb(n, k)*p**k*(1 - p)**(n - k)
    cdf = cdf + pmf
    return {"pmf": float(pmf), "cdf": float(cdf)}