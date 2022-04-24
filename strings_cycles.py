from tkinter import W
import igraph as g
import numpy as np
from copy import copy
from data_structures import *
import utils


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
        # print(vertices)
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
    







