class Matrix:
    def __init__(self, s):
        self.s = s
        self.matrix = [list(map(int, i.split())) for i in s.split("\n")]


m = Matrix("3 4\n5 6\n7 8")
print(m.matrix)