def calculate():
    l = []
    for i in range(10, 100):
        for j in range(10, 100):
            prod = i * j
            prod = str(prod)
            if prod == prod[::-1]:
                l.append(int(prod))
    return max(l)

print(calculate())