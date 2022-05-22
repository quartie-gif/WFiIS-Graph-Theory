from secrets import choice
from matplotlib.pyplot import plot
from structures import *
from strings_cycles import *
import utils
import os


def cls():
    '''Clear consol'''
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    cls()
    '''Function that clear consol and print header of user interface'''
    print("=================================================")
    print("||       Graphs and Their Uses - labs          ||")
    print("||                                             ||")
    print("||   Made by:                                  ||")
    print("||   K.Jagodzinski, L.Bartoszek, M.Piwek       ||")
    print("=================================================")


def main_menu():
    '''Print and let user choose which set wants to open'''
    print_header()
    print("=================== MAIN MENU ===================")
    print("||  Choose which set of excecices you want open:")
    print("||  (1) Set 1 - undirected graphs")
    print("||  (2) Set 2 - graph string, graph cycles")
    print("||  (3) Set 3 - weighted graphs")
    print("||  (4) Set 4 - directed graphs ")
    print("||  (5) Set 5 - unaviable")
    print("||  (6) Set 6 - unaviable")
    print("||  (0) Exit ")
    return int(input())


def match_set(choice: int):
    '''Matching choice to proper set of excecices'''
    if choice == 1:
        set1_choice()
        os.system("pause")
        return True
    elif choice == 2:
        set2_choice()
        os.system("pause")
        return True
    elif choice == 3:
        set3_choice()
        os.system("pause")
        return True
    elif choice == 4:
        set4_choice()
        os.system("pause")
        return True
    elif choice == 5:
        print('unaviable')
        os.system("pause")
        return True
    elif choice == 6:
        print('unaviable')
        os.system("pause")
        return True
    elif choice == 0:
        return False
    else:
        print('Unexpected choice')
        return True


def set1_choice():
    lines = np.loadtxt("input/input_1.txt", dtype='i',
                       delimiter=",", unpack=False)
    adj_matrix = AdjacencyMatrix(matrix=lines, size=len(lines))
    adj_list = adj_matrix.to_adjacency_list()
    inc_matrix = adj_list.to_incidence_matrix()
    while True:
        cls()
        '''Picker of excecices from set 1'''
        print_header()
        print("===================== SET 1 =====================")
        print("||  Choose which set of excecices you want open:")
        print("||  (1) Exercise 1")
        print("||  (2) Exercise 2")
        print("||  (3) Exercise 3")
        print("||  (0) Exit ")
        ex = int(input())
        if ex == 1:

            result = adj_matrix
            while True:
                cls()
                print("===================== SET 1 =====================")
                print("||  Choose which transformation you want open:")

                print("||  (1) Adjancency Matrix -> Adjacency list  ")
                print("||  (2) Adjancency Matrix -> Incidence Matrix")
                print("||  (3) Incidence Matrix  -> Adjacency list  ")
                print("||  (4) Incidence Matrix  -> Adjacency Matrix")
                print("||  (5) Adjacency List    -> Adjacency Matrix")
                print("||  (6) Adjacency List    -> Incidence Matrix")
                print("||  (0) Exit ")

                print("==================== RESULT =====================")
                print(result.__str__())

                option = int(input())
                if option == 1:
                    result = adj_matrix.to_adjacency_list()
                    cls()
                elif option == 2:
                    result = adj_matrix.to_incidence_matrix()
                    cls()
                elif option == 3:
                    result = inc_matrix.to_adjacency_list()
                    cls()
                elif option == 4:
                    result = inc_matrix.to_adjacency_matrix()
                    # cls()
                elif option == 5:
                    result = adj_list.to_adjacency_matrix()
                    cls()
                elif option == 6:
                    result = adj_list.to_incidence_matrix()
                    cls()
                elif option == 0:
                    break
                else:
                    print('Unexpected choice')

        elif ex == 2:
            data_to_visualize = adj_list.generate_graph_data()
            graph = Graph(vertices=len(adj_list.adjacency_dictionary),
                          edges=data_to_visualize, directed=False)

            graph.plot(layout='circle')

        elif ex == 3:
            while True:
                cls()
                print("===================== SET 1 =====================")
                print("||  Choose which transformation you want open:")

                print("||  (1) Model G(number_of_vertices, number_of_edges)")
                print("||  (2) Model G(number_of_vertices, probability)")
                print("||  (0) Exit ")

                option = int(input())
                if option == 1:
                    number_of_vertices = int(
                        input("Enter number of vertices: "))
                    number_of_edges = int(input("Enter number of edges: "))
                    graph = Graph.generate_random_graph_ve(
                        number_of_vertices=number_of_vertices, number_of_edges=number_of_edges)
                    graph.plot(layout='circle')
                    cls()
                elif option == 2:
                    number_of_vertices = int(
                        input("Enter number of vertices: "))
                    probability = float(input("Enter probability: "))
                    random_probability_graph = Graph.generate_random_graph_vp(
                        number_of_vertices=number_of_vertices, probability=probability)
                    random_probability_graph.plot(layout='circle')
                    cls()
                elif option == 0:
                    break
                else:
                    print('Unexpected choice')
        elif ex == 0:
            break
        else:
            print('Unexpected choice')


def set2_choice():
    '''Picker of excecices from set 2'''
    print_header()
    print("===================== SET 2 =====================")
    print("||  Choose which set of excecices you want open:")
    print("||  (1) Check if given string is graphical string")
    print("||  (2) Randomize graph")
    print("||  (3) Find greatest component of given graph")
    print("||  (4) Eulerian cycle/path")
    print("||  (5) Generate k-regular graph")
    print("||  (6) Hamiltonian cycle/path")
    ex = int(input())
    if ex == 1:
        print("Insert a string (pattern: 3 2 2 2 1): ")
        cin = input()
        in_str = list(map(int, list(cin.split(" "))))
        print("Is graphical string: ", is_graphical_string(in_str))
        if is_graphical_string(in_str):
            g = string_to_graph(in_str)
            g.plot()

    elif ex == 2:
        print("Insert a graphical string: ")
        cin = input()
        in_str = list(map(int, list(cin.split(" "))))
        if is_graphical_string(in_str):
            g = string_to_graph(in_str)
            g.plot(layout='circle')
            print("How many randomizations You wants to make? ")
            cin = input()
            g.randomize(int(cin))
            # g.plot()
        else:
            print("Given string is not graphical string")

    elif ex == 3:
        print("Insert a graphical string: ")
        cin = input()
        in_str = list(map(int, list(cin.split(" "))))
        if is_graphical_string(in_str):
            g = string_to_graph(in_str)
            g.plot(color_vs=all_components(g))
            print(components_listing(g))
        else:
            print("Given string is not graphical string")

    elif ex == 4:
        print("Insert a string (pattern: 3 2 2 2 1): ")
        cin = input()
        in_str = list(map(int, list(cin.split(" "))))
        g = string_to_graph(in_str)
        g.plot(layout='circle')
        print(eulerian_cycle(g))

    elif ex == 5:
        print("Insert n - verticles: ")
        n = int(input())
        print("Insert k - degree: ")
        k = int(input())
        g = Graph.generate_k_regular_graph(n, k)
        g.plot()

    elif ex == 6:
        while(True):
            print("Insert verticles: ")
            v = int(input())
            print("Insert edges: ")
            e = int(input())
            g = Graph.generate_random_graph_ve(v, e)
            g.plot()
            print('Is recived graph appropriate? [Yes/No]')
            is_ok = str(input())
            if is_ok == "Yes":
                break
        print(hamilotnian_cycle(g))

    else:
        print('Unexpected choice')


def set3_choice():

    def get_random_graph_with_user_input():
        number_of_vertices = int(
            input("Enter number of vertices: "))
        probability = float(input("Enter probability: "))
        graph = Graph()
        while True:
            graph = graph.generate_random_graph_vp(
                number_of_vertices=number_of_vertices, probability=probability, weighted=True, directed=False)
            if graph.is_connected():
                break
        graph.plot()
        return graph

    '''Picker of excecices from set 3'''
    print_header()
    print("===================== SET 3 =====================")
    print("||  Choose which set of excecices you want open:")
    print("||  (1) Exercise 1")
    print("||  (2) Exercise 2")
    print("||  (3) Exercise 3")
    print("||  (4) Exercise 4")
    print("||  (5) Exercise 5")
    ex = int(input())
    # graph = Graph()
    if ex == 1:
        graph = get_random_graph_with_user_input()

    elif ex == 2:
        graph = get_random_graph_with_user_input()
        start_vertex = int(
            input("Start: "))
        while(True):
            graph.get_shortest_path(start_vertex, print_solutions=True)
            are_ok = str(
                input('Are recieved shorthest paths appropriate? [Yes/No]'))
            if are_ok == "Yes":
                break

    elif ex == 3:
        graph = get_random_graph_with_user_input()
        while(True):
            dist_matrix = graph.to_distance_matrix()
            print(dist_matrix)
            are_ok = str(
                input('Is recieved distance matrix appropriate? [Yes/No]'))
            if are_ok == "Yes":
                break

    elif ex == 4:
        while True:
            graph = get_random_graph_with_user_input()
            center, min_sum = graph.get_center_vertices()
            print(f'Centrum = {center} (suma odleglosci: {min_sum})')
            center_minimax, minimax = graph.get_center_minimax()
            print(
                f'Centrum minimax = {center_minimax} (odleglosc od najdalszego: {minimax})')
            are_ok = str(
                input('Is recieved distance matrix appropriate? [Yes/No]'))
            if are_ok == "Yes":
                break
    elif ex == 5:
        while True:
            graph = get_random_graph_with_user_input()
            graph.find_min_spanning_tree()
            are_ok = str(
                input('Is recieved min spanning tree appropriate? [Yes/No]'))
            if are_ok == "Yes":
                break
    else:
        print('Unexpected choice')
        return True


def set4_choice():
    print_header()
    print("===================== SET 4 =====================")
    print("||  Choose which set of excecices you want open:")
    print("||  (1) Exercise 1")
    print("||  (2) Exercise 2")
    print("||  (3) Exercise 3")
    print("||  (4) Exercise 4")
    ex = int(input())
    if ex == 1:
        print("Insert verticles: ")
        v = int(input())
        print("Insert probability: ")
        p = float(input())
        g = DirectedGraphs.generate_random_directed_graph(v, p)
        g.plot()
    elif ex == 2:
        while True:
            cls()
            print("=============== Kosajaru Algorithm ===============")
            print("||  (1) Load graph from file")
            print("||  (2) Make random graph G(number_of_vertices, probability)")
            print("||  (0) Exit ")

            option = int(input())
            if option == 1:

                file = open("input/input_4.2.txt", "r")
                list = []
                line = file.readline()
                while line:
                    list.append(map(int, line.split(" ")))
                    line = file.readline()
                adjencyList = AdjacencyList(size=len(list))
                for i in range(len(list)):
                    adjencyList.adjacency_dictionary.setdefault(i, list[i])
                g = Graph(vertices=adjencyList.size, directed=True, weighted=False)
                g.edges = adjencyList.generate_graph_data(directed=True)
                g.plot(color_vs=DirectedGraphs.kosaraju(g))

            if option == 2:
                print("Insert verticles: ")
                v = int(input())
                print("Insert probability: ")
                p = float(input())
                gr = DirectedGraphs.generate_random_directed_graph(v, p)
                gr.plot(color_vs=DirectedGraphs.kosaraju(gr))

            else:
                set4_choice()
    elif ex == 3:
        cls()
        print("============== Bellman-Ford Algorithm ==============")
        print("||  (1) Load graph from file")
        print("||  (2) Make random graph G(number_of_vertices, probability)")
        print("||  (0) Exit ")

        option = int(input())
        if option == 1:
            file = open("input/input_4.2.txt", "r")
            list = []
            line = file.readline()
            while line:
                list.append(map(int, line.split(" ")))
                line = file.readline()
            adjencyList = AdjacencyList(size=len(list))
            for i in range(len(list)):
                adjencyList.adjacency_dictionary.setdefault(i, list[i])
            g = Graph(vertices=adjencyList.size, directed=True, weighted=True)
            g.edges = adjencyList.generate_graph_data(directed=True)
            g.randomize_weights(0,10)
            g.plot(color_vs=DirectedGraphs.kosaraju(g))
            if b := DirectedGraphs.shortest_path_bf(g, 0, 5):
                g.plot(color_vs = b)

        if option == 2:
            print("Insert verticles: ")
            v = int(input())
            print("Insert probability: ")
            p = float(input())
            print("Minimal weight: ")
            b = int(input())
            print("MAximal weight: ")
            e = int(input())
            b = False
            while not b:
                gr = DirectedGraphs.generate_random_directed_graph(v, p)
                b = (len(DirectedGraphs.kosaraju(gr)) == 1)
            gr.randomize_weights(b, e)
            gr.plot(color_vs=DirectedGraphs.kosaraju(gr))
            if b2 := DirectedGraphs.shortest_path_bf(gr, 0, 5):
                gr.plot(color_vs=b2)
            else:
                print("Graph has a negative cycle")
        else:
            set4_choice()
    elif ex == 4:
        print('Unaviable')
    else:
        print('Unexpected choice')
        return True
