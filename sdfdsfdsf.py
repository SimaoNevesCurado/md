# -*- coding: utf-8 -*-
"""
Created on Fri May 31 20:36:56 2024

@author: simao
"""

import math as mt
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power as mpower



U=set(range(1001,7001))


#

catchy=set()
for n in U:
    if(n %15 == 0 ):
      catchy.add(n)      
len(catchy)





groovy=set()
for n in U:
    if((n**2) % 8 == 1 % 8 ):
        groovy.add(n)
len(groovy) #1500

       
serenity=set()
for n in U:
    if(n % 9 == 0 and n % 12 != 0 ):
      serenity.add(n)    
len(serenity)        

#3899

len(catchy & groovy) + len(catchy & serenity) + len(groovy & serenity) - 3 * len(catchy & groovy & serenity)



def u(n):
    if n == 1:
        return 3

    return mt.sqrt(4*u(n-1) + 5)

y = np.array(())
for i in range (1,21):
    y = np.append(y,(u(i)))

x = np.arange(1,21)

plt.plot(x,y,"*")




#b
def v(n):
    return mt.cos(((n+1)/n)*u(n))

n=1

while (abs(v(n)) < 2.6):
     n += 1


print(f"O menor valor de n para o qual  {n}")































