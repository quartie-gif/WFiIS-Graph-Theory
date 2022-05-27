import copy
import random
import sys
from collections import deque

from . import *


class FlowNetwork (Graph):
    def __init__(self, vertices: int = 0, edges: list = None,
                 number_of_layers: int = 0, layers: dict = None, flow: [] = None):
        super().__init__(vertices=vertices, edges=edges, directed = True, weighted= True)
        self.number_of_layers = number_of_layers
        self.layers = layers
        self.flow = flow


    @staticmethod
    def generate_random_flow_network(n: int):
        flowNetwork = FlowNetwork(number_of_layers=n)
        flowNetwork.layers = {i: [] for i in range(n)}
        flowNetwork.number_of_vertices += 1
        flowNetwork.layers[0].append(0)
        for key in range(1,flowNetwork.number_of_layers):
            rand = random.randint(1, n)
            for _ in range(rand):
                flowNetwork.layers[key].append(flowNetwork.number_of_vertices)
                flowNetwork.number_of_vertices += 1
        flowNetwork.end = flowNetwork.number_of_vertices
        flowNetwork.layers[flowNetwork.number_of_layers] = [flowNetwork.number_of_vertices]
        flowNetwork.number_of_vertices += 1
        flowNetwork.edges = []
        for key in range(flowNetwork.number_of_layers):
            l1 = len(flowNetwork.layers[key])
            l2 = len(flowNetwork.layers[key+1])
            if l1 == l2:
                for i in range(l2):
                    flowNetwork.edges.append((flowNetwork.layers[key][i], flowNetwork.layers[key+1][i]))
            if l1 > l2:
                for i in range(l2):
                    flowNetwork.edges.append((flowNetwork.layers[key][i], flowNetwork.layers[key+1][i]))
                for i in range(l2, l1):
                    flowNetwork.edges.append((flowNetwork.layers[key][i], random.randint(min(flowNetwork.layers[key+1]), max(flowNetwork.layers[key+1]))))
            if l1 < l2:
                for i in range(l1):
                    flowNetwork.edges.append((flowNetwork.layers[key][i], flowNetwork.layers[key+1][i]))
                for i in range(l1, l2):
                    flowNetwork.edges.append((random.randint(min(flowNetwork.layers[key]), max(flowNetwork.layers[key])), flowNetwork.layers[key + 1][i]))
        counter = 2 * n
        counter2 = 2 * n
        flowNetwork.weighted = False
        while counter and counter2:
            counter2 -= 1
            rand1 = random.randint(0, flowNetwork.number_of_vertices-2)
            rand2 = random.randint(1, flowNetwork.number_of_vertices-1)
            if not flowNetwork.edges.count((rand1, rand2)) and not flowNetwork.edges.count((rand2, rand1)) and rand1 != rand2:
                flowNetwork.edges.append((rand1, rand2))
                counter -= 1
            else:
                counter2 -= 1
        flowNetwork.randomize_weights(1, 10)
        flowNetwork.flow = [0] * len(flowNetwork.weighted_edges)
        return flowNetwork

    def plot(self):
        super().plot(color_vs=self.layers, isFlowNetwork = True)

    def ford_fulkerson (self):
        self.flow = [0] * len(self.weighted_edges)
        gf = copy.copy(self)
        while len(p := gf.bfs()) != 0:
            cp = self.get_cp(p)
            for i in range(len(p) - 1):
                if self.edges.count((p[i], p[i+1])) == 1:
                    for j in range(len(gf.edges)):
                        if gf.edges[j] == (p[i], p[i+1]):
                            self.flow[j] += cp
                    if gf.edges.count((p[i+1], p[i])) == 1:
                        for j in range(len(gf.edges)):
                            if gf.edges[j] == (p[i+1], p[i]):
                                self.flow[j] -= cp
                    else:
                        gf.edges.append((p[i+1], p[i]))
                        gf.weighted_edges.append(0)
                        gf.flow.append(-cp)

                else:
                    for j in range(len(gf.edges)):
                        if gf.edges[j] == (p[i], p[i + 1]):
                            self.flow[j] -= cp
                    for j in range(len(gf.edges)):
                        if gf.edges[j] == (p[i + 1], p[i]):
                            self.flow[j] += cp
        result = 0
        for v in gf.layers[1]:
            result += gf.get_flow(0, v)
        return result



    def bfs (self):
        d = [sys.maxsize] * self.number_of_vertices
        p = [None] * self.number_of_vertices
        d[0] = 0
        q = deque()
        q.append(0)
        while len(q) != 0:
            v = q.popleft()
            for u in range(self.number_of_vertices):
                for e in self.edges:
                    if e[0] == v and e[1] == u and self.get_cf(v, u) > 0:
                        if d[u] == sys.maxsize:
                            d[u] = d[v] + 1
                            p[u] = v
                            q.append(u)
        if p[self.number_of_vertices-1] == None:
            return []
        shortestPath = []
        shortestPath.append(self.number_of_vertices-1)
        next = self.number_of_vertices-1
        while 0 != next:
            next = p[next]
            shortestPath.insert(0, next)
        return shortestPath

    def get_cp(self, p):
        min = sys.maxsize
        for i in range(len(p)-1):
            if (min > self.get_cf(p[i], p[i+1])):
                min = self.get_cf(p[i], p[i+1])
        return min

    def get_cf (self, v, u):
        return self.get_weight (v,u) - self.get_flow(v, u)

    def get_flow (self, v:int, u:int):
        for i in range(len(self.edges)):
            if self.edges[i][0] == v and self.edges[i][1] == u:
                return self.flow[i]
        return False
