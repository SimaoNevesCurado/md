# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:21:49 2024

@author: bruno
"""
import math as mt
mt.ceil(100/8)

def conversor(x):
    return mt.ceil(x/8)

conversor(9)

mt.ceil(-2.5)

def inteiro(x):
    if (x<0):
        return mt.ceil(x)
    else :
        return mt.floor(x)
    
inteiro(0.1)

def bissexto(x):
    if (x%400==0 or (x%100!=0 and x%4==0)):
        return print("Bissexto")
    return print("Nao Bissexto")

bissexto(2023)

'''
def F(n):
    if (n==1 or n==2):
        return 1
    return F(n-1)+F(n-2)
F(50)
'''

def f(n):
    if n<3:
        return 1
    a=1
    b=1
    for i in range(3,n+1):
       c=a+b
       a=b
       b=c
    return c

f(9)

def soma_fib(n):
    soma=0
    for i in range(1,n+1):
        soma=soma+f(i)
    return soma

soma_fib(5)

import numpy as np
import math as mt


def termos_fib(s):
    v=np.array([],dtype=int)
    i=1
    while (soma_fib(i)<=s):
        v=np.append(v, f(i))
        i=i+1
    return v

termos_fib(20)

phi=(1+mt.sqrt(5))/2



n=2
while (abs(f(n)/f(n-1)-phi)>(10**-10)):
    n=n+1
print(f(n)/f(n-1))

import matplotlib.pyplot as plt

y=np.array([],dtype=int)
for i in range(2,n+1):
    y=np.append(y, f(i)/f(i-1))
    
plt.plot(y,".")

ANO=int(input("Indique o Ano: "))

ANO=2024
A=2024%100

S=mt.ceil(ANO/100)

SEMANA=["domingo","segunda","terça","quarta","quinta","sexta","sábado"]

d=(50 + A + ((S - 1)//4) + (A//4) - 2 * (S- 1))%7

print(SEMANA[d])

#%%

NOTA="M50027558701"

L=['R','S','T','U','M','N']

INICIO=L.index(NOTA[0])+1

soma=INICIO
for i in range(1,len(NOTA)):
    soma+=int(NOTA[i])

































