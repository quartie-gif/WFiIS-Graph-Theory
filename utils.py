import numpy as np


def print_matrix(matrix: list):
    '''Function to print a matrix in a nice way'''
    return_string = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            return_string += str(matrix[i][j]) + ' '
        return_string += '\n'
    print(return_string)


def random_choice_except(range: int, excluding: int, size=None, replace=True):
    '''Function to generate a random choice from a list of integers, excluding a given integer'''
    choices = np.random.choice(range-1, size, replace=replace)
    return choices + (choices >= excluding)
