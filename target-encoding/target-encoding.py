def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    map = {}

    for i in range(len(categories)):
        curr = categories[i]
        if curr in map:
            map[curr][0] = map[curr][0] + targets[i]
            map[curr][1] = map[curr][1] + 1
        else:
            map[curr] = [targets[i], 1]            

    result = []

    for i in range(len(categories)):
        curr = categories[i]
        result.append(map[curr][0]/ map[curr][1])

    return result