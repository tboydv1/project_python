#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 03:12:08 2019

@author: tboydev
This program calculates the distance of the voyager from the sun from 9/25/2009
"""
voyager_speed = 32241 #miles per hour
current_distance = 16_637_000_000

days_travelled = int(input("Enter number of days travelled: "))

"""Convert days to hours"""
days_travelled *= 24

#calculate distance from the sun
distance_in_miles = voyager_speed * days_travelled

#distance in miles
print("Distance travelled in miles is: ", distance_in_miles)

#distance in kilometers is 
distance_in_km = distance_in_miles * 1.609344

print("Distance travelled in kilometers is: ", distance_in_km)

#distance in austronomical units is

distance_in_au = distance_in_km * 92955807.267433
print("Distance travelled in austronomical units is: ", distance_in_au)

#distance in radio waves distance
"""convert distance in miles to meters"""
distance_in_meters = distance_in_miles * 1609.34

radio_seconds = distance_in_meters / 299792458
radio_hours = radio_seconds / 3600

print("Round-trip time for radio communication in hours is: ", radio_hours)

