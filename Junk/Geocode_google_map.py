# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 18:12:18 2018

@author: ByungsuJung
"""

import requests #Maybe slow down the data request rate?

def get_zip(lat, long):
    # grab some lat/long coords from wherever. For this example,
    # I just opened a javascript console in the browser and ran:
    #
    # navigator.geolocation.getCurrentPosition(function(p) {
    #   console.log(p);
    # })
    #
    latitude = lat
    longitude = long

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
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    street_data = response.json()['results'][0]['address_components'][5]['long_name']
    
    return(int(street_data))