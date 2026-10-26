import numpy as np
import math

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    _, count = np.unique(y, return_counts=True)
    prob0 = 1
    entropy = 0
    for i in range(len(count)): 
        prob = count[i]/len(y)
        entropy = entropy -prob*np.log2(prob) 
        prob0 = prob0 - prob
    if (prob0 != 0):
        entropy = entropy -prob0*np.log2(prob0)
    return entropy
        