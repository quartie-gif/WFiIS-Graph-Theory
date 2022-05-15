from . import *
import random

def generate_random_directed_graph(vert: int, probability: float):
    random_graph = Graph()
    # random_graph.weighted = True
    random_graph.directed = True
    random_graph.number_of_vertices = vert
    for i in range(random_graph.number_of_vertices):
        for j in range(random_graph.number_of_vertices):
            if i != j and random.uniform(0, 1) < probability:
                random_graph.edges.append((i, j))
    # for _ in range(len(random_graph.edges)):
    #     random_graph.weighted_edges.append(random.randint(1, 10))
    return random_graph

def DFS_visit(v, graph : Graph, d, f, t):
    t += 1
    d[v] = t
    for u in range (graph.number_of_vertices):
        for e in graph.edges:
            if e[0]==v and e[1] == u:
                if d[u] == -1:
                    t = DFS_visit(u, graph, d, f, t)
    t += 1
    f[v] = t
    return t

def components_R (nr, v, graph, comp):
    for u in range(graph.number_of_vertices):
        for e in graph.edges:
            if e[0] == v and e[1] == u:
                if comp[u] == -1:
                    comp[u] = nr
                    components_R(nr, u, graph, comp)

def kosaraju(graph: Graph):
    d = [-1 for i in range(graph.number_of_vertices)]
    f = [-1 for i in range(graph.number_of_vertices)]
    t = 0
    for v in range (graph.number_of_vertices):
        if d[v] == -1:
            t = DFS_visit(v, graph, d, f, t)
    graphT = Graph.transpose(graph)
    nr = 0
    comp = [-1 for i in range(graph.number_of_vertices)]
    currentf = max(f)
    fcopy = list(f)
    findex = []
    next = True
    while next:
        for i in range(len(f)):
            if currentf == fcopy[i] and fcopy[i] != 1000000:
                findex.append(i)
                fcopy[i] = 1000000
                if currentf != min(fcopy):
                    currentf = min(fcopy)
                    next = True
            elif len(f) == len(findex):
                next = False
    for v in findex:
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_R(nr, v, graphT, comp)
    result = { i+1: [] for i in range(max(comp)) }
    for i in range(len(comp)):
        result[comp[i]].append(i)
    return result
