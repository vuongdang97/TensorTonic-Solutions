def color_to_grayscale(image: list) -> list:
    """
    Returns the luminance value of every RGB pixel.
    """
    # Write code here
    result = []
    for list_element in image:
        temp = []
        for combination in list_element:
            R = combination[0]
            G = combination[1]
            B = combination[2]
            Y = 0.299*R + 0.587*G + 0.114*B
            temp.append(Y)
        result.append(temp)
    return result