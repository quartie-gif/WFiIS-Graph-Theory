from tkinter import W
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
    # graph = Graph.generate_random_graph_ve(vertices=6, edges=10)
    # graph.plot()

    # print('zad 1.3b')
    # random_probability_graph = Graph.generate_random_graph_vp(6, 0.3)
    # random_probability_graph.plot()

    # print( 'zad 2.1' )
    # str_1 = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    # str_2 = [4, 4, 3, 1, 2]
    # print( "Czy ciag graficzny:" )
    # print( "str_1: ", is_graphical_string(str_1) )
    # print( "str_2: ", is_graphical_string(str_2) )
    # graph = string_to_graph(str_1)
    # graph.plot()
    
    # print('zad 2.2')
    # graph.randomize(2)
    # graph.plot()

    # print('zad 2.3')
    # print( components_listing(graph) )

    # print('zad 2.4')
    # str_3 = [ 4, 2, 6, 2, 6, 2, 4, 2 ]
    # graph = string_to_graph(str_3)
    # graph.plot()
    # print( eulerian_cycle(graph) )

    # print('zad 2.5')
    # k_regular_graph = Graph.generate_k_regular_graph(4, 1)
    # k_regular_graph.plot()

    # k_regular_graph = Graph.generate_k_regular_graph(4, 2)
    # k_regular_graph.plot()

    # k_regular_graph = Graph.generate_k_regular_graph(4, 3)
    # k_regular_graph.plot()

    # k_regular_graph = Graph.generate_k_regular_graph(8, 1)
    # k_regular_graph.plot()

    # k_regular_graph = Graph.generate_k_regular_graph(8, 3)
    # k_regular_graph.plot()

    # k_regular_graph = Graph.generate_k_regular_graph(8, 5)
    # k_regular_graph.plot()

    # k_regular_graph = Graph.generate_k_regular_graph(7, 2)
    # k_regular_graph.plot()

    # k_regular_graph = Graph.generate_k_regular_graph(7, 4)
    # k_regular_graph.plot()

    # k_regular_graph = Graph.generate_k_regular_graph(7, 6)
    # k_regular_graph.plot()

    # print('zad 2.6')
    for i in range(10):
        k_regular_graph = Graph.generate_k_regular_graph(8, 3)
        k_regular_graph.randomize()
        k_regular_graph.plot()
        k_regular_graph.plot()
        print( hamilotnian_cycle(k_regular_graph) )





