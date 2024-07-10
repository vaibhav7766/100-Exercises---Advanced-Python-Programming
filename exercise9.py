def calculate(n):

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

count = 0
num = 0
i = 2
while count < 100:
    if calculate(i) == True:
        count += 1
        if count == 100:
            num = i
        i += 1
    else:
        i += 1

print(num)
