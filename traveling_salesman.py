from operator import is_
from matplotlib import pyplot as pl
import random
from copy import deepcopy, copy
from math import exp

from numpy import copy

def distance(p1: tuple, p2: tuple):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return ( (x2-x1)**2 + (y2-y1)**2 )**0.5

def calc_distance(order: list, verts: dict):
    out = 0
    for i in range(len(order) - 1):
        out += distance( verts[order[i]], verts[order[i+1]] )
    out += distance(verts[order[-1]], verts[order[0]])
    return out

def swap_positions(L: list, pos1: int, pos2: int):
    L[pos1], L[pos2] = L[pos2], L[pos1]

def reverse_between(L: list, pos1: int, pos2: int):
    start = min(pos1, pos2)
    stop = max(pos1, pos2)
    steps = (stop - start)//2
    for add_to_pos in range(steps+1):
        swap_positions(L, start+add_to_pos, stop-add_to_pos)

def TSP(vertices: int, MAX_IT: int, file: str):

    with open(file) as f:
        data = f.readlines()

    i=0
    all_vert = {}

    for line in data:
        all_vert[i]  = ( float(line.split()[0]), float(line.split()[1]))  
        i += 1
        if( i >= vertices ):
            break

    P = [i for i in range(vertices)]

    # print("P = ", P)
    # print("all_vert = ", all_vert)

    d_P = calc_distance(P, all_vert)

    d_P_start = copy(d_P)
    P_start = copy(P)


    for i in range(100, 1, -1):
        T = 0.001 * i**2
        for it in range(MAX_IT):
            a = random.randint(0,len(P)-1)
            if a is not int(len(P)-1):
                b = a+1
            else:
                b = 0 

            while True:
                c = random.randint(0,len(P)-1)
                if c is not int(len(P)-1):
                    d = c+1
                else:
                    d = 0

                if (c is not a and c is not b
                    and d is not a and d is not b):
                    break
            
            dist_old = distance( all_vert[P[a]], all_vert[P[b]] ) + distance( all_vert[P[c]], all_vert[P[d]] )
            dist_new = distance( all_vert[P[a]], all_vert[P[c]] ) + distance( all_vert[P[b]], all_vert[P[d]] )

     
            if( dist_old > dist_new ):
                reverse_between(P, b, c)
               
            else:
                r = random.random()
                if r < exp( -(dist_new - dist_old)/T ):
                    reverse_between(P, b, c)
        
    d_P = calc_distance(P, all_vert)       
            
    print("Distance before annealing: ", d_P_start)
    print("Path before annealing:\n", P_start)
    print("\n========================================\n")
    print("Distance after annealing: ", d_P)
    print("Path after annealing:\n", P)

    with open(r'TSP_result.txt', 'w') as fp:
        is_first = True
        end_od_line = False
        eol_count = 0
        for item in P:
            if is_first:
                loop = item
                is_first = False
            # write each item on a new line
            fp.write("%s-" % item)
            eol_count += 1
            if eol_count % 10 == 0:
                end_od_line = True
            if end_od_line:
                fp.write("\n")
                end_od_line = False
        fp.write("%s" % loop)
        print('Saved')

    

    figure, axis = pl.subplots(1, 2)
    x = [ all_vert[p][0] for p in P_start ]
    x.append( all_vert[P_start[0]][0])
    y = [ all_vert[p][1] for p in P_start ]
    y.append( all_vert[P_start[0]][1])
    axis[0].set_xlim(-100, 100)
    axis[0].set_ylim(-100, 100)
    axis[0].plot(x, y, "-o", color="red")
    axis[0].set_title(f"Old path, d = {d_P_start}")


    x = [ all_vert[p][0] for p in P ]
    x.append( all_vert[P[0]][0])
    y = [ all_vert[p][1] for p in P ]
    y.append( all_vert[P[0]][1])
    axis[1].set_xlim(-100, 100)
    axis[1].set_ylim(-100, 100)
    axis[1].plot(x, y, "-o", color="blue")
    axis[1].set_title(f"New path, d = {d_P}")

    pl.show()

    
            
