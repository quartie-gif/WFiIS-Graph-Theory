import numpy as np


class AdjacencyMatrix:
    '''Representation of a graph as adjacency matrix'''

    def __init__(self, matrix: list, size: int):

        self.adj_matrix = matrix
        self.size = size

    def __str__(self):
        return_string = ''
        for i in range(self.size):
            for j in range(self.size):
                return_string += str(self.adj_matrix[i][j]) + ' '
            return_string += '\n'
        return return_string

    def to_incidence_matrix(self):
        '''Converts the adjacency matrix to incidence matrix'''
        incidence_matrix = []
        for i in range(self.size):
            for j in range(i, self.size):
                if self.adj_matrix[i][j] == 1:
                    incidence_matrix.append(
                        np.zeros(self.size, dtype=int))
                    incidence_matrix[-1][i] = 1
                    incidence_matrix[-1][j] = 1
        incidence_matrix = np.transpose(incidence_matrix)
        return incidence_matrix

    def to_adjacency_list(self):
        '''Converts the adjacency matrix to adjacency list'''
        neighbours_list = dict()
        for i, line in enumerate(self.adj_matrix):
            for j in range(len(line)):
                if self.adj_matrix[i][j] == 1:
                    neighbours_list.setdefault(i, []).append(int(j))
        return neighbours_list
