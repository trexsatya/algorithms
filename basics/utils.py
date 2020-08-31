import math
import random


def an_int(within=None):
    if within is None:
        within = [-5000, + 5000]
    return random.randint(within[0], within[1])


def array_of_random_ints(size, within=None):
    if within is None:
        within = [-5000, + 5000]

    return [random.randint(within[0], within[1]) for x in range(size)]