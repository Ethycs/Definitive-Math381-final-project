# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:30:55 2018

@author: Qeyto
"""
import osmnx as ox
class Road(object):
    
    def __init__(self, name,start, destination, length):
        self.name = name #int
        self.u = start #Node u 
        self.v = destination #Node v
        self.length = length #meters, float

class Intersection(object):
    
    def __init__(self, name, x, y, weight, zipcode, geoid, map=None):
        self.name = name
        self.x = x
        self.y = y
        self.weight = weight #Population
        self.geoid = geoid
        self.zipcode = zipcode
        self.map = map

        
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


# Currently used, maybe merge with map class in map.py?
V = set()
D = {}
E = set()
#Multiple scope issues
def initialization(a_map):
    D = {} # Cache for distances
    edges = []
    edge_and_length = {}
    a = a_map.edge_map.values()
    for e in a:
        edge = (e.u, e.v)
        length = e.length
        edges.append(edge)
        edge_and_length[edge] = length
    
    E = set(edges) # Edges
    cost = edge_and_length # Costs

    # Create iterable object for vertices
    V1 = list(a_map.node_map.values())
    weight = {} # Weight

    for v in V1: #Setting weights
        weight[v] = v.weight
        V = set(V1) # V
        C = set([])



def drawMap(nodes,edges):
    """
    Method: drawMap

    Method Arguments:
    * nodes - List of nodes that will be draw on to the graph to help
              help visualize the follow of traffic.

    * edges - List of edges that will be draw on to the graph to help
              help visualize the follow of traffic.

    Output:
    * No return values, but the graph will be created in its initial state
      using the nodes and edges.
    """ 
    for key, node in nodes.items():
        if node == best_donutshop_place:
            ax.plot(node.x,node.y, marker = 'o', color = 'r', markersize = 20)
            ax.plot(node.x,node.y, marker = '+', color = 'b', markersize = 20)
        if node == second_best_donutshop_place:
            ax.plot(node.x,node.y, marker = 'o', color = 'b', markersize = 20)
            ax.plot(node.x,node.y, marker = '+', color = 'r', markersize = 20)
        if node in min_list:
            ax.plot(node.x,node.y, marker = 'o', color = 'g', markersize = 20)
        else:
            ax.plot(node.x,node.y, marker = 'o', color = 'b')
    for key, edge in edges.items():
        if type(edge.u) is int:
            u = nodes[str(edge.u)]
            v = nodes[str(edge.v)]
            ax.plot([u.x,v.x],[u.y,v.y], color = 'k')
        else:
            ax.plot([edge.u.x,edge.v.x],[edge.u.y,edge.v.y], color = 'k')




# Given: vertex set V (of numbers or strings)
#        edge set E (subset of VxV) (undirected - order doesn't matter)
#        edge cost function (maps edges to positive reals)
#        weight function (maps vertices to positive reals)
#	 set of competitors C (subset of V)

# We are assuming that the given graph is connected and undirected

# Toy problem from the proposal
#V = set([1,2,3,4,5])
#E = set([(1,2), (2,3), (3,4), (4,1), (4,5)])
#cost = {(1,2) : 1, (2,3) : 2, (3,4) : 1, (4,1) : 2, (4,5) : 3}
#weight = {1 : 300, 2 : 300, 3 : 300, 4 : 300, 5 : 600}
#C = set([1,3])

# Returns a list of all pairs (F(v),v) (sorted by decreasing F(v)) and prints
# the vertex v in V that minimizes F(v)
def solve():
    X = []
    count = 0
    for v in V:
        X.append((F(v),v))
        print(count)
        count+=1
    return X

# Objective function
def F(v):
    result = 0
    for u in V:
        result += pi(u,v)*weight[u]/(1 + d(u,v))
    return result

# Returns the proportion of customers retained from u
# for a facility at v
def pi(u,v):
    if u == v:
        return 1
    if u in C:
        return 0
    gammas = 1/d(u,v)
    for x in C:
        gammas += 1/d(u,x)
    return 1/d(u,v)/gammas

#Jay's Dijkstra
def dijkstra(s, V, E):
    R = set([s]) # list of intersections(nodes)
    l = {} # key = destination(v), value = shortest path length from s to v
    for e in E:
        e = E[e]
        if e.u == s:
            l[e.v] = e.length
        else:
            l[e.v] = float('inf')
    l[s] = 0
    V_set = set(list(V.values()))
    count = 0
    while R != V_set:
        count += 1
        X = V_set.difference(R)
        x = minimal(X,l)
        print(count)
        for y in X:
            if (x, y) in ee.keys():
                length = ee[(x,y)]
                l[y] = min(l[y], l[x] + length)
#        for e in E:
#            e = E[e]
#            if e.u == x:
#                l[e.v] = min(l[e.v], l[x] + e.length)
        R.add(x)
    return (l)


# Returns the shortest distance between vertices u and v
# using Dijkstra's algorithm
def d(u,v):
    if (u,v) in D:
        return D[(u,v)]
    if (v,u) in D:
        return D[(v,u)]
    l = {}
    R = set([v])
    for x in V:
        if (v,x) in E:
            l[x] = cost[(v,x)]
        elif (x,v) in E:
            l[x] = cost[(x,v)]
        else:
            l[x] = float('inf')
    l[v] = 0
    while R != V:
        X = V.difference(R)
        x = minimal(X,l)
        for y in X:
            if (x,y) in E:
                l[y] = min(l[y], l[x] + cost[(x,y)])
            elif (y,x) in E:
                l[y] = min(l[y], l[x] + cost[(y,x)])
        R.add(x)
    for x in V:
        D[x,v] = l[x]
    return l[u]

# Given a set of vertices X and a length map l, returns the
# vertex v in X that minimizes l[v]
def minimal(X, l):
    result = X.pop()
    X.add(result)
    for x in X:
        if l[x] < l[result]:
            result = x
    return result

###########################################################################3
"""
Clustering algorithm : Mean-Shift
"""
def mshift(toy_map):
#    toy_map = Map(CENTER_LAT, CENTER_LONG, DISTANCE_FROM_CENTER)
    G = ox.graph_from_point(CENTER_POINT, DISTANCE_FROM_CENTER, network_type='drive')
    
    V = list(toy_map.node_map.values())
    
    
    # for lcustering , need a table or dict with loc and weight
    
    import numpy as np
    from sklearn.cluster import MeanShift, estimate_bandwidth
    def V_cls(V):
        V_cls = []
        for v in V:
            x = v.x
            y= v.y
            loc = (y,x) # Lat & Long
            V_cls.append(loc)
        return(V_cls)
    
    bandwidth = estimate_bandwidth(V_cls(V))
    
    ms = MeanShift(bandwidth = bandwidth, bin_seeding = True)
    ms.fit()

##########################################################




