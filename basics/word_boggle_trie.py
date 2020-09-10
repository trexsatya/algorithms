


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


def create_trie(list_of_keys):
    trie = {}

    for key in list_of_keys:
        tmp = trie
        for letter in key:
            if letter not in tmp:
                tmp[letter] = {}
            tmp = tmp[letter]

    return trie


def find_in_trie(trie, key):
    tmp = trie
    for letter in key:
        if letter not in tmp:
            return False
        tmp = tmp[letter]
    return True


def next_letters(trie, prefix):
    # print("next for ", prefix)
    tmp = trie
    for letter in prefix:
        if letter not in tmp:
            return False
        tmp = tmp[letter]
    return tmp


# print(next_letters(trie, "G"))

def not_visited(x, visited):
    L = len(list(filter(lambda o: o[0] == x[0] and o[1] == x[1], visited)))
    return L == 0


def check_word(nxts, word, x, y, matrix, trie, found, dictionary, boggle, visited = []):
    at = lambda o: matrix[o[0]][o[1]]

    if nxts == False:
        return

    if not nxts:
        # print(word)
        found[word] = 1
        return

    if word in dictionary:
        # print(word)
        found[word] = 1

    nbrs = neighbors([x, y], boggle)
    nbrs = list(filter(lambda n:
                       matrix[n[0]][n[1]] in list(nxts.keys()), nbrs))

    # if word == 'G':
    #     print(nxts.keys(), list(map(at, nbrs)))

    # if not nbrs:
    #     print(word)
    #     return
    visited.append([x, y])
    for nbr in nbrs:
        if not_visited(nbr, visited.copy()):
            tmp_word = word + matrix[nbr[0]][nbr[1]]
            check_word(next_letters(trie, tmp_word),
                       tmp_word, nbr[0], nbr[1],
                       matrix, trie, found, dictionary, boggle, visited)
    visited.pop()


def solve(boggle, dictionary):
    trie = create_trie(dictionary)

    found = {}

    for i, row in enumerate(boggle):
        for j, letter in enumerate(row):
            could_be_in_dict = next_letters(trie, letter)

            if could_be_in_dict == False:
                continue

            # if not could_be_in_dict:
            # continue
            # print(letter)

            check_word(could_be_in_dict, letter, i, j,
                       boggle, trie, found,
                       dictionary, boggle)

    return found
# print(next_letters(trie, "S").keys())


dictionary = ['dfd', 'ded', 'fd', 'e', 'dec', 'df']

boggle = [['f', 'f'],
          ['d', 'e'],
          ['f', 'b'],
          ['b', 'e']]

found = solve(boggle, dictionary)
L = list(found.keys())
if len(L) == 0:
    print(-1)
else:
    print(" ".join(sorted(L)))

# db bcd
# e fd ded dfd df