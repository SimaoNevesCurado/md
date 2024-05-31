# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:46:37 2024

@author: ruben
"""

# Aula 2 - 8/03/2024

# Folha 2

# Exemplos vetores

import numpy as np
import math as mt
import matplotlib.pyplot as plt

vetor = np.array([3,7,4,5])

impares = np.arange(1,10,2) # start , end , step

u = np.linspace(1,9,5)

np.append(vetor,65) # nao muda o vetor simplesmente adiciona para este instancia o valora

vetor =  np.append(vetor,65) # para redefinir

# definir funcoes tpo f(x) = x^2 + 5

def f(x):
    return (x**3 - 5 * x)
        
# print (f(4))

# multiplle returns

def g(x,y,z,w):
    return x+y, y+z, z+w

# print(g(1,2,3,4))

# exemplos rep graficas

x = np.array([2,5,10]) # vetor das abcissas

y = np.array([3,-1,4])  # vetor das ordenadas

# plt.plot(x,y, "*") # com "*" o grafico vai ser desenhado com pontos em vez de linhas

# plt.plot(x,y, "r") # com "r" desenha com cor vermelha

def h(x):
    return x**2

# definir o [-2, 2] com o linspace

X = np.linspace(-2, 2,5) # start, finish, number of elements

Y = h(X)

plt.plot(X,Y)

# melhorar o grafico aumentando o numero de pontos dos Y

XX = np.linspace(-2, 2,25) # start, finish, number of elements

YY = h(XX)

plt.plot(XX,YY)

# exemplos de ifs - funcoes definidas por ramos

def f(x):
    if(x>10):
        return x**2 + 1
    else:
        return x + 3

f(6)

# for 

for x in range(2,21,2): # range works start, stop, step 
# to get numbers up until limit it has to be within the range x - y example 1,20,2 so mostra até ao 19
    print(x)
    
# while

i=2
while(i<=20):
    print(i)
    i+=2
    
