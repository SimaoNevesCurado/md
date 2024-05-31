# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:36:16 2024

@author: ruben
"""

u1 = {(k+2)**2 for k in range(8,100) if (k+2)**2<=1599}
u2 = {(k+2)**2 for k in range(9,100) if (k+2)**2<=1599}


a = set();u=128;n=7

while u>100:
    if n<10:
        u=2**n
    else:
        u=1600-n**2
    a.add(u)
    n=n+1
    
    
b = set();u=128;n=7

while u>100:
    b.add(u)
    n=n+1
    if n<10:
        u=2**n
    else:
        u=1600-n**2