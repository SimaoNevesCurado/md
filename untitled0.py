import math as mt
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power as mpower
import pandas as pd

#exemplo 1

A = np.array([[1,1,0,0],
              [1,0,0,1],
              [0,1,0,0],
              [1,0,1,0]])


#%% 1)

#Como criar uma copia de uma matriz
#P = A.copy()
def Warshall(A):

    [a,b] = np.shape(A)
    P = A.copy()
    for k in range(0,a):
        for i in range(0,a):
            for j in range(0,b):
                P[i,j] = P[i,j] or P[i,k] and P[k,j]
        print(f"Print da P{k+1}:\n{P}\n")
    return P
print(Warshall(A))

#%% 2)
#matriz pesos
A = np.array([[7,5,0,0],
              [7,0,0,2],
              [0,3,0,0],
              [4,0,1,0]])

#construção das matrizes Q's

def Warshall_MIN(W):

    [a,b] = np.shape(W)

    Q = W.astype(float)
    M = np.empty((a,b))
    M = M.astype(str)
    #Q[Q==0] = np.inf

    #ou

    for i in range(0,a):
        for j in range(0,b):
            if Q[i,j] == 0:
                Q[i,j] = np.inf
                M[i,j] = "-"
            else:
                M[i,j] = str(i+1) + str(i+1)

    for k in range(0,a):
        for i in range(0,a):
            for j in range(0,b):
                if Q[i,j] > Q[i,k] + Q[k,j]:
                    Q[i,j] = Q[i,k] + Q[k,j]
        print("")
        print(f"Q{k+1}")
        print(Q)
        print("")
        print(f"M{k+1}")
        print(M)

Warshall_MIN(A)