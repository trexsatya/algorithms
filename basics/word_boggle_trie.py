
def neighbors(point, matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    ret = []
    for next_cell in [[+1, 0],   # Down
                      [-1, 0],   # Up
                      [0, -1],   # Left
                      [0, +1],   # Right
                      [+1, +1],  # Lower Right
                      [-1, +1],  # Upper Right
                      [-1, -1],  # Upper Left
                      [+1, -1]]:  # Lower Left
        if (0 <= point[0] + next_cell[0] < num_rows) \
                and (0 <= point[1] + next_cell[1] < num_cols):
            # Check that it is inside matrix
            ret.append([point[0] + next_cell[0],  # Row
                        point[1] + next_cell[1]])  # Column
    return ret


def create_data_structure(list_of_keys):
    trie = {}

    for key in list_of_keys:
        tmp = trie
        for letter in key:
            if letter not in tmp:
                tmp[letter] = {}
            tmp = tmp[letter]

    return trie


def retrieve_from_data_structure(trie, key):
    tmp = trie
    for letter in key:
        if letter not in tmp:
            return False
        tmp = tmp[letter]
    return True


def retrieve_next_letters(trie, prefix):
    tmp = trie
    for letter in prefix:
        if letter not in tmp:
            return False
        tmp = tmp[letter]
    return tmp


def not_visited(x, visited):
    L = len(list(filter(lambda o: o[0] == x[0] and o[1] == x[1], visited)))
    return L == 0


def check_word_is_in_dictionary(next_letters, word,
                                x, y,
                                matrix, trie,
                                found, dictionary,
                                visited=[]):
    if not next_letters:
        found[word] = 1
        return

    if word in dictionary:
        found[word] = 1

    nbrs = neighbors([x, y], board)
    nbrs = list(filter(lambda n:
                       matrix[n[0]][n[1]] in list(next_letters.keys()), nbrs))

    visited.append([x, y])
    for nbr in nbrs:
        if not_visited(nbr, visited.copy()):
            tmp_word = word + matrix[nbr[0]][nbr[1]]
            check_word_is_in_dictionary(retrieve_next_letters(trie, tmp_word),
                                        tmp_word,
                                        nbr[0], nbr[1],
                                        matrix, trie, found,
                                        dictionary, visited)
    visited.pop()


def solve(board, dictionary):
    trie = create_data_structure(dictionary)

    found = {}

    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            next_letters = retrieve_next_letters(trie, letter)

            if next_letters == False:
                continue

            check_word_is_in_dictionary(next_letters, letter, i, j,
                                        board, trie, found,
                                        dictionary)

    return found


dictionary = ['dfd', 'ded', 'fd', 'e', 'dec', 'df']

board = [['f', 'f'],
          ['d', 'e'],
          ['f', 'b'],
          ['b', 'e']]

found = solve(board, dictionary)
L = list(found.keys())
if len(L) == 0:
    print(-1)
else:
    print(" ".join(sorted(L)))

