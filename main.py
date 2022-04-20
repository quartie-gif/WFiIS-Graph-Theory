from tkinter import W
import igraph as g
import numpy as np
from data_structures import *
from strings_cycles import *
import utils

if __name__ == "__main__":

    # print('zad 1.1')
    # lines = np.loadtxt("input/input_1.txt", dtype='i',
    #                    delimiter=",", unpack=False)
    # print("Loading input adjacency matrix ... ")
    # utils.print_matrix(lines)

    # adj_list = AdjacencyList(size=len(lines))
    # adj_matrix = AdjacencyMatrix(matrix=lines, size=len(lines))
    # inc_matrix = IncidenceMatrix(matrix=lines, size=len(lines))

    # adj_list.adjacency_dictionary = adj_matrix.to_adjacency_list()
    # print(adj_list)
    # inc_matrix.in_matrix = adj_matrix.to_incidence_matrix()
    # print(inc_matrix)

    # print('zad 1.2')
    # data_to_visualize = adj_list.generate_graph_data()
    # graph_visualization = g.Graph(data_to_visualize)
    # graph_visualization.vs["label"] = adj_list.vertex_labels()

    # graph_visualization.simplify()
    # g.plot(graph_visualization, layout = 'circle', directed = False)

    # print('zad 1.3a')
    # graph = Graph.generate_random_graph_ve(vertices=8, edges=6)
    # print(graph)
    # data_to_visualize = graph.generate_graph_data()
    # graph_visualization = g.Graph(data_to_visualize)
    # graph_visualization.vs["label"] = graph.vertex_labels()
    # graph_visualization.simplify()
    # g.plot(graph_visualization, layout='circle', directed=False)

    # print('zad 1.3b')
    # random_probability_graph = Graph.generate_random_graph_vp(6, 0.3)
    # data_to_visualize = random_probability_graph.generate_graph_data()
    # graph_visualization = g.Graph(data_to_visualize)
    # graph_visualization.vs["label"] = random_probability_graph.vertex_labels()
    # graph_visualization.simplify()
    # g.plot(graph_visualization, layout='circle', directed=False)

    print('zad 2.1')
    str_1 = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    str_2 = [4, 4, 3, 1, 2]
    print("Czy ciag graficzny:")
    print("str_1: ", is_graphical_string(str_1) )
    print("str_2: ", is_graphical_string(str_2) )

    graph = string_to_graph(str_1)
    data_to_visualize = graph.generate_graph_data()
    graph_visualization = g.Graph(data_to_visualize)
    graph_visualization.vs["label"] = graph.vertex_labels()
    graph_visualization.simplify()
    g.plot(graph_visualization, layout='circle', directed=False)

    print('zad 2.2')
    graph.randomize()
    data_to_visualize = graph.generate_graph_data()
    graph_visualization = g.Graph(data_to_visualize)
    graph_visualization.vs["label"] = graph.vertex_labels()
    graph_visualization.simplify()
    g.plot(graph_visualization, layout='circle', directed=False)


