from tkinter import W
from structures import *
from strings_cycles import *
import utils


def task_1():
    print('zad 1.1')
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

    print('zad 1.2')
    data_to_visualize = adj_list.generate_graph_data()
    print(data_to_visualize)
    graph = Graph(vertices=len(data_to_visualize)//2,
                  edges=data_to_visualize, directed=False)

    graph.plot(layout='circle', directed=False)

    print('zad 1.3a')
    graph = Graph.generate_random_graph_ve(vertices=8, edges=6)
    graph.plot()

    print('zad 1.3b')
    random_probability_graph = Graph.generate_random_graph_vp(6, 0.3)
    random_probability_graph.plot(layout='auto')


def task_2():
    # print( 'zad 2.1' )
    # str_1 = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    # str_2 = [4, 4, 3, 1, 2]
    # print( "Czy ciag graficzny:" )
    # print( "str_1: ", is_graphical_string(str_1) )
    # print( "str_2: ", is_graphical_string(str_2) )
    # graph = string_to_graph(str_1)
    # graph.plot(layout='auto')

    # print('zad 2.2')
    # graph.randomize()
    # graph.plot(layout='auto')

    # print('zad 2.3')
    # print( components_listing(graph) )

    print('zad 2.4')

    print('zad 2.5')
    k_regular_graph = Graph.generate_k_regular_graph(4, 1)
    k_regular_graph.plot()

    k_regular_graph = Graph.generate_k_regular_graph(4, 2)
    k_regular_graph.plot()

    k_regular_graph = Graph.generate_k_regular_graph(4, 3)
    k_regular_graph.plot()

    k_regular_graph = Graph.generate_k_regular_graph(8, 1)
    k_regular_graph.plot()

    k_regular_graph = Graph.generate_k_regular_graph(8, 3)
    k_regular_graph.plot()

    k_regular_graph = Graph.generate_k_regular_graph(8, 5)
    k_regular_graph.plot()

    k_regular_graph = Graph.generate_k_regular_graph(7, 2)
    k_regular_graph.plot()

    k_regular_graph = Graph.generate_k_regular_graph(7, 4)
    k_regular_graph.plot()

    k_regular_graph = Graph.generate_k_regular_graph(7, 6)
    k_regular_graph.plot()


def task_3():
    print('zad 3.1')
    graph = Graph.generate_random_graph_vp(
        vertices=10, probability=0.2, weighted=True, directed=False)
    while graph.is_connected() == False:
        graph = graph.generate_random_graph_vp(
            vertices=10, probability=0.2, weighted=True, directed=False)
    graph.plot(weighted=True, directed=False)

    print('zad 3.2')
    graph.get_shortest_path(0, print_solutions=True)

    print('zad 3.3')
    # Creating Distance Matrix
    dist_matrix = graph.to_distance_matrix()
    print(dist_matrix)

    print('zad 3.4')
    center, min_sum = graph.get_center_vertices()
    print(f'Centrum = {center} (suma odleglosci: {min_sum})')

    center_minimax, minimax = graph.get_center_minimax()
    print(
        f'Centrum minimax = {center_minimax} (odleglosc od najdalszego: {minimax})')


def main():
    # task_1()
    # task_2()
    task_3()


if __name__ == "__main__":
    main()
