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

#%%

#   MATRIZES

import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8]])

np.shape(a)
np.size(a)

print(a[1][3])

a[1][3]=3

b=np.array([[1,2,3,4],[5,6,4,8]])

a==b

np.array_equal(a, b)
(a==b).all()

np.eye(4)

np.zeros((3,6))

np.ones((2,4))

a.T
a*b
a@b

c=a.T

d=c@b
np.trace(a)

aq=np.array([[1,2],
            [5,6]])

from numpy.linalg import matrix_power as mpower

mpower(aq, 3)

#R = f(1; 1);(1; 3);(2; 1);(2; 3);(3; 1);(3; 2);(4; 4)g

mR=np.array([[1,0,1,0],
          [1,0,1,0],
          [1,1,0,0],
          [0,0,0,1]])

mR.T

A=(mR@mR)

def binaria(M):
    [a,b]=np.shape(M)
    for i in range(0,a):
        for j in range(0,b):
            if M[i,j]>0:
                M[i,j]=1
    return M

A[A!=0]=1

R=np.array([[0,1,0],
            [1,1,1],
            [1,0,0]])

S=np.array([[0,1,0],
            [0,1,1],
            [1,1,1]])

RoS=R@S
RoS[RoS!=0]=1

# c não está RoS relacionado com a uma vez que, na relação ...

def relcomp(MR,MS):
    MRoS=MR@MS
    MRoS[MRoS!=0]=1
    return MRoS

def is_reflexiva(M):
    [a,b]=M.shape
    return np.trace(M)==a
        
np.diag(A)

def is_simetrica(M):
    return np.array_equal(M, M.T)

def is_transitiva(M):
    [a,b]=M.shape
    R=M
    for i in range(1,a):
        R=R+mpower(M, i+1)
    R[R!=0]=1
    return np.array_equal(M, R)

r=np.array([[0,1,0],
            [0,0,1],
            [0,0,0]])

is_transitiva(r)

def fecho_reflexivo(M):
    if not is_reflexiva(M):
        [a,b]=M.shape
        R=M+np.eye(a)
        R[R!=0]=1
        return R
    else:
        return M

def fecho_simetrico(M):
    if not is_simetrica(M):
        S=M+M.T
        S[S!=0]=1
        return S
    else:
        return M
    
def fecho_transitivo(M):
    if not is_transitiva(M):
        [a,b]=M.shape
        T=M
        for i in range(1,a):
            T=T+mpower(M, i+1)
        T[T!=0]=1
        return T
    else:
        return M

def equival(M):
    if is_reflexiva(M) & is_simetrica(M) & is_transitiva(M):
        print("Já é relação de equivalência")
    else:
        print("Menor relação de equivalência: ")
        return fecho_transitivo(fecho_simetrico(fecho_reflexivo(M)))

equival(r)

def is_antissimetrica(M):
    [a,b]=M.shape
    for i in range(a):
        for j in range(b):
            if i!=j and M[i,j]==1 and M[j,i]==1:
                return False
    return True

is_antissimetrica(r)















