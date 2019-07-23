# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:26:38 2018

@author: ByungsuJung
"""
import networkx as nx

G=nx.dodecahedral_graph()
nx.draw(G)
nx.draw(G,pos=nx.spring_layout(G))