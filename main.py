from tkinter import W
import igraph as g
import numpy as np
from data_structures import *
import utils

if __name__ == "__main__":

    # 1
    lines = np.loadtxt("input/input_1.txt", dtype='i',
                       delimiter=",", unpack=False)
    print("Loading input adjacency matrix ... ")
    utils.print_matrix(lines)

    adj_list = AdjacencyList(size=len(lines))
    adj_matrix = AdjacencyMatrix(matrix=lines, size=len(lines))
    inc_matrix = IncidenceMatrix(matrix=lines, size=len(lines))

    adj_list.adjacency_dictionary = adj_matrix.to_adjacency_list()
    print(adj_list)
    inc_matrix.in_matrix = adj_matrix.to_incidence_matrix()
    print(inc_matrix)

    # 2
    data_to_visualize = adj_list.generate_graph_data()
    graph_visualization = g.Graph(data_to_visualize)
    graph_visualization.vs["label"] = adj_list.vertex_labels()

    graph_visualization.simplify()
    # g.plot(graph_visualization, layout = 'circle', directed = False)

    # 3
    graph = Graph.generate_random_graph(vertices=5, edges=8)
    print(graph)
    data_to_visualize = graph.generate_graph_data()
    graph_visualization = g.Graph(data_to_visualize)
    graph_visualization.vs["label"] = graph.vertex_labels()
    graph_visualization.simplify()
    g.plot(graph_visualization, layout='circle', directed=False)
