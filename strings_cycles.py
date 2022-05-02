from distutils.command.config import config
import re
from tkinter import W
import igraph as g
import numpy as np
from copy import copy
from data_structures import *
import utils
from itertools import permutations

def is_graphical_string(input: list):
    '''Check if given numbers forms graphical string'''

    if sum(input) % 2 != 0:
        return False
    if max(input) >= len(input):
        return False
   
    input.sort( reverse = True )
    vertices = { i: input[i]  for i in range(len(input)) }

    while True:
        if min(vertices.values()) < 0:
            return False
        if max(vertices.values()) == 0 and min(vertices.values())== 0:
            return True
        vertices = dict(sorted(vertices.items(), key=lambda item: item[1], reverse=True))
        iter_ver = iter(vertices)
        current = next(iter_ver)
        for _ in range( vertices[current] ):
               vertices[ next(iter_ver) ] -= 1
        vertices[current] = 0

def string_to_graph(input: list):
    '''Convert graphical string to graph'''
    if is_graphical_string(input):
        e = []
        v = len(input)
        input.sort( reverse = True )
        vertices = { i: input[i]  for i in range(len(input)) }

        while sum(vertices.values()) != 0:
            vertices = dict(sorted(vertices.items(), key=lambda item: item[1], reverse=True))
            iter_ver = iter(vertices)
            current = next(iter_ver)
            for _ in range( vertices[current] ):
                temp = next(iter_ver)
                vertices[ temp ] -= 1
                e.append( (current, temp) )
            vertices[current] = 0
        return Graph(v, e)

    else:
        raise ValueError('Invalid string')

def all_components(in_graph: Graph):
    '''Find all components'''
    verts = in_graph.get_vertices()
    nr = 0
    comp = { i: -1  for i in verts }
    for key in comp.keys():
        if comp[key] == -1:
            nr += 1
            comp[key] = nr
            components_rec(nr, key, in_graph, comp)
    all_components = { i: [] for i in comp.values() }
    for key in comp.keys():
        all_components[comp[key]].append(key)  
    return all_components

def components_rec(nr: int, key: int, in_graph: Graph, comp: dict):
    '''Recursive search'''
    neighburs = in_graph.get_neighbors(key)
    for u in neighburs:
        if comp[u] == -1:
            comp[u] = nr
            components_rec(nr, u, in_graph, comp)

def greatest_components_elements(in_graph: Graph):
    '''Return all vertices of largest component'''
    all_comps = all_components(in_graph)
    largest = max( [len(i) for i in all_comps.values()] )
    out = []
    for i in all_comps.values():
        if len(i) == largest:
            out.append(i)
    return out

def greatest_components_size(in_graph: Graph):
    '''Return size of largest component'''
    all_comps = all_components(in_graph)
    return max( [len(i) for i in all_comps.values()] )

def components_listing(in_graph: Graph):
    ''' Listing of all components'''
    out = ''
    max_size = -1
    max_id = -1
    data = all_components(in_graph)
    print(data)
    for key, val in data.items():
        out += f"{key}) " + " ".join(map(str, val)) + '\n'
        if len(val) > max_size:
            max_size = len(val)
            max_id = key
    out += f"Greatest component: {max_id}).\n"
    return out;

def eulerian_cycle(in_graph: Graph):
    '''Searching eulerian cycle in given graph'''
    non_zero = []
    for i in range(in_graph.vertices):
        degree = in_graph.degree(i)
        if degree > 0:
            non_zero.append(i)
        elif degree % 2 != 0:
            return "Degree of all vertices must be even number - no eulerian cycle in graph"
    if len(non_zero) != greatest_components_size(in_graph):
        return "No eulerian cycle in graph - isolated edges"
    
    current = random.choice(non_zero)

    edges = copy(in_graph.edges) 
    cycle = f"[ {current}"
    while len(edges) > 0:
            current = jump_to_next_vertex(current, edges)
            cycle += f" - {current}"
    cycle += " ]"            
    return cycle

def jump_to_next_vertex(old_vert: int, edges: list):
    '''Go to next vertex, prioritizing edges that aren't briges'''
    cur_vert = old_vert
    possible_edges = get_edges_from_vertices(cur_vert, edges)
    if len(possible_edges) == 0:
        raise Exception("No possible edges to jump")
    selected_edge = possible_edges[0]
    for e in possible_edges:
        if not is_brige(old_vert, e, edges):
            selected_edge = e
            break
    edges.remove(selected_edge)
    if old_vert == selected_edge[0]:
        cur_vert = selected_edge[1]
    else:
        cur_vert = selected_edge[0]
    return cur_vert

def get_edges_from_vertices(vert: int, edges: list):
    '''Returns all edges from given vertex'''
    is_connected = lambda x: vert == x[0] or vert == x[1]
    return list( filter( is_connected, edges ) )

def is_brige(cur_vert: int, edge: tuple, edges: list):
    '''Check if given edge is brige'''
    edges.remove( edge )
    if cur_vert == edge[0]:
        vert = edge[1]
    else:
        vert = edge[0]
    is_connected = lambda x: vert == x[0] or vert == x[1]
    if len(list( filter( is_connected, edges))) == 0:
        edges.append(edge)
        return True
    else:
        edges.append(edge) 
        return False

def hamilotnian_cycle(in_graph: Graph):
    '''Searching hamiltonian cycle in given graph'''
    for i in range(in_graph.vertices):
        degree = in_graph.degree(i)
        if degree < 2:
            return "Degree of all vertices must be grater or equal to 2 - no hamiltonian cycle in given graph"
    if in_graph.amount_of_vertices() != greatest_components_size(in_graph):
        return "Graph is not connected - neccesery condition is not met"
    all_configs = generate_all_configs(in_graph.amount_of_vertices())
    all_edges = in_graph.get_edges()
    for configuration in all_configs:
        if is_hamiltonian_cycle(configuration, all_edges):
            return "["+ " - ".join(map(str, configuration)) + f" - {configuration[0]}"  +"]"
    return "No hamiltonian cycle in given graph"

def generate_all_configs(amount: int):
    '''Generates all possible permutations of verrticles order'''
    base = [i for i in range(amount) ]
    return permutations(base, len(base))

def is_hamiltonian_cycle(configuration: tuple, all_edges: list):
    '''Check if given configuration is a hamiltonian cycle'''
    for i in range(len(configuration)-1):
        if (    ( configuration[i], configuration[i+1] ) not in all_edges 
            and ( configuration[i+1], configuration[i] ) not in all_edges ):
            return False
    return True








    

    


    
            
        
    
