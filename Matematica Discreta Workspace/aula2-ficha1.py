# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:10:31 2024

@author: ruben
"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt

def f(x):
    return mt.cos(x) + mt.exp(x)

# 1 - b)
    f(0)
    
    f(mt.pi)
    
# 1 - c)

X = np.linspace(1, 2, 98)

f(X)

# result ERROR - only size 1 arrays can be converted to python scales so it doesn't work
# o f(x) so estava a espera de receber um ecalar e nao um array de elementos por causa do MT

# fix usa o numpy para ele adaptar-se


def f(x):
    return np.cos(x) + np.exp(x)


X = np.linspace(1, 2, 98)

Y = f(X)

plt.plot(X,Y)

# ou 

plt.plot(X,f(X))

# ex 2 - TPC

# como dao o incremento tempos de usar o np.arange

def f(x):
    return x**5 - 3*x**4 - 3*x**3 + 7*x**2 + 6*x

X = np.arange(-1.5,2.5,0.125) # como usamos o arange o limite nao pode ser ultrapassado ou atingido, por isso podemos adicionar um bocadinho mais para ele chegar la

X = np.arange(-1.5, 2.51, 0.125)

plt.plot(X,f(X))

# ex 3

def r(t):
    C0 = 10 # inicial
    v = 140 # tempo meia vida 
    return C0 * (0.5)**(t/v)

X = np.linspace(0,70,11) # range do instante inicial 0 , ate ao final de 70 dias, 10 semanas, de sete em sete dias, dai o limite de 11 elementos para ser 0,7,14,..,70
X = np.arange(0, 70,7) # range do instante inicial 0, até ao final de 70 dias, 10 semanas,  de sete em sete dias

Y = r(X)

plt.plot(X,Y,"*")

# Ex 4

# b - while


# Ex 5 

 # sucessoe so funcionam em N




