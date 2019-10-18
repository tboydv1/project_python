#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:10:37 2019

@author: tboydev
"""

x = 'a c e g i k m o q s u w y'
y = '+bdfhjlnprtvxz'
n = 1
z = x

for indx,space in enumerate(x):
    if space == ' ':
        z = z.replace(' ',y[n],1)
        n += 1
   
print(z)
        
    
