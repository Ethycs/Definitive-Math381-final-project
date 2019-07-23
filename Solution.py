# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:11:33 2018
Reference : https://towardsdatascience.com/clustering-the-us-population-observation-weighted-k-means-f4d58b370002
@author: ByungsuJung
"""

import methods
import matplotlib.pyplot as plt
#import osmnx as ox
from map import Map

CENTER_LAT = 47.608013
CENTER_LONG = -122.335167
CENTER_POINT = (CENTER_LAT, CENTER_LONG)
DISTANCE_FROM_CENTER = 1000 # Meters

# Create a map
a_map = Map(center_lat=CENTER_LAT, center_long=CENTER_LONG, dist=DISTANCE_FROM_CENTER)
methods.initialization(a_map) #Engage in necessary logic

Answer = methods.solve()
#best_donutshop_place = Answer[len(Answer)-1][1]
#second_best_donutshop_place = Answer[len(Answer)-2][1]
# Create a blank figure

#### Answer tweak?
Answer.sort(key = lambda x: x[0])
best_donutshop_place = Answer[len(Answer)-1][1]
second_best_donutshop_place = Answer[len(Answer)-2][1]
fig, ax = plt.subplots()

# Draw complete graph into the figure. Best donut place is indicated as red dot
methods.drawMap(a_map.node_map, a_map.edge_map)

competitors = [(47.6057,    -122.3369),
               (47.610087, -122.32376),
               (47.608631, -122.34021),
               (47.603269, -122.33616),
               (47.613096, -122.31657),
               (47.616912, -122.33183),
               (47.616359, -122.345628)
              ]


# find score of competitors
min_list = []
for i in competitors:
    temp_min_p = methods.Intersection
    temp_min = 99999999
    for v in methods.V:
        x = abs(v.y - i[0])
        y = abs(v.x - i[1])
        z = x+y
        if z < temp_min:
            temp_min_p = v
            temp_min = z
    min_list.append(temp_min_p)     
    
gps_add = [] 
for v in min_list:
    x = v.x # -122
    y = v.y # 42
    z = (y, x)
    gps_add.append(z)

# For calculating mean
total = 0
for i in Answer:
    total += i[0]
    
### Use to find competitor's score and location
for i in Answer:
    x = i[1]
    if x in min_list:
        print(i)




