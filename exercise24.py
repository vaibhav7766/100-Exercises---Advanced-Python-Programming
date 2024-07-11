from itertools import cycle

def spiral_matrix(size):
    matrix = [[None] * size for _ in range(size)]

    x, y = 0, 0

    movements = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    dx, dy = next(movements)

    for i in range(size**2):
        matrix[x][y] = i + 1
        xdx = x + dx
        ydy = y + dy
        if not 0 <= xdx < size or not 0 <= ydy < size or matrix[xdx][ydy] is not None:
            dx, dy = next(movements)
        x += dx
        y += dy
    return matrix
