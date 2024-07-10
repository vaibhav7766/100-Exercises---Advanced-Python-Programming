def is_prime(n):
    flag = 0
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n ** (0.5) + 1)):
            if n % i == 0:
                flag = 1
                break
        if flag == 1:
            return False
        else:
            return True
