#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 04:06:28 2019

@author: tboydev
program reprints information about gallons of gasoline
"""

gallons = float(input("Enter gallons of gasoline: "))

print("Total gallons of gasoline is: {:.2f}".format(gallons))

"""convert gasoline to litres"""
gallons_in_litres = gallons * 3.78541

print("Number of litres of gasoline is: {:.2f}".format(gallons_in_litres))

"""calculate number of barrels of oil
 required to make this amount of gasoline"""
 
barrels_of_oil = gallons / 19.5

print("Number of barrels of oil required to make {:.2f} gallons of gasoline \
is {:.2f}".format(gallons, barrels_of_oil))

"""calculate price in dollars"""
cost_per_gallons = 3.0 #in dollars

total_cost = cost_per_gallons * gallons

print("price in dollars: {} dollars".format(total_cost))

 