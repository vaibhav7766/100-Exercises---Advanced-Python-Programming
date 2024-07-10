def compress(s):
    s = str(s)
    res = ""
    count = 0
    for i in range(len(s) - 1):
        count += 1
        if s[i] != s[i + 1]:
            res += s[i] + str(count) + "_"
            count = 0
        if i == len(s) - 2:
            count += 1

    res += s[i] + str(count) + "_"
    return res[:-1]

# Alternate solution
# from itertools import groupby


# def compress(number):
#     result = [
#         "".join((key, str(len(list(group))))) for key, group in groupby(str(number))
#     ]
#     return "_".join(result)
