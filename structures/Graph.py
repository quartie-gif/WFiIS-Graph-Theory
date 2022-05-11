import random
import igraph as ig
import utils
from structures import AdjacencyList, DistanceMatrix, WeightMatrix
import heapq as hq
import math


class Graph:
    '''Class that represents a graph'''

    def __init__(self, vertices: int = 0, edges: list = [], directed: bool = False, weighted: bool = False):
        self.number_of_vertices = vertices
        self.edges = edges
        self.directed = directed
        self.weighted = weighted
        # weighted edges are stored in a list of tuples according to the order of the self.edges
        self.weighted_edges = []

    def __str__(self):
        return_string = ''
        for i in range(len(self.edges)):
            return_string += str(i) + ': ' + str(self.edges[i]) + '\n'
        return return_string

    def generate_graph_data(self):
        '''Generate a graph data for plotting'''
        data = []
        for edge in self.edges:
            if self.directed:
                data.append((edge[0], edge[1]))
            else:
                if (edge[1], edge[0]) not in data:
                    data.append((edge[0], edge[1]))
        return data

    def randomize_weights(self, start: int, stop: int):
        '''Generate random weights for the edges'''
        self.weighted_edges.clear()
        for _ in range(len(self.edges)):
            self.weighted_edges.append(random.randint(start, stop))

    @staticmethod
    def generate_random_weights(start: int, stop: int, size: int):
        '''Generate random weights for the edges'''
        weights = []
        for _ in range(size):
            weights.append(random.randint(start, stop))
            # print(weights)
        return weights

    @staticmethod
    def generate_random_graph_ve(number_of_vertices: int, number_of_edges: int, weighted=False, directed=False):
        '''
        vertices: int - number of vertices
        edges: int - number of edges
        '''

        if number_of_vertices < 0 or number_of_edges < 0:
            raise ValueError('Invalid number of edges')

        if directed:
            if number_of_edges > number_of_vertices * (number_of_vertices - 1):
                raise ValueError('Too many edges')
        else:
            if number_of_edges > (number_of_vertices * (number_of_vertices - 1)/2):
                raise ValueError('Too many edges')
        random_graph = Graph()
        random_graph.number_of_vertices = number_of_vertices
        random_graph.directed = directed
        random_graph.weighted = weighted
        random_graph.edges = []
        while(random_graph.edges.__len__() < number_of_edges):
            random_u_1 = random.randint(0, number_of_vertices-1)
            random_u_2 = utils.random_choice_except(
                number_of_vertices, random_u_1)
            # print(f'''random_u_1: {random_u_1}, random_u_2: {random_u_2}''')
            if (random_u_1, random_u_2) not in random_graph.edges:
                random_graph.edges.append((random_u_1, random_u_2))

            if not random_graph.directed:
                # get rid of duplicates in undirected graph
                random_graph.edges = random_graph.get_edges()
        return random_graph

    @staticmethod
    def generate_random_graph_vp(vertices: int, probability: float, weighted=False, directed=False):
        '''
        vertices: int - number of vertices
        probability: float - given probability of generating each edge
        '''

        if probability < 0.0 or probability > 1.0:
            raise ValueError("Error, value of probability is invalid!")

        if vertices <= 0:
            raise ValueError('Invalid number of vertices')

        random_graph = Graph()
        random_graph.weighted = weighted
        random_graph.directed = directed
        random_graph.number_of_vertices = vertices
        random_graph.edges = []

        for vertice in range(vertices):
            for vertice_to_align in range(vertices):
                if vertice_to_align != vertice:
                    # print("vertice_to_align = ", vertice_to_align)
                    # print("vertice = ", vertice)
                    random_probability = random.random()
                    if random_probability <= probability:
                        if directed:
                            random_graph.edges.append(
                                (vertice, vertice_to_align))
                        else:
                            random_graph.edges.append(
                                (vertice, vertice_to_align))
                            # get rid of duplicates for undirected graphs
                            random_graph.edges = random_graph.get_edges()

                    #    print(f'''vertice: {vertice}, inner_vertice: {vertice_to_align}''')
        if random_graph.weighted:
            random_graph.randomize_weights(1, 10)
        return random_graph

    # zestaw 2
    @staticmethod
    def generate_k_regular_graph(vertices: int, k: int):
        if vertices < 0 or k < 0 or k > vertices-1 or (k*vertices) % 2 != 0:
            raise ValueError('Invalid number of edges')

        regular_graph = Graph()
        regular_graph.number_of_vertices = vertices
        regular_graph.edges = []

        if vertices % 2 == 0:
            if k % 2 == 0:
                step = 1
                for _ in range(k//2):
                    for i in range(vertices):
                        regular_graph.edges.append(
                            (i % vertices, (i+step) % vertices))
                    step += 1
            else:
                step = vertices//2
                for _ in range(k//2+1):
                    for i in range(vertices):
                        regular_graph.edges.append(
                            (i % vertices, (i+step) % vertices))
                    step -= 1
        else:
            step = 1
            while step < k:
                for i in range(vertices):
                    regular_graph.edges.append(
                        (i % vertices, (i+step) % vertices))
                step += 2

        return regular_graph

    def is_connected(self, edges: list = []):
        '''Check if graph is connected'''
        if self.number_of_vertices == 0:
            return False
        if self.directed:
            return self.is_connected_directed()
        else:
            return self.is_connected_undirected()

    def is_connected_directed(self):
        '''Check if graph is directed connected'''
        # TODO: implement this method for directed graphs
        pass

    def is_connected_undirected(self):
        '''Check if graph is undirected connected'''
        visited_vertices = [False for _ in range(self.number_of_vertices)]
        for edge in self.edges:
            visited_vertices[edge[0]] = True
            visited_vertices[edge[1]] = True
        for visited_vertex in visited_vertices:
            if not visited_vertex:
                return False
        return True

    def vertex_labels(self):
        '''Generate vertex labels'''
        labels = [i for i in range(self.number_of_vertices)]
        return labels

    def to_adjacency_list(self):
        '''Convert a graph to adjacency list'''
        adj_list = AdjacencyList(self.number_of_vertices)
        for edge in self.edges:
            adj_list.insert(edge[0], edge[1])
        return adj_list

    def to_weight_matrix(self):
        '''Convert a graph to weight matrix'''
        weight_matrix = WeightMatrix.WeightMatrix(self.number_of_vertices)
        for i, edge in enumerate(self.generate_graph_data()):
            weight_matrix.insert(edge[0], edge[1], self.weighted_edges[i])
        return weight_matrix

    def plot(self, weighted: bool = False, directed: bool = False, layout='auto'):
        '''Plot and display graph'''
        data_to_visualize = self.generate_graph_data()

        if weighted:
            graph_visualization = ig.Graph(
                data_to_visualize)
            graph_visualization.es["weights"] = self.weighted_edges
            graph_visualization.es["label"] = self.weighted_edges
        graph_visualization = ig.Graph(data_to_visualize)
        # print(self.vertex_labels())
        graph_visualization.vs["label"] = self.vertex_labels()
        # print(graph_visualization.get_edgelist())

        ig.plot(graph_visualization, layout=layout,
                directed=directed, weighted=weighted)

    def get_vertices(self):
        '''Return list of all vertices'''
        return [i for i in range(self.number_of_vertices)]

    def get_directed_edges(self):
        '''Return list of all directed edges'''
        return [edge for edge in self.edges if self.directed]

    def get_undirected_edges(self):
        '''Return list of all undirected edges'''
        data = []
        for edge in self.edges:
            if self.directed:
                data.append((edge[0], edge[1]))
            else:
                if (edge[1], edge[0]) not in data:
                    data.append((edge[0], edge[1]))
        return data

    def get_edges(self):
        '''Return list of all edges'''
        if self.directed:
            return self.get_directed_edges()
        else:
            return self.get_undirected_edges()

    def count_edges_directed(self):
        pass

    def count_edges_undirected(self):
        adj_list = self.to_adjacency_list()
        count = 0
        for vertex in range(self.number_of_vertices):
            count += len(adj_list.adjacency_dictionary[vertex])
        return int(count / 2)

    def count_edges(self):
        '''Return number of edges'''

        if self.directed:
            return self.count_edges_directed()
        else:
            return self.count_edges_undirected()

    def get_neighbors(self, vert: int):
        '''Return list od neighburs of given vertice'''
        def is_connected(x): return vert == x[0] or vert == x[1]
        edges = list(filter(is_connected, self.edges))
        out = [edge[0] if vert == edge[1] else edge[1] for edge in edges]
        return out

    def amount_of_vertices(self):
        return self.number_of_vertices

    def get_list_vertices(self):
        return [i for i in range(self.number_of_vertices)]

    # zestaw 2
    def randomize(self, times: int = 1):
        '''Randomize graph given times'''
        for i in range(times):
            to_change = len(self.edges)/2
            while to_change > 0:
                rand_1 = random.randint(0, len(self.edges)-1)
                rand_2 = utils.random_choice_except(len(self.edges), rand_1)
                edge_1 = self.edges[rand_1]
                edge_2 = self.edges[rand_2]
                new_1, new_2 = (edge_1[0], edge_2[1]), (edge_2[0], edge_1[1])
                if (
                    new_1[0] != new_1[1] and new_2[0] != new_2[1]
                    and new_1 not in self.edges and new_2 not in self.edges
                    and (new_1[1], new_1[0]) not in self.edges
                    and (new_2[1], new_2[0]) not in self.edges
                ):
                    self.edges[rand_1], self.edges[rand_2] = new_1, new_2
                    to_change -= 1

    def get_shortest_path_directed(self, start_vertex: int, print_solutions: bool = False):
        '''Return shortest path from start to all other vertices'''
        # TODO implement this method for directed graphs
        pass

    def minDistance(self, dist, p_s):
        min = math.inf
        for v in range(self.number_of_vertices):
            if dist[v] < min and p_s[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def get_shortest_path_undirected(self, src: int, print_solutions: bool = False):

        weight_matrix = self.to_weight_matrix()
        d_s = [math.inf] * self.number_of_vertices
        d_s[src] = 0
        parent = [-1] * self.number_of_vertices
        p_s = [False] * self.number_of_vertices
        for _ in range(self.number_of_vertices):

            u = self.minDistance(d_s, p_s)

            p_s[u] = True

            for v in range(self.number_of_vertices):
                if (weight_matrix[u][v] > 0 and
                   p_s[v] == False and
                   d_s[v] > d_s[u] + weight_matrix[u][v]):
                    d_s[v] = d_s[u] + weight_matrix[u][v]
                    parent[v] = u
        if print_solutions:
            self.printSolution(d_s, parent)
        return d_s

    def printPath(self, parent, j):

        if parent[j] == -1:
            print(j, end="-")
            return
        self.printPath(parent, parent[j])
        print(j, end="-")

    def printSolution(self, dist, parent: list):
        for i in range(1, len(dist)):
            print(f'\nd({i}) = {dist[i]} ==>\t', end=" ")
            self.printPath(parent, i)
        print('\n')

    def get_shortest_path(self, start: int, print_solutions: bool = False):
        '''Return shortest path between start and end vertices'''
        if self.directed:
            return self.get_shortest_path_directed(start, print_solutions)
        else:
            return self.get_shortest_path_undirected(start, print_solutions)

    def to_distance_matrix(self):
        '''Return distance matrix'''
        dist_matrix = DistanceMatrix.DistanceMatrix(self.number_of_vertices)
        for i in range(self.number_of_vertices):
            row_to_append = self.get_shortest_path(i)
            # print("From vertex {} to all other vertices:".format(i))
            # print(row_to_append)
            for j in range(self.number_of_vertices):
                dist_matrix.set(i, j, row_to_append[j])
        return dist_matrix

    def get_center_vertices(self):
        '''Return the center vertice'''
        dist_matrix = self.to_distance_matrix()
        min_sum = math.inf
        center = 0
        for element in range(dist_matrix.size):
            sum = 0
            for i in range(dist_matrix.size):
                sum += dist_matrix.get(element, i)
            if sum < min_sum:
                min_sum = sum
                center = element
        return center, min_sum

    def get_center_minimax(self):
        '''Return the center vertice'''
        min_distance = math.inf
        center = 0
        for vertex in range(self.number_of_vertices):
            max_distance_from_vertex = max(self.get_shortest_path(vertex))
            if max_distance_from_vertex < min_distance:
                min_distance = max_distance_from_vertex
                center = vertex
        return center, min_distance

    def find_min_spanning_tree_undirected(self):
        '''Return the minimum spanning tree'''
        weight_matrix = self.to_weight_matrix()
        selected_vertices = [0 for _ in range(self.number_of_vertices)]
        counter = 0
        selected_vertices[0] = True
        while (counter < self.number_of_vertices - 1):
            minimum = math.inf
            from_vertex = to_vertex = 0
            for i in range(self.number_of_vertices):
                if selected_vertices[i]:
                    for j in range(self.number_of_vertices):
                        if ((not selected_vertices[j]) and weight_matrix[i][j]):
                            if minimum > weight_matrix[i][j]:
                                minimum = weight_matrix[i][j]
                                from_vertex = i
                                to_vertex = j
            print(str(from_vertex) + " -> " + str(to_vertex) +
                  " :\t" + str(weight_matrix[from_vertex][to_vertex]))
            selected_vertices[to_vertex] = True
            counter += 1

    def find_min_spanning_tree_directed():
        # TODO  implement this method for directed graphs
        pass

    def find_min_spanning_tree(self):
        if self.directed:
            return self.find_min_spanning_tree_directed()
        else:
            return self.find_min_spanning_tree_undirected()

    def degree(self, vert: int):
        '''Return degree of a given vertex'''
        return sum(i.count(vert) for i in self.edges)
