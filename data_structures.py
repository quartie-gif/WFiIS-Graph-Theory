import numpy as np
import random
import utils
import igraph as g
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
        labels = [ i for i in range(self.size) ]
        return labels

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


class Graph:
    '''Class that represents a graph'''

    def __init__(self, vertices: int = 0, edges: list = []):
        self.vertices = vertices
        self.edges = edges

    def __str__(self):
        return_string = ''
        for i in range( len(self.edges) ):
            return_string += str(i) + ': ' + str(self.edges[i]) + '\n'
        return return_string

    def generate_graph_data(self):
        '''Generate a graph data for plotting'''
        data = []
        for edge in self.edges:
            data.append((edge[0], edge[1]))
        return data

    @staticmethod
    def generate_random_graph_ve(vertices: int, edges: int):
        '''
        vertices: int - number of vertices
        edges: int - number of edges
        '''

        if vertices < 0 or edges < 0:
            raise ValueError('Invalid number of edges')

        random_graph = Graph()
        random_graph.vertices = vertices
        random_graph.edges = []
        print('edges = ', edges)
        for i in range(edges):
            random_u_1 = random.randint(0, vertices-1)
            random_u_2 = utils.random_choice_except(vertices, random_u_1)
            # print(f'''random_u_1: {random_u_1}, random_u_2: {random_u_2}''')
            if (random_u_1, random_u_2) not in random_graph.edges:
                random_graph.edges.append((random_u_1, random_u_2))
            else:
                i -= 1
        return random_graph

    @staticmethod
    def generate_random_graph_vp(vertices: int, probability: float):
        '''
        vertices: int - number of vertices
        probability: float - given probability of generating each edge
        '''
        
        if probability < 0.0 or probability > 1.0:
            raise ValueError("Error, value of probability is invalid!")
        
        if vertices<=0:
            raise ValueError('Invalid number of vertices')

        random_graph = Graph()
        random_graph.vertices = vertices
        random_graph.edges = []
        
        for vertice in range(vertices):
            for vertice_to_align in range(vertices):
                if vertice_to_align != vertice:
                    random_probability = random.random()
                    if random_probability < probability: 
                       random_graph.edges.append((vertice_to_align, vertice))
                    #    print(f'''vertice: {vertice}, inner_vertice: {vertice_to_align}''')
        return random_graph

    #zestaw 2
    @staticmethod
    def generate_k_regular_graph(vertices: int, k: int):
        if vertices < 0 or k < 0 or k > vertices-1 or (k*vertices)%2 != 0:
            raise ValueError('Invalid number of edges')

        regular_graph = Graph()
        regular_graph.vertices = vertices
        regular_graph.edges = []

        if vertices%2 == 0:
            if k%2 == 0:
                step = 1
                for _ in range(k//2):
                    for i in range(vertices):
                        regular_graph.edges.append( (i%vertices, (i+step)%vertices) )
                    step += 1
            else:
                step = vertices//2 
                for _ in range(k//2+1):
                    for i in range(vertices):
                        regular_graph.edges.append( (i%vertices, (i+step)%vertices) )
                    step -= 1
        else:
            step = 1
            while step < k:
                for i in range(vertices):
                    regular_graph.edges.append( (i%vertices, (i+step)%vertices) )
                step += 2

        return regular_graph

    def vertex_labels(self):
        '''Generate vertex labels'''
        labels = [ i for i in range(self.vertices) ]
        return labels

    def to_adjacency_list(self):
        '''Convert a graph to adjacency list'''
        adj_list = AdjacencyList(self.vertices)
        for edge in self.edges:
            adj_list.insert(edge[0], edge[1])
        return adj_list

    def plot(self):
        '''Plot and display graph'''
        data_to_visualize = self.generate_graph_data()
        graph_visualization = g.Graph(data_to_visualize)
        graph_visualization.vs["label"] = self.vertex_labels()
        graph_visualization.simplify()
        g.plot(graph_visualization, layout='circle', directed=False)

    def get_vertices(self):
        '''Return list of all vertices'''
        return [ i for i in range(self.vertices) ]

    def get_edges(self):
        '''Return list of all edges'''
        return [ i for i in self.edges ]

    def get_neighbors(self, vert: int):
        '''Return list od neighburs of given vertice'''
        is_connected = lambda x: vert == x[0] or vert == x[1]
        edges = list( filter( is_connected, self.edges ) )
        out = [ edge[0] if vert == edge[1] else edge[1] for edge in edges]
        return out

    def amount_of_vertices(self):
        return self.vertices

    #zestaw 2
    def randomize(self, times: int=1):
        '''Randomize graph given times'''
        for i in range(times):
            to_change = len(self.edges)/2;
            while to_change > 0:
                rand_1 = random.randint(0, len(self.edges)-1)
                rand_2 = utils.random_choice_except(len(self.edges), rand_1)
                edge_1 = self.edges[rand_1]
                edge_2 = self.edges[rand_2]
                new_1, new_2 = (edge_1[0], edge_2[1]), (edge_2[0], edge_1[1])
                if  (   
                        new_1[0] != new_1[1] and new_2[0] != new_2[1] 
                        and new_1 not in self.edges and new_2 not in self.edges
                        and (new_1[1], new_1[0]) not in self.edges
                        and (new_2[1], new_2[0]) not in self.edges
                    ):
                    self.edges[rand_1], self.edges[rand_2] = new_1, new_2
                    to_change -= 1;

    def degree(self, vert: int):
        '''Return degree of a given vertex'''
        return sum( i.count(vert) for i in self.edges )

