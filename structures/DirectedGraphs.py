import sys

from . import *
import random
import utils
import numpy as np

def generate_random_directed_graph(vert: int, probability: float):
    random_graph = Graph()
    random_graph.directed = True
    random_graph.number_of_vertices = vert
    for i in range(random_graph.number_of_vertices):
        for j in range(random_graph.number_of_vertices):
            if i != j and random.uniform(0, 1) < probability:
                random_graph.edges.append((i, j))
    return random_graph


def generate_network(pages: int, links: int):
    network = Graph()
    network.directed = True
    network.number_of_vertices = pages
    for _ in range(links):
        while True:
            i = random.randrange(0, pages)
            j = utils.random_choice_except(pages, i)
            if ((i,j) not in network.edges) :
                break
        network.edges.append((i, j)) 
    return network

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

def bellman_ford(graph: Graph, start: int):
    p = {}
    d = {}
    for v in range(graph.number_of_vertices):
        d[v] = sys.maxsize
        p[v] = None
    d[start] = 0

    for _ in range(graph.number_of_vertices):
        for i in range(len(graph.edges)):
            u = graph.edges[i][0]
            v = graph.edges[i][1]
            if d[u] + graph.weighted_edges[i] < d[v]:
                d[v] = d[u] + graph.weighted_edges[i]
                p[v] = u

    for i in range(len(graph.edges)):
        u = graph.edges[i][0]
        v = graph.edges[i][1]
        if d[v] > d[u] + graph.weighted_edges[i]:
            return False, False
    print("For ", start, "as start:")
    print("Vertices => predecessor, distance")
    for key in p:
        print (key, "=>", p[key], ",", d[key])
    return p, d

def shortest_path_bf (graph: Graph, start:int, end:int):
    if p := bellman_ford(graph, start)[0]:
        print("Path from", start, "to", end, "plotted with different color vertices")
        shortestPath = []
        shortestPath.append(end)
        while start != end:
            end = p[end]
            shortestPath.insert(0, end)
        result = {}
        result[0] = shortestPath
        return result
    return False
        
def graph_to_adjencyList(graph: Graph):
    out = [ [ 0.0 for i in range(graph.amount_of_vertices()) ] for j in range(graph.amount_of_vertices()) ]
    for i in range(graph.amount_of_vertices()):
        neighburs = graph.directed_outcoming_edges(i)
        for j in neighburs:
            out[j][i] += 1.0
    return out