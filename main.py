from tkinter import W
import igraph as g
import numpy as np
import data_structures
import utils

if __name__ == "__main__":
    lines = np.loadtxt("input/input_1.txt", dtype='i',
                       delimiter=",", unpack=False)
    print("Loading input adjacency matrix ... ")
    utils.print_matrix(lines)

    adj_list = data_structures.AdjacencyList(size=len(lines))
    adj_matrix = data_structures.AdjacencyMatrix(matrix=lines, size=len(lines))
    inc_matrix = data_structures.IncidenceMatrix(matrix=lines, size=len(lines))

    adj_list.adjacency_dictionary = adj_matrix.to_adjacency_list()
    print(adj_list)
    inc_matrix.in_matrix = adj_matrix.to_incidence_matrix()
    print(inc_matrix)

    data = adj_list.generate_graph_data()
    # print(data)
    graph = g.Graph(data)
    # graph.add_vertices(12)
    # graph.TupleList(data)
    g.plot(graph, layout = 'circle', directed = False)