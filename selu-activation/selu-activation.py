import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    lba = 1.0507
    alpha = 1.6733
    y = [lba*i if(i > 0) else lba*alpha*(math.exp(i) - 1) for i in x]
    return y