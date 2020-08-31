import math


def solve():
    matrix = [[0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1],
              [0, 0, 1, 1, 1],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1]]

    row_with_min = -1
    minimum = math.inf

    R = len(matrix)
    C = len(matrix[0])

    done = False
    row = 0
    col = 0
    while not done:
        if row >= R:  # Matrix scanned completely
            return row_with_min

        if matrix[row][col] == 1:
            if C - col < minimum:
                minimum = C - col
                row_with_min = row
            row += 1
        else:  # 0
            col += 1  # Just move right

        if row < R and col >= C:  # If we are going out of matrix
            col = 0
            row += 1
    return row_with_min


ret = solve()
print(ret)

# Does it work? - YES

