def compress(s):
    s = str(s)
    l = []
    count = 0
    for i in range(len(s) - 1):
        count += 1
        if s[i] != s[i + 1]:
            l.append((s[i], count))
            count = 0
        if i == len(s) - 2:
            count += 1

    l.append((s[i], count))
    return l
