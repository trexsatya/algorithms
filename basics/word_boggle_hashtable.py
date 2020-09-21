
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
    hashtable = {}

    for key in list_of_keys:
        for prefix in [key[0:x] for x in
                       range(1, len(key))]:
            if prefix not in hashtable:
                hashtable[prefix] = 'prefix'
        hashtable[key] = 'word'

    return hashtable


# print(next_letters(trie, "G"))

def not_visited(x, visited):
    L = len(list(filter(lambda o: o[0] == x[0] and o[1] == x[1], visited)))
    return L == 0


def check_word_is_in_dictionary(word,
                                x, y,
                                matrix,
                                hashtable,
                                found,
                                visited=[]):
    if word not in hashtable:
        return

    if hashtable[word] == 'word':
        found[word] = 1

    nbrs = neighbors([x, y], matrix)

    visited.append([x, y])
    for nbr in nbrs:
        if not_visited(nbr, visited.copy()):
            tmp_word = word + matrix[nbr[0]][nbr[1]]
            check_word_is_in_dictionary(tmp_word,
                                        nbr[0], nbr[1],
                                        matrix,
                                        hashtable,
                                        found,
                                        visited)
    visited.pop()


def solve(boggle, dictionary):
    hashtable = create_data_structure(dictionary)

    found = {}

    for i, row in enumerate(boggle):
        for j, letter in enumerate(row):
            check_word_is_in_dictionary(letter,
                                        i, j,
                                        boggle,
                                        hashtable,
                                        found
                                       )

    return found


dictionary = ['b', 'edc', 'ddd', 'cc', 'ccb', 'ffb']

boggle = [['d', 'd'],
          ['c', 'c'],
          ['b', 'f'],
          ['d', 'd'],
          ['c', 'd']]

found = solve(boggle, dictionary)
L = list(found.keys())
if len(L) == 0:
    print(-1)
else:
    print(" ".join(sorted(L)))

print(create_data_structure(dictionary))
