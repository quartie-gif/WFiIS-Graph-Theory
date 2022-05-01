import numpy as np
from . import AdjacencyMatrix


class IncidenceMatrix:
    '''Representation of a graph as incidence matrix'''

    def __init__(self, matrix: list, size: int):
        self.in_matrix = matrix
        self.size = size

    def __str__(self):
        return_string = ''
        for i in range(self.size):
            for j in range(self.size):
                return_string += str(self.in_matrix[i][j]) + ' '
            return_string += '\n'
        return return_string

    def to_adjacency_matrix(self):
        '''Convert incidence matrix to adjacency matrix'''
        adjacency_matrix = np.zeros((self.size, self.size), dtype=int)
        n1 = -1
        n2 = -1
        self.in_matrix = np.transpose(self.in_matrix)
        for i in range(self.size):
            for j in range(len(self.in_matrix[i])):
                if self.in_matrix[i][j] == 1:
                    if n1 == -1:
                        n1 = j
                    else:
                        n2 = j
            adjacency_matrix[n1][n2] = 1
            adjacency_matrix[n2][n1] = 1
            n1 = -1
            n2 = -1

    def to_adjacency_list(self):
        '''Convert incidence matrix to adjacency list'''
        adj_matrix = self.incidence_to_adjacency(self.in_matrix)
        adj_list = AdjacencyMatrix.adjacency_to_list(adj_matrix)
        return adj_list
