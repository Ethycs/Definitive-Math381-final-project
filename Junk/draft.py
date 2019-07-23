# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:28:27 2018

@author: ByungsuJung

something to be improved :
    
"""

# I must create undirected graph here and set edges and nodes here.
import matplotlib.pyplot as plt
import osmnx as ox
from map import Map
CENTER_LAT=47.608013
CENTER_LONG=-122.335167
DISTANCE_FROM_CENTER = 2000

#G = ox.graph_from_point((CENTER_LAT, CENTER_LONG),distance= DISTANCE_FROM_CENTER, network_type='drive', simplify=True) 
fig, ax = plt.subplot()
a_map = Map(center_lat=CENTER_LAT, center_long=CENTER_LONG, dist=DISTANCE_FROM_CENTER)

ax.plot()
    z = a_map.edge_map

for i in z.keys():
    print(z[i].u.x)
def drawMap(nodes, edges):
    for key, node in nodes.items():
        ax.plot(node.x,node.y)
    for key, edge in edges.items():
        if type(edge.u) is int:
            u = nodes[str(edge.u)]
            v = nodes[str(edge.v)]
            ax.plot([u.x,v.x],[u.y,v.y],linestyle='-',\
                    color=c.EDGE_COLOR,linewidth=edge.num_lanes*c.PLOT_EDGE_WIDTH)
        else:
            ax.plot([edge.u.x,edge.v.x],[edge.u.y,edge.v.y],linestyle='-',\
                color=c.EDGE_COLOR,linewidth=edge.num_lanes*c.PLOT_EDGE_WIDTH)        
            
drawMap(a_map.node_map,a_map.edge_map)


#G = ox.graph_from_point((CENTER_LAT, CENTER_LONG),distance= DISTANCE_FROM_CENTER, network_type='drive', simplify=True) 
fig, ax = plt.subplot()
a_map = Map(center_lat=CENTER_LAT, center_long=CENTER_LONG, dist=DISTANCE_FROM_CENTER)

def drawMap(nodes, edges):
    for key, node in nodes.items():
        ax.plot(node.x,node.y)
    for key, edge in edges.items():
        if type(edge.u) is int:
            u = nodes[str(edge.u)]
            v = nodes[str(edge.v)]
            ax.plot([u.x,v.x],[u.y,v.y],linestyle='-',\
                    color=c.EDGE_COLOR,linewidth=edge.num_lanes*c.PLOT_EDGE_WIDTH)
        else:
            ax.plot([edge.u.x,edge.v.x],[edge.u.y,edge.v.y],linestyle='-',\
                color=c.EDGE_COLOR,linewidth=edge.num_lanes*c.PLOT_EDGE_WIDTH)        
            
drawMap(a_map.node_map,a_map.edge_map)