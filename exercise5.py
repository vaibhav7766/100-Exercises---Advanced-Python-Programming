def calculate():
    count = 0
    for i in range(100, 1000):
        i = str(i)
        if i == i[::-1]:
            count += 1
    return count


print(calculate())
