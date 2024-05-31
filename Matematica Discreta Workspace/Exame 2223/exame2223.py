# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:48:48 2024

@author: ruben
"""

import math as mt
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power as mpower

numeroUsers = set(np.arange(1001,7001))

catchy = set()
for i in numeroUsers: 
    if i//100 % 15 == 0:
        catchy.add(i)

groovy = set()
for i in numeroUsers:
    if ((i**2) % 8) == (1 % 8):
        groovy.add(i)

serenity = set()
for i in numeroUsers:
    if i % 9 == 0 and i % 12 != 0:
        serenity.add(i)


# b

B = ((catchy & groovy) | (catchy & serenity) | (groovy & serenity)) - (catchy & groovy & serenity)
len(B)

# ou 

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


def v(n):
    return mt.cos( (n+1) / n) * u(n) )

n = 1
while (abs(v(n) < 2.6)):
    n+=1
    
print(n)


import pandas as pd
FICHEIRO = pd.ExcelFile(r"D:\ESTG_Stuff\Matematica Discreta Workspace\Exame 2223\Material\Dados.xlsx")
F1 = pd.read_excel(FICHEIRO, 'Folha1', header=None)
MR=F1.to_numpy()

#simetrica
def funcao3(MR):
    [c,d]=MR.shape
    for i in range(0,c):
        for j in range(i+1,d):
            if MR[i,j]!=MR[j,i]:
                return False
    return True

funcao3(MR)


# fecho transitivo
def funcao2(M):
    [L,C]=M.shape
    A=M
    for i in range(2,L+1):
        A=A+np.linalg.matrix_power(M,i)
    A[A!=0]=1
    return A

MS = funcao2(MR) 


import pandas as pd
FICHEIRO = pd.ExcelFile(r"D:\ESTG_Stuff\Matematica Discreta Workspace\Exame 2223\Material\Dados.xlsx")
F1 = pd.read_excel(FICHEIRO, 'Folha2', header=None)
MCG=F1.to_numpy()

MCGA = MCG.copy()
MCGA[MCGA!=0]=1

MCGAMasMelhor = MCGA+np.linalg.matrix_power(MCGA,2)+np.linalg.matrix_power(MCGA,3)

if MCGAMasMelhor[0,4] > 0:
    print(MCGAMasMelhor[0,4])
    
    
import numpy as np

def Warshall_Min(W):
    [a,b]=np.shape(W)
    
    Q=W.astype(float)
    
    M=np.empty((a, b))
    M=M.astype(str)
    for i in range(0,a):
        for j in range(0,a):
            if W[i,j]==0:
                Q[i,j]=np.inf
                M[i,j]='-'
            else:
                M[i,j]=str(i+1)+str(j+1)                
    print(M)
              
    for k in range(0,a):
        for i in range(0,a):
            for j in range(0,a):
                if Q[i,j]>Q[i,k]+Q[k,j]:
                    Q[i,j]=Q[i,k]+Q[k,j]
                    M[i,j]=M[i,k]+M[k,j][1:len(M[k,j])]     
    print(Q)
    print(M)
    
    S=[Q,M]
    return S
    
[Q,M]=Warshall_Min(MCG)

Q[Q!=np.inf] = 1
Q[Q==np.inf] = 0

# custo 8 caminho = 83765



'''
4-
'''


def pagamentos(E, R, V):    
    E = str(E)
    R = str(R)
    V = str(V)
    
    if (len(E) != 5 or len(R) != 9):
        print("barraca, valores com caracteres a mais ou a menos")
        return
       
    referenciaSemControlo = R[:7]
    controlo = R[7:]    
   
    i = V.index('.')

    V = V[:i] + V[i+1:]

    n=len(V)

    while n < 8:
        V = '0' + V
        n+=1
    
    inteira = V[:6]
    decimal = V[6:]
    print(E + referenciaSemControlo + inteira + decimal + controlo)
    x = int(E + referenciaSemControlo + inteira + decimal + controlo)
    
    if x % 97 == 1:
        print("Valido")
        return True
    else:
        print("Invalido")
        return False
    
    
pagamentos(11473, 574024763, 25.99)

