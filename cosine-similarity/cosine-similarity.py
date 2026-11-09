import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)
    cos = np.dot(a, b)
    temp = np.linalg.norm(a, ord = 2)*np.linalg.norm(b, ord = 2)
    if(temp == 0):
        return 0.0
    else: 
        cos = cos/temp
    return float(cos)