
dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]

boggle = [['G','I','Z'],
          ['U','E','K'],
          ['Q','S','E']]


def neighbors(point, matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    ret = []
    for next_cell in [[+1, 0], [-1, 0], [0, -1], [0, +1],
                      [+1, +1], [-1, +1], [-1, -1], [+1, -1]]:
        if (0 <= point[0] + next_cell[0] < num_rows) \
                and (0 <= point[1] + next_cell[1] < num_cols):
            ret.append([point[0] + next_cell[0], point[1] + next_cell[1]])
    return ret


def not_visited(x, visited):
    L = len(list(filter(lambda o: o[0] == x[0] and o[1] == x[1], visited)))
    return L == 0


def dfs(matrix, x, y, target_word, constructed_word, visited):
    at = lambda cell: matrix[cell[0]][cell[1]]

    if len(target_word) == len(constructed_word):
        if constructed_word in dictionary:
            print(constructed_word)
        return

    nbrs = neighbors([x, y], matrix)
    visited.append([x, y])

    for n in nbrs:
        if not_visited(n, visited.copy()):
            dfs(matrix, n[0], n[1], target_word, constructed_word + at(n), visited)
    visited.pop()


# print(list(map(lambda x: boggle[x[0]][x[1]], neighbors([1, 1], boggle))))

dfs(boggle, 2, 0, "QUIZ", "Q", [[2, 0]])

