import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code her
    expect_value = 0.0
    x = np.asarray(x)
    p = np.asarray(p)
    for i in range(len(x)):
        expect_value = expect_value + x[i]*p[i]
    return expect_value