import functools
from basics.utils import timing, print_timings

# decimal("01" + "10" + "11" + "100" + ...) 1 to N


def collect_position_of_ones(bin_str_of_i):
    accumulated = []
    for idx, letter in enumerate(bin_str_of_i):
        if letter == '1':
            accumulated.append(len(bin_str_of_i) - idx -1)
    return accumulated


@timing
def decimal(n):
    accumulated = []
    mod = (pow(10, 9) + 7)
    accumulated_sum = 0

    size = 0
    for i in range(1, n+1):
        if i & (i-1) == 0:
            size += 1
        accumulated_sum = ((accumulated_sum << size) | i) % mod

    # tot = 0
    # for x in accumulated:
    #     tot += (pow(2, x) % mod)

    # print(accumulated_sum)
    return accumulated_sum % mod


# print(collect_position_of_ones("111"))


print(decimal(100000000))

# print_timings()