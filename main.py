from ui_managment import *


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


def debug():
    number_of_vertices = int(
        input("Enter number of vertices: "))
    probability = float(input("Enter probability: "))
    graph = Graph.generate_random_graph_vp(
        number_of_vertices=number_of_vertices, probability=probability, weighted=True, directed=False)
    while True:
        graph = graph.generate_random_graph_vp(
            number_of_vertices=number_of_vertices, probability=probability, weighted=True, directed=False)
        print("graph.is_connected(): " + str(graph.is_connected()))

        if graph.is_connected():
            break
    graph.plot(layout='circle')

    graph.get_shortest_path(0, print_solutions=True)
    dist_matrix = graph.to_distance_matrix()
    print(dist_matrix)


def main():
    is_running = True
    while(is_running):
        try:
            choice = main_menu()
            is_running = match_set(choice)
        except Exception as e:
            print(e)
            os.system("pause")


if __name__ == "__main__":
    main()
    # debug()
# 1 2 4
# 0 2 3 4 6
# 5
# 1 6
# 6
# 1
# 5
