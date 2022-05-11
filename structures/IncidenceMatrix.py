import numpy as np
from . import AdjacencyMatrix


class IncidenceMatrix:
    '''Representation of a graph as incidence matrix'''

    def __init__(self, matrix: list, row_size: int, column_size: int):
        self.in_matrix = matrix
        self.row_size = row_size
        self.column_size = column_size

    def __str__(self):
        return_string = ''
        for i in range(self.row_size):
            for j in range(self.column_size):
                return_string += str(self.in_matrix[i][j]) + ' '
            return_string += '\n'
        return return_string

    def to_adjacency_matrix(self):
        '''Convert incidence matrix to adjacency matrix'''
        adjacency_matrix = np.zeros((self.row_size, self.row_size), dtype=int)
        for j in range(self.column_size):
            edge = []
            for i in range(self.row_size):
                if self.in_matrix[i][j] == 1:
                    print(self.in_matrix)
                    edge.append(i)
            edge.sort()
            if len(edge) == 2:
                adjacency_matrix[edge[0]][edge[1]] = 1
                adjacency_matrix[edge[1]][edge[0]] = 1
        return AdjacencyMatrix.AdjacencyMatrix(matrix=adjacency_matrix, size=self.row_size)

    def to_adjacency_list(self):
        '''Convert incidence matrix to adjacency list'''
        adj_matrix = self.to_adjacency_matrix()
        adj_list = adj_matrix.to_adjacency_list()
        return adj_list
