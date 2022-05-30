from ui_managment import *

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

def main_debug():
    is_running = True
    while(is_running):
        choice = main_menu()
        is_running = match_set(choice)


if __name__ == "__main__":
    main()
