import gc
from secrets import choice
from matplotlib.pyplot import plot
from structures import *
from strings_cycles import *
import numpy as np
import utils
import os

def random_walker(graph: DirectedGraphs, steps: int, damping: float ):
    if damping < 0 or damping > 1:
        raise ValueError("Damping factor must be between 0 and 1")
    ranks = { i: 0 for i in range(graph.amount_of_vertices())  }
    current = random.randint(0, graph.amount_of_vertices() )
    for step in range(steps):
        # print (f"on {current}")
        if len( graph.directed_outcoming_edges(current) ) > 0:
            if(random.random() > damping):
                current = random.choice(graph.directed_outcoming_edges(current))
                ranks[current] += 1
            else:
                current = random.randint(0, graph.amount_of_vertices()-1 )
                ranks[current] += 1
        else:
            current = random.randint(0, graph.amount_of_vertices()-1 )
            ranks[current] += 1
    return { i: float(pr/steps) for (i, pr) in ranks.items()}

def page_rank(graph: DirectedGraphs, damping: float ):
    ranks = { i: 0 for i in range(graph.amount_of_vertices()) }
    n = graph.amount_of_vertices()
    P = np.zeros((n,n))
    A = np.array( DirectedGraphs.graph_to_adjencyList(graph) )
    for i in range(n):
        for j in range(n):
            degree = len(graph.directed_outcoming_edges(j))

            if degree > 0:
                P[i][j] = (1.0 - damping) * A[i][j] / degree + damping/n
            else:
                P[i][j] = damping/n

    previous = np.full(n, 1/n)
    current = np.zeros(n)

    itr, error = 0, 1.0
    while error > 1e-12:
        current = np.dot(previous, np.transpose(P))
        err_mtx = current - previous
        previous = current
        error = sum( e**2 for e in err_mtx ) ** 0.5
        itr += 1
        
    print(f"Iteracje = {itr}")
    return { i: previous[i] for i in range(n) }




