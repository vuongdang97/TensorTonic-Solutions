def image_histogram(image: list) -> list:
    """
    Returns a list of intensity and count pairs.
    """
    # Write code here
    temp = [0] *256
    for i in range(len(image)):
        for j in range(len(image[i])):
            curr = int(image[i][j])
            temp[curr] = temp[curr] + 1
    result = []
    
    for i in range(len(temp)):
        if(temp[i] == 0):
            continue 
        result.append([i, temp[i]])
        
    return result