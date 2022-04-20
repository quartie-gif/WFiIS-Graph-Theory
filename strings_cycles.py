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


