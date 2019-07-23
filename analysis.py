# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:09:37 2018

@author: ByungsuJung
"""

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

D = {} # Cache for distances


import matplotlib.pyplot as plt
from intersection import Intersection
import osmnx as ox
from map import Map

CENTER_LAT=47.608013
CENTER_LONG=-122.335167
DISTANCE_FROM_CENTER = 1000
fig, ax = plt.subplots()
a_map = Map(center_lat=CENTER_LAT, center_long=CENTER_LONG, dist=DISTANCE_FROM_CENTER)
V = a_map.node_map
E = a_map.edge_map
C = []

# Returns the set of all pairs (F(v),v) and prints the vertex v in V
# that minimizes F(v)
def solve():
    X = set()
    for v in list(V.values()):
        X.add((F(v),v))
    print(max(X))
    return X

# Objective function
# v is a intersection to be examined.
# V is set of vertices 
# v is intersection and V is list of intersections
def F(v, V):
    result = 0
    for u in list(V.values()):
        result += pi(u,v,C) * u.weight /(1 + d(u,v))
    return result

# Returns the proportion of customers retained from u
# for a facility at v
# 
def pi(u, v, C): #u is intersection being examined, v is potential donut shot place
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
# E = a_map.edge_map
# V = a_map.node_map
def dijkstra(s, V, E):
    R = set([s]) # list of intersections(nodes)
    l = {} # key = destination(v), value = shortest path length from s to v
    for e in E:
        if e.u == s:
            l[e.v] = e.length
        else:
            l[e.v] = float('inf')
    l[s] = 0
    V_set = set(list(V.values()))
    while R != V_set:
        X = V_set.difference(R)
        x = minimal(X,l)
        for e in E:
            if e.u == x:
                l[e.v] = min(l[e.v], l[x] + e.length)
        R.add(x)
    return (l)
        
        
        
        
    

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
    result = X.pop()
    X.add(result)
    for x in X:
        if l[x] < l[result]:
            result = x
    return result
