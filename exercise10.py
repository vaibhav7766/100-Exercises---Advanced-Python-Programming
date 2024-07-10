def is_palindrome(n):
    b = str(bin(n)).replace("0b", "")
    a = str(n)
    if a == a[::-1] and b == b[::-1]:
        return True
    else:
        return False
