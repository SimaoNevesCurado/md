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

#%%

import pandas as pd

FICHEIRO = pd.ExcelFile(r'C:\Users\bruno\Documents\Univeridade\1ano_2semestre\Matemática Discreta\Programas\MAdj_ex1.xlsx')
F1 = pd.read_excel(FICHEIRO, 'MAdj', header=None)
A=F1.to_numpy()

import networkx as nx
G=nx.DiGraph(A)
pos={2:[0,1],0:[1,0],1:[2,0],3:[3,1],4:[1,2],5:[2,2]}
label={0:'v1',1:'v2',2:'v3',3:'v4',4:'v5',5:'v6'}
nx.draw(G,pos,labels=label,node_color='pink',node_size=1000,font_color='black',arrowsize=25)

FICHEIRO = pd.ExcelFile(r'C:\Users\bruno\Documents\Univeridade\1ano_2semestre\Matemática Discreta\Programas\A_ex2_f6.xlsx')
F1 = pd.read_excel(FICHEIRO, 0, header=None)
B=F1.to_numpy()

from numpy.linalg import matrix_power as mpower
import numpy as np

C=B
for i in range(2,9):
    C=C+mpower(B, i)

print(C)

C[C!=0]=1

def isFortementeConexo(M):
    [a,b]=np.shape(M)
    P=np.zeros((a,a))
    for i in range(1,a+1):
        P=P+mpower(M, i)
    P[P!=0]=1
    for i in range(a):
        for j in range(b):
            if P[i,j]==0:
                print("Não é fortemente conexo")
                return False
    print("É fortemente conexo")
    return True


def isUniConexo(A):
    # verificar as posições simetricas para ver se I,J AND J,I == 0, SE SIM NÃO É Uni
    [a,b] = np.shape(A)
    B = np.zeros((a,b))

    for i in range(1,b+1):
        B = B+mpower(A,i)
   
    B[B!=0]=1
    P = B
    uniCon = True
    
    for i in range(0,a):
        for j in range(0,b):
            if i!=j and P[i,j] == 0 and P[j,i] == 0:
                uniCon = False
                break
    
    if uniCon:
        print("Grafo é Unilateralmente Conexo")
    else:
        print("Grafo não é Unilateralmente Conexo")
    return uniCon 

A = np.array([[0,1,0],[0,0,1],[0,0,0]])
isUniConexo(A)

def isFracamenteConexo(A):
    # não vale a pena fazer a matriz de caminhos pq nao podemos ir por ai
    # temos de ver se existe semi caminhos
    [a,b] = np.shape(A)
    V = np.zeros((a,b))

    # A + A.T = SA

    for i in range(1,b+1):
        V = V+mpower(A+A.T,i)
   
    # SP = MATRIZ DE SEMI CAMINHOS
    V[V!=0]=1
    SP = V
    fraCon = True
    
    if 0 in SP:
        fraCon = False
    
    if fraCon:
        print("Grafo é Unilateralmente Conexo")
    else:
        print("Grafo não é Unilateralmente Conexo")
    return fraCon

A = np.array([[0,1,0],[0,0,1],[0,0,0]])
isFracamenteConexo(A)

def conectividade(A):
    if (isFortementeConexo(A)):
        print()
    elif isUniConexo(A):
        print()
    elif isFracamenteConexo(A):
        print()
    else:
        print("Grafo é Desconexo")
        
    return

def graus(A,v):
    [a,b]=np.shape(A)
    gs=0; ge=0
    for i in range (0,a):
        gs=gs+A[v-1,i]
        ge=ge+A[i,v-1]
    print(f"O grau de saída do vértice {v} é {gs} e o de entrada é {ge}")
    Gr=[gs,ge]
    return Gr

def poço(A):
    [a,b]=np.shape(A)
    p=set()
    for i in range(1,a+1):
        if graus(A, i)[0]==0:
            p.add(i)
    if p==set():
        print("Não tem poços")
    else:
        print("Tem")
        
def caminho_compk(A,k,v,u):
    Ak=mpower(A, k)
    return Ak[v-1,u-1]
            
R=caminho_compk(B, 3, 2, 4)
    

FICHEIRO = pd.ExcelFile(r'C:\Users\bruno\Documents\Univeridade\1ano_2semestre\Matemática Discreta\Programas\MAdj_ex6.xlsx')
F1 = pd.read_excel(FICHEIRO, 0, header=None)
B=F1.to_numpy()

print(B)    
    
def caminho(M):
    [a,b]=np.shape(M)
    P=np.zeros((a,a))
    for i in range(1,a+1):
        P=P+mpower(M, i)
    P[P!=0]=1
    print(P)
    
caminho(B)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    