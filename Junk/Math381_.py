# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:44:02 2018

@author: ByungsuJung
"""
# I must create undirected graph here and set edges and nodes here.
import matplotlib.pyplot as plt
from intersection import Intersection
import osmnx as ox
from map import Map
import matplotlib.pyplot as plt

CENTER_LAT=47.608013
CENTER_LONG=-122.335167
DISTANCE_FROM_CENTER = 1000
fig, ax = plt.subplots()
a_map = Map(center_lat=CENTER_LAT, center_long=CENTER_LONG, dist=DISTANCE_FROM_CENTER)
#a_map = Map("Seattle, Washington, USA")



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
        ax.plot(node.x,node.y, marker = 'o', color = 'r')
    for key, edge in edges.items():
        if type(edge.u) is int:
            u = nodes[str(edge.u)]
            v = nodes[str(edge.v)]
            ax.plot([u.x,v.x],[u.y,v.y], color = 'b')
        else:
            ax.plot([edge.u.x,edge.v.x],[edge.u.y,edge.v.y], color = 'b')



# Returns the set of all pairs (F(v),v) and prints the vertex v in V
# that minimizes F(v)
def solve():
    X = set()
    for v in V:
        X.add((F(v),v))
    print(max(X))
    return X

# Objective function
# v is a intersection to be examined.
# V is set of vertices 
def F(v, V):
    result = 0
    for u in V:
        result += pi(u,v) * u.weight /(1 + d(u,v))
    return result

# Returns the proportion of customers retained from u
# for a facility at v
# 
def pi(u, v, C):
    if len(C) == 0:
        return 1
    if u == v:
        return 1
    if u in C:
        return 0
    gammas = 1/d(u,v)
    for x in C:
        gammas += 1/d(u,x)
    return 1/d(u,v)/gammas


# I need to find the shorest distance from  u to v in V where v is the nodes satisfying threshold.
# I use the distance between u and v to calculate F.
    
def zz (E):
    a = {}
    for e in E:
        e = E[e]
        aa = (e.u, e.v)
        a[aa] = e.length
    return(a)
ee =zz(a_map.edge_map)        

    
f = ee.keys()


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


dijkstra(s, a_map.node_map, a_map.edge_map)
        


# Returns the shortest distance between vertices u and v
# using Dijkstra's algorithm
def d(u,v): # v= s
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
    X = list(X)
    mini = X[0]
    for x in X:
        for x in l.keys():
            if l[x] < l[mini]:
                mini = x
    return(mini)
            
            
        




drawMap(a_map.node_map,a_map.edge_map)