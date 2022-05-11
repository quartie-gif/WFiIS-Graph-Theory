import numpy as np

from structures import AdjacencyList
from structures.IncidenceMatrix import IncidenceMatrix


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
        adj_list = self.to_adjacency_list()
        return  adj_list.to_incidence_matrix()

    def to_adjacency_list(self):

        adjacency_list = AdjacencyList.AdjacencyList(size=self.size)
        neighbours_list = dict()
        for i, line in enumerate(self.adj_matrix):
            for j in range(len(line)):
                if self.adj_matrix[i][j] == 1:
                    neighbours_list.setdefault(i, []).append(int(j))
        adjacency_list.adjacency_dictionary = neighbours_list
        return adjacency_list
