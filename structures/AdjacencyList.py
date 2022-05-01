import numpy as np


class AdjacencyList:
    '''Representation of a graph as adjacency list'''

    def __init__(self, size: int):
        self.size = size
        self.adjacency_dictionary = dict()

    def __str__(self):
        return_string = ''
        for (key, value) in self.adjacency_dictionary.items():
            return_string += str(key) + ': ' + str(value) + '\n'
        return return_string

    def vertex_labels(self):
        '''Generate vertex labels for plotting'''
        labels = [i for i in range(self.size)]
        return labels

    def insert(self, key: int, val: int):
        '''Insert a new edge into the adjacency list'''
        self.adjacency_dictionary.setdefault(key, [])
        self.adjacency_dictionary.setdefault(val, [])
        if val not in self.adjacency_dictionary[key]:
            self.adjacency_dictionary[key].append(int(val))
        if key not in self.adjacency_dictionary[val]:
            self.adjacency_dictionary[val].append(int(key))

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

    def generate_graph_data(self, directed: bool = False):
        '''Generate graph data for plotting'''
        data = []
        for (key, value) in self.adjacency_dictionary.items():
            for val in value:
                if directed:
                    data.append((key, val))
                else:
                    if not (value, key) in data:
                        data.append((key, val))
        return data
