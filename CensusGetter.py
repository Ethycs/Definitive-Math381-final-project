# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:24:08 2018

@author: <Jasper >
"""
acs_shape = "C:\\Users\\Qeyto\\Dropbox\\Definitive Math381_final_project\\ACS_16_5yr_SHAPE\\" #ACS of 
CENSUS_FILE = "C:\\Users\\Qeyto\\Dropbox\\Definitive Math381_final_project\\ACS_16_5YR_B01003\\ACS_16_5YR_B01003_with_ann.csv"
import methods
import fiona
import shapely
import shapely.geometry
from pyproj import Proj, transform
import pandas as pd

block_counter = dict()
GEO_MAP = fiona.open(acs_shape, 'r')
checkmap = dict()

def addcount(geoid): #Pass me the string of geoid
    if geoid in block_counter:
        block_counter[geoid] += 1
    else:
        block_counter[geoid] = 1
        
def checkpoint(node:methods.Intersection) ->bool: #Check point against all regions
    for record in iter(GEO_MAP):
        region = shapely.geometry.asShape(record['geometry'])
        #Construct a type of dictionary for points, pop intersection object type
        #Take unassigned node, check its coordinates
        proj_coords_epsg3857 = transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), node.x, node.y)
        point = shapely.geometry.Point(*proj_coords_epsg3857)
        if region.contains(point):
            x = record['properties']['GEO_ID']
            node.geoid = x #Set censusblock code to x
            addcount(x)
            return True

#Populate checkmap with average block densities.
def initpop():
    df = pd.read_csv(CENSUS_FILE)
    for geoid in block_counter.keys():    
        x = df[df["GEO.id"]== geoid]['HD01_VD01'] 
        checkmap[geoid] = int(int(x.values[0]) / block_counter[geoid])
        print(checkmap[geoid])
        
def getweight(geoid) ->int:
    return checkmap[geoid]