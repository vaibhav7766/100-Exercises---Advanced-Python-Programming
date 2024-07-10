def calculate():
    sn = 0
    a, b = 0, 1
    while a < 1000000:
        if a % 2 == 0:
            sn += a
        a, b = b, a + b
    return sn


print(calculate())
