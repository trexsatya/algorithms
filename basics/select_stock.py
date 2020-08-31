import basics.utils as utils

def pretty_print(anything, pad=5, char=' '):
    # if isinstance(anything, list):
    #     to_print = [str(i).rjust(pad, char) for i in anything]
    # else:
    #     to_print = anything
    # print(to_print)
    pass


# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    for i, row in enumerate(K):
        pretty_print(row)

    res = K[n][W]
    items = []
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:

            # This item is included.
            # print(wt[i - 1])
            items.append([wt[i - 1], i-1, val[i-1]])

            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]

    # print(items)

    return K[n][W]


def add_forward(num, row, col, matrix):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        if matrix[row][col] < num:
            matrix[row][col] = num


def solve(limit, current_values, profits):
    # profits = [future_values[i] - current_values[i] for i in range(len(current_values))]

    # print(profits)
    matrix = [0 for i in current_values]
    for i, row in enumerate(matrix):
        matrix[i] = [0]*(limit+2)


    maximum = 0
    for i, investment in enumerate(current_values[:]):
        for subset_sum in range(limit+1):
            if subset_sum == 0:
                continue
            if subset_sum == investment:
                matrix[i][investment] = profits[i]

            matrix[i][subset_sum] = max(matrix[i][subset_sum], matrix[i-1][subset_sum])  # From top
            if matrix[i-1][subset_sum]:
                add_forward(matrix[i-1][subset_sum] + profits[i], i, subset_sum + investment, matrix)
            maximum = max(maximum, matrix[i][subset_sum])

    # print('  ', end='')
    pretty_print([x for x in range(len(matrix[0]))])
    for i, x in enumerate(matrix):
        # print(' ' + str(i), end='')
        pretty_print(x)
    # print(len([x for x in matrix[i] if x > 0]))
    # print()

    return maximum


def simple(limit, wts, vals):
    cumulated = []
    maximum = 0
    for i, weight in enumerate(wts):
        tmp = []
        for c in cumulated:
            if weight + c[0] <= limit:
                tmp.append([weight + c[0], vals[i] + c[1]])
                maximum = max(maximum, vals[i] + c[1])
        if weight <= limit:
            tmp.append([weight, vals[i]])
            maximum = max(maximum, vals[i])
        cumulated.extend(tmp)

    return maximum


values = "51 94 66 55 81 99 79 12 14 32 36 88 65 79 62 37 47 13 93 77 100 26 44 66 73 71 74 27 6 43 16 50 7 65 3 58 7 " \
         "90 99 60 84 54 68 45 28 5 43 77 47 68 9 83 66 20 84 67 4 70 90 80 11 72 54 63 9 91 43 44 36 89 60 92 70 13 " \
         "66 43 45 20 32 22 61 94 25 79 27".split()
weights = "6 89 12 23 22 72 2 25 47 40 51 93 15 49 85 43 88 75 96 72 72 26 90 46 17 69 74 73 7 25 35 27 7 19 77 53 11 " \
          "21 20 32 39 45 24 19 54 94 85 9 38 19 40 37 40 53 62 32 47 20 19 51 90 5 89 50 68 63 59 8 64 16 24 51 13 " \
          "37 76 63 68 32 12 18 12 60 45 39 64".split()

# values = [10, 15, 40]
# weights = [1, 2, 3]
values = list(map(int, values))
weights = list(map(int, weights))


# pretty_print(weights)
# pretty_print(values)
# pretty_print(list(map(lambda x: '-', weights)), 5, '-')
# res = solve(50, weights, values)
# res = knapSack(71, weights, values, len(weights))
# print(res)
W = 71
res1 = knapSack(W, weights, values, len(weights))
res2 = solve(W, weights, values)
res3 = solve2(W, weights, values)
print(res1, res2, res3)

for x in range(500):
    W = utils.an_int([0, 1000])
    n = utils.an_int([5, 30])
    weights = utils.array_of_random_ints(n, [1, 800])
    values = utils.array_of_random_ints(n, [1, 800])
    res1 = knapSack(W, weights, values, len(weights))
    res2 = solve(W, weights, values)
    res3 = solve2(W, weights, values)
    # print(res1, res2, res3)
    if not (res1 == res2 == res3):
        print("Found------------------------")
        print(res1, res2, res3)
        print(W, weights, values)
        print("EndFound------------------------")

