def get_slices(sequence, length):
    n = len(sequence)
    if length < 1:
        raise ValueError("The length cannot be less than 1.")
    if length > n:
        raise ValueError("The length cannot be greater than sequence.")
    if length == n:
        return sequence
    return [sequence[i : i + length] for i in range(n - length + 1)]
