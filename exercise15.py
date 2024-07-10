from itertools import groupby

def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = ["".join(item) for item in result]
    return "_".join(result)


def decompress(s):
    s = s.split("_")
    res = ""
    for i in s:
        res += i[0] * int(i[1:])
    return int(res)
