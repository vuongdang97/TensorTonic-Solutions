def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    result = []
    
    for point in points: 
        row = []
        for centroid  in centroids: 
            d = sum((x-c)**2 for x, c in zip(point, centroid))
            row.append(d)
        minimum = min(row)
        idx = row.index(minimum)
        result.append(idx)

    return result