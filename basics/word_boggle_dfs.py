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


def check_the_combined_word(matrix, x, y, max_length, constructed_word, green_ones, found):
    at = lambda cell: matrix[cell[0]][cell[1]]

    if len(constructed_word) > max_length:
        return

    if len(constructed_word) <= max_length:
        if constructed_word in dictionary:
            # print(constructed_word)
            found[constructed_word] = 1



    nbrs = neighbors([x, y], matrix)
    green_ones.append([x, y])

    for n in nbrs:
        if not_visited(n, green_ones.copy()):
            check_the_combined_word(matrix, n[0], n[1], max_length, constructed_word + at(n), green_ones, found)
    green_ones.pop()




dictionary = ['gee', 'go', 'get', 'blue']

board = [['g', 'o', 't'],
         ['s', 'e', 'e'],
         ['s', 'o', 'n']]


def solve(board, dictionary):
    max_lengths = {}
    for word in dictionary:
        if word[0] not in max_lengths:
            max_lengths[word[0]] = len(word)
        else:
            max_lengths[word[0]] = max(len(word), max_lengths[word[0]])

    found = {}

    # print(max_lengths)
    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            max_length = 0
            if letter in max_lengths:
                max_length = max_lengths[letter]
            check_the_combined_word(board, i, j, max_length, letter, [[i, j]], found)

    return found

found = solve(board, dictionary)
L = list(found.keys())
if len(L) == 0:
    print(-1)
else:
    print(" ".join(sorted(L)))