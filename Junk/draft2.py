# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 17:05:22 2018

@author: ByungsuJung
"""

import osmnx as ox
import pandas as pd

CENTER_LAT=47.608013
CENTER_LONG=-122.335167
DISTANCE_FROM_CENTER = 2000


center_pt = (CENTER_LAT, CENTER_LONG)


G = ox.graph_from_point(center_pt, distance=DISTANCE_FROM_CENTER, network_type='drive')
N = G.nodes()
zipped = zip(zip_df['LAT'], zip_df['LNG'])

for e in N.keys():
    x = N[e]
    for i in len():
        if lat == x['y'] and lng == x['x']:
            
        
    
for i in rangelen(x):
    print(i)
N

zip_df = pd.read_csv("C:\\Users\\jbsoo\\Downloads\\7882666-5bdc46db47d9515269ab12ed6fb2850377fd869e\\US Zip Codes from 2013 Government Data")
df[df['ZIP'] == 98104]
df.head()

df.head(10)
import numpy as np


for i,j in zip_df['LAT'], zip_df['LNG']:
    print(i,j)
    break

x = np.array(zip_df)
x[2999]

g_nodes = G.nodes()


g_nodes

for n in g_nodes.keys():
    name = g_nodes[n]['osmid']
    x = g_nodes[n]['x']
    y = g_nodes[n]['y']
    zipcode = -1
    for i in range(len(zip_df)-1):
        address = zip_df[i]
        if address[1] == y and address[2] == x:
            zipcode = address[0]


zip_df[30000]



accepted
Not the most efficient one, but by far the most obvious way to do it is:
a = [1, 2, 3, 4, 5]
b = [1, 6, 2, 5, 4]
a = set(a)
b = set(b)
for i in a:
    print(i)
xxxx = a.difference(b)




    def __init__(self, center_lat=47.608013, center_long=-122.335167, \
    dist=2000):
        center_pt = (center_lat, center_long)
        #G = ox.graph_from_point(center_pt, distance=dist, network_type='drive')
        G = ox.graph_from_place("Seattl, washington, USA")
        self.G = G
        self.node_map = self.set_intersections(G) #dictionary of nodes
        self.edge_map = self.set_roads(G, self.node_map) #dictionary of edges
        



