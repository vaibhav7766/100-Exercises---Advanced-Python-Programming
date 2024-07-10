def hamming_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Both vectors must be the same length.")
    count = 0
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            count += 1
    return count
