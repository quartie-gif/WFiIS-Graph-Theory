import numpy as np


class AdjacencyList:
    '''Representation of a graph as adjacency list'''

    def __init__(self, size: int):
        self.size = size
        self.adjacency_dictionary = dict()

    def insert(self, key: int, val: int):
        '''Insert a new edge into the adjacency list'''
        self.adjacency_dictionary.setdefault(key, []).append(int(val))
        self.adjacency_dictionary.setdefault(val, []).append(int(key))

    def delete_edge(self, u: int, v: int):
        '''
        Delete an edge from the adjacency list
            u: int - source vertex
            v: int - destination vertex
        '''

        for i in range(self.size):
            if (self.adjacency_dictionary[u][i] == v):
                self.adjacency_dictionary[u].pop(i)
                break

        for i in range(self.size):
            if (self.adjacency_dictionary[v][i] == u):
                self.adjacency_dictionary[v].pop(i)
                break

    def to_incidence_matrix(self):
        '''Convert adjacency list to incidence matrix'''
        adjacency_matrix = self.list_to_adjacency(self.adjacency_dictionary)
        incidence_matrix = AdjacencyMatrix.adjacency_to_incidence(
            adjacency_matrix)
        return incidence_matrix

    def to_adjacency_matrix(self):
        '''Convert adjacency list to adjacency matrix'''
        adjacency_matrix = np.zeros((self.size, self.size), dtype=int)
        for j, k in enumerate(self.adjacency_dictionary.items()):
            for l in k:
                adjacency_matrix[j-1, l-1] = 1
        return adjacency_matrix

    def generate_graph_data(self):
        '''Generate graph data for plotting'''
        data = []
        for (key, value) in self.adjacency_dictionary.items():
            for val in value:
                data.append((key, val))
        return data

    def __str__(self):
        return_string = ''
        for (key, value) in self.adjacency_dictionary.items():
            return_string += str(key) + ': ' + str(value) + '\n'
        return return_string


class AdjacencyMatrix:
    '''Representation of a graph as adjacency matrix'''

    def __init__(self, matrix: list, size: int):

        self.adj_matrix = matrix
        self.size = size

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
                    neighbours_list.setdefault(i + 1, []).append(int(j+1))
        return neighbours_list

    def __str__(self):
        return_string = ''
        for i in range(self.size):
            for j in range(self.size):
                return_string += str(self.adj_matrix[i][j]) + ' '
            return_string += '\n'
        return return_string


class IncidenceMatrix:
    '''Representation of a graph as incidence matrix'''

    def __init__(self, matrix: list, size: int):
        self.in_matrix = matrix
        self.size = size

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

    def __str__(self):
        return_string = ''
        for i in range(self.size):
            for j in range(self.size):
                return_string += str(self.in_matrix[i][j]) + ' '
            return_string += '\n'
        return return_string

