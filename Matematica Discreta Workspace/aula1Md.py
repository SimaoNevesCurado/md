# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:46:37 2024

@author: ruben
"""

# Aula 1 - 1/03/2024


import math


# EX 1 - A

# 7 ** 3 == math.pow(7,3) == 7 elevado a 3

print((35.6*64-7**3)/(45 + math.pow(5,2)))

# B

print(((5/7) * 4 * 6 ** 2) - ((3 ** 7) / (9 ** 3 - 236)))

# C

print( ((3 ** 2) * math.log(76) / ((7**3) + 54 ) + 910 ** (1/3) ))

# d - not working
 
# print((math.cos(5*math.pi/6) **2) * (math.sin(7*math.pi/8)**2) + (math.tan((math.pi/6) * math.log(8)) / math.sqrt(7)))

print( math.cos(5*math.pi/6) ** 2 * math.sin(7*math.pi/8)**2 + (math.tan((math.pi/6) * math.log(8)) / math.sqrt(7)) )
# 2 - a

x = 13.5

print(x**3 - 2*x + 23.5*x**2)

# 2 - b

print(  math.sqrt(14*x**3) / math.e ** 3*x    )
