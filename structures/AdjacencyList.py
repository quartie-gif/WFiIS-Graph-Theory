import numpy as np

from structures import AdjacencyMatrix
from structures.IncidenceMatrix import IncidenceMatrix


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
        node_count = len(self.adjacency_dictionary)
        edge_count = 0
        for parent_vertex, vertices in self.adjacency_dictionary.items():
            edge_count += len(vertices)
        edge_count = edge_count // 2
        incident_matrix = np.zeros((node_count, edge_count), dtype=int)
        current_row = 0
        edge_index_map = {}
        for node_index in range(0, node_count):
            for neighbor_index in self.adjacency_dictionary[node_index]:
                edge = tuple(sorted([node_index, neighbor_index]))
                if edge not in edge_index_map:
                    edge_index_map[edge] = len(edge_index_map)
                edge_index = edge_index_map[edge]
                incident_matrix[node_index][edge_index] = 1
        return IncidenceMatrix(
            matrix=incident_matrix, row_size=node_count, column_size=edge_count)

    def to_adjacency_matrix(self):
        '''Convert adjacency list to adjacency matrix'''
        adjacency_matrix = np.zeros((self.size, self.size), dtype=int)
        for j, k in enumerate(self.adjacency_dictionary.items()):
            for l in range(len(k)):
                if j != k[l]:
                    adjacency_matrix[j, k[l]] = 1
        return AdjacencyMatrix.AdjacencyMatrix(matrix=adjacency_matrix, size=self.size)


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
