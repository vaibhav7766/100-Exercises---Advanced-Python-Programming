def binary_to_int():
    with open("binary.txt", "r") as f:
        content = f.read().strip()

    return [int(line.strip(), 2) for line in content.split("\n")]
