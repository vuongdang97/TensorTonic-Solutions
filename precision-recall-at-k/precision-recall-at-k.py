def binary_search(element: int, relevant:list) -> bool:
    left = 0
    right = len(relevant)
    while(left < right - 1):
        mid = int((left + right)/2)
        if(element == relevant[mid]):
            return True
        if(element < relevant[mid]):
            right = mid
        else:
            left = mid
    if(element == relevant[right - 1]):
        return True
    return False

def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    count = 0
    # Write code here
    for i in range(k): 
        if(binary_search(recommended[i], relevant)):
            count = count + 1
    return [float(count/k), float(count/len(relevant))]