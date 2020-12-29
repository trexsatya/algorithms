import pprint
from collections import namedtuple
from enum import Enum
from tabulate import tabulate
import pandas as pd
from tkinter import *
from basics.utils import print_matrix


class From(Enum):
    TOP = 0
    TOP_LEFT = 1
    ARRAY = 2


class Data:
    min = None
    comes_from = None

    def __init__(self, mn, cf):
        self.min = abs(mn)
        self.comes_from = cf

    def __repr__(self):
        return f"{self.min}/{self.comes_from}"


def partition(array):
    S = sum(array)
    matrix = [[None for s in range(S+1)] for x in array]

    first_number = array[0]
    matrix[0][first_number] = Data(S - 2 * first_number, From.ARRAY)

    for i in range(1, len(array)):
        num = array[i]
        for j, val in enumerate(matrix[i-1]):
            if val:
                matrix[i][j] = Data(val.min, From.TOP)
                new_val = Data(S - 2 * (j+num), From.TOP_LEFT)
                # Complicacy
                matrix[i][j+num] = new_val
            if not matrix[i][num]:
                matrix[i][num] = Data(S - 2 * num, From.ARRAY)

    print_matrix(matrix, array)


class Solution:
    def find_min(self, x, y=None, z=None):
        if x and y and z:
            x = abs(x)
            y = abs(y)
            z = abs(z)
            return min(x, y, z)
        if x is not None and y is not None:
            x = abs(x)
            y = abs(y)
            return min(x, y)
        return x

    def minDiffernce(self, array, n):
        S = sum(array)

        matrix = [[10000 for s in range(S + 1)] for x in array]

        first_number = array[0]
        matrix[0][first_number] = (S - 2 * first_number)
        for i in range(first_number, S+1):
            matrix[0][i] = matrix[0][first_number]

        minimum = matrix[0][first_number]

        for i in range(1, len(array)):
            num = array[i]
            matrix[i][num] = S - 2 * num
            for j, val in enumerate(matrix[i - 1]):
                matrix[i][j] = self.find_min(matrix[i - 1][j],
                                   matrix[i - 1][j-1], # top
                                   matrix[i][j]
                                   )
                minimum = self.find_min(minimum, matrix[i][j])

        print_matrix(matrix, row_ids=array)
        return minimum


ar = [1, 6, 11, 5]
print(Solution().minDiffernce(ar, len(ar)))
print(partition(ar))


