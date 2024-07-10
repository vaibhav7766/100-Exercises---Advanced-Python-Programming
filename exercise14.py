def compress(s):
    s = str(s)
    res = ""
    count = 0
    for i in range(len(s) - 1):
        count += 1
        if s[i] != s[i + 1]:
            res += s[i] + "." * count
            count = 0
        if i == len(s) - 2:
            count += 1

    res += s[i] + "." * count
    return res
