# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 18:30:34 2018

@author: ByungsuJung
"""
from methods import Intersection, Road
import CensusGetter
import requests
import osmnx as ox
import pandas as pd
ZIP_DIRECTORY = "C:\\Users\\Qeyto\\Desktop\\Math 381\\Math381_final_project\\pop_by_zip.csv"


class Map:
    
    # center_lat=47.608013, center_long=-122.335167, dist=1000
    
    def __init__(self,  center_lat=47.608013, center_long=-122.335167, dist=1000):
        center_pt = (center_lat, center_long)
        G = ox.graph_from_point(center_pt, distance=dist, network_type='drive')
        #G = ox.graph_from_place(place)
        self.G = G
        self.node_map = self.set_intersections(G) #dictionary of nodes
        self.edge_map = self.set_roads(G, self.node_map) #dictionary of edges
        
    def set_intersections(self, G):
        """
        Method: set_intersections

        Method Arguments:
        * G - The graph of a real section of the world that will be produced
              from using the osmnx package and the lat and lon provided by the
              user input.

        Output:
        * A dictionary of the nodes created will be returned, where each node id
          is their key.
        """ 
        node_dict = {} 
        g_nodes = G.nodes()
        weight = 100  # To be modified (Defaut)
        for n in g_nodes.keys():
            name = g_nodes[n]['osmid'] #What does this do?
            x = g_nodes[n]['x'] # -122
            y = g_nodes[n]['y'] # 42
#            zipcode = get_zip(y,x) #Insert point for zipcode data
#            #Entry point 
#            if zipcode == 11111: #Exception handling
#                weight = 300
#            weight = 100
#            #weight = get_pop(zipcode)
            node_to_insert = Intersection(name, x, y, weight, None, None,self)
            CensusGetter.checkpoint(node_to_insert)
            if name not in node_dict: 
                node_dict[name] = node_to_insert #Insert Node
            else:
                pass
        CensusGetter.initpop() #Set average weights in the system
        for n in node_dict:
            node_dict[n].weight = CensusGetter.getweight(node_dict[n].geoid)
        return node_dict #Return full dictionary with data added. 
    
    def set_roads(self, G, node_dict):
        
        """
        Method: set_roads

        Method Arguments:
        * G - The graph of a real section of the world that will be produced
              from using the osmnx package and the lat and lon provided by the
              user input.

        * node_dict - The node dictionary that will be used to show which roads
                        are connected to each other.

        Output:
        * A dictionary of the edges created will be returned, where each edge id
          is their key.
        """ 
        
        edge_dict = {}
        id = 0
        for e in G.edges(data=True):
            start = node_dict[e[0]]
            destination = node_dict[e[1]]
            length = int(e[2]['length']) 
            #name = e[2]['name']
            edge_to_insert = Road(id, start, destination, length)
            if id in edge_dict: 
                print("duplicate edge")
            edge_dict[id] = edge_to_insert
            id+=1
        #removed bad edge
        return edge_dict
    
#########################################################################3
        
def get_pop(zipcode):
    df = pd.read_csv(ZIP_DIRECTORY)
    #x =df[zipcode]
    x = df[df["Zip Code ZCTA"] == zipcode]['2010 Census Population']
    print(x)
    # if len(x) < 1:
    x = int(x.values)

    return(x)


# This code stopped working in between. But automatically fixed.
# https://gist.github.com/bradmontgomery/5397472
def get_zip(lat, long):
# grab some lat/long coords from wherever. For this example,
# I just opened a javascript console in the browser and ran:
#
# navigator.geolocation.getCurrentPosition(function(p) {
#   console.log(p);
# })
    #
    latitude = 47.608013#lat
    longitude = -122.335167#long

    # Did the geocoding request comes from a device with a
    # location sensor? Must be either true or false.
    sensor = 'true'

    # Hit Google's reverse geocoder directly
    # NOTE: I *think* their terms state that you're supposed to
    # use google maps if you use their api for anything.
    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=latitude,
        lon=longitude,
        sen=sensor
    )
    #print("Debug Format get_zip",base,params)
    url = "{base}{params}".format(base=base, params=params)
    #url = url + "&Key=AIzaSyCirOJRPBGCQ_UrF_r49FkPf14anlxRtTk"
    response = requests.get(url)
    result = 11111
    while True:
        response = requests.get(url).json()
        if(response['status'] == 'OK'):
            street_data = response['results'][0]['address_components']
            for i in street_data:
                if i['types'] == ['postal_code']:
                    result = int(i['long_name'])
            #length = len(street_data) - 1
            #result = street_data[length]['long_name']
            break
    return (result)   



        