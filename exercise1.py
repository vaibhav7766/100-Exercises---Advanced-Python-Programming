def calculate(x):
    return sum(x)


l = []
for i in range(100):
    if i % 5 == 0 or i % 7 == 0:
        l.append(i)
    else:
        pass
print(calculate(l))
