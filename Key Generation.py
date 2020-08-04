# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:45:33 2019
@author: MOHAN
"""

from  geopy.geocoders import Nominatim

geolocator = Nominatim()

Place = str(input("Enter your location: "))
location = geolocator.geocode(Place)

latitude = str(location.latitude)
longitude = str(location.longitude)
k1 = latitude[0:2] + longitude[3:]
k2 = longitude[0:2] + latitude[3:]
k = k1 + k2
print(k[0:16])