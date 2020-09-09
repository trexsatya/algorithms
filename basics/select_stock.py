import utils
from utils import timing

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
@timing
def knapSack(limit, weights, values):
    # Prepare matrix
    K = [[0 for x in range(limit + 1)] for x in range(len(weights) + 1)]

    for i in range(len(weights) + 1):
        for w in range(limit + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(
                              values[i - 1] + K[i - 1][w - weights[i - 1]],
                              K[i-1][w]
                        )
            else:
                K[i][w] = K[i-1][w]

    for i, row in enumerate(K):
        pretty_print(row)

    return K[n][limit]

@timing
def knapSack2(limit, weights, values):
    # Prepare matrix
    K = [[0 for x in range(limit + 1)] for x in range(len(weights) + 1)]

    for i in range(len(weights)):
        if weights[i] < limit:
            K[i][weights[i]] = values[i]

        for w in range(limit + 1):
            # if i == 0 or w == 0:
            #     K[i][w] = 0
            # if weights[i] <= limit and w == weights[i]:
            #     K[i][w] = max(K[i][w], values[i])

            # From top cell
            K[i][w] = max(K[i][w], K[i-1][w])

            if w - weights[i] >= 0:
                K[i][w] = max(
                    # From top left
                    values[i] + K[i-1][w - weights[i]],
                    K[i][w]
                )

    return K[n-1][limit]


def add_forward(num, row, col, matrix):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        if matrix[row][col] < num:
            matrix[row][col] = num

@timing
def matrix_based_solution(limit, item_weights, values):
    # profits = [future_values[i] - current_values[i] for i in range(len(current_values))]

    # print(profits)
    matrix = [0 for i in item_weights]
    for i, row in enumerate(matrix):
        matrix[i] = [0]*(limit+2)


    maximum = 0
    for i, cost in enumerate(item_weights[:]):
        for wt in range(1, limit+1):
            if wt == cost:
                matrix[i][cost] = values[i]

            matrix[i][wt] = max(matrix[i][wt], matrix[i-1][wt])  # From top
            
            if matrix[i-1][wt]:
                add_forward(matrix[i-1][wt] + values[i], i, wt + cost, matrix)

            maximum = max(maximum, matrix[i][wt])

    for i, row in enumerate(matrix):
        pretty_print(row)
    return maximum


@timing
def simple_solution(limit, weights, values):
    possible_ways = []
    maximum = 0
    
    for i, weight in enumerate(weights):
        more_ways = []
        for way in possible_ways:
            if weight + way[0] <= limit:
                more_ways.append([weight + way[0], values[i] + way[1]])
                # Append the current item
                maximum = max(maximum, values[i] + way[1])
        if weight <= limit:
            more_ways.append([weight, values[i]])
            maximum = max(maximum, values[i])

        possible_ways.extend(more_ways)

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
# res1 = knapSack(W, weights, values)
# res2 = matrix_based_solution(W, weights, values)
# res3 = simple_solution(W, weights, values)
# print(res1, res2, res3)

for x in range(100):
    W = utils.an_int([2, 900])
    n = utils.an_int([5, 900])
    weights = utils.array_of_random_ints(n, [1, 90], 2)
    values = utils.array_of_random_ints(n, [1, 80])

    # print("size", n)
    # print(W, weights, values)
    res1 = knapSack(W, weights, values)

    # print("Knapsack", res1)

    res3 = knapSack2(W, weights, values)
    # print("KnapSack2", res3)

    res2 = matrix_based_solution(W, weights, values)

    # print("Solve1", res2)
    
    if not (res1 == res2 == res3):
        print("Found------------------------")
        print(res1, res2, res3)
        print(W, weights, values)
        print("EndFound------------------------")
    print("......................................................")


utils.print_timings()