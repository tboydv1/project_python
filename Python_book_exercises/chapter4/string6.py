#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:41:10 2019

@author: tboydev
"""

#String position 
pos = 0

S = 'I had a cat named amanda when I was little'
count = 0

#find all a's in S
while(pos > -1):
    count += 1
    pos = S.find("a", pos+1)
    print(count, "in")
    
    
    

    
    
    