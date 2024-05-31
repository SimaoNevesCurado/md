# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:08:50 2024

@author: ruben
"""

'''
EX 1 
'''

'''
    NOTA: P0 = A
    
    MAS -> ter cuidado ao fazer P = A no inicio para o acaso de mudarmos a P vamos tambem mudar a A
    
    i.e
    
    P = A
    P[i,j] = m <=> A[i,j] = m
        
    devemos fazer o P ser uma cópia do A == P = A.copy
    
'''

import numpy as np

A = np.array([[1,1,0,0],[1,0,0,1],[0,1,0,0],[1,0,1,0]]) # Matriz adjacencias do exemplo 1 ficha 7

def warshall(A):
    [a,b] = np.shape(A)
    
    P = A.copy()
    
    # 3 for's, o primeiro é para o numero de vertices ou seja, para ver quantas vezes tem de fazer isto tudo
    # os outros dois percorrem a matriz
    for k in range(0,a):
        for i in range(0,a):
            for j in range(0,b):
                if P[i,j] == 1 or P[i,k] == 1 and P[k,j] == 1:
                    P[i,j] = 1
    print("A matriz de caminhos é:")
    return P                    

# MELHOR VERSÃO

def warshall2(A):
    [a,b] = np.shape(A)
    
    P = A.copy()
    
    # 3 for's, o primeiro é para o numero de vertices ou seja, para ver quantas vezes tem de fazer isto tudo
    # os outros dois percorrem a matriz
    for k in range(0,a):
        for i in range(0,a):
            for j in range(0,b):
                P[i,j] = P[i,j] or (P[i,k] and P[k,j])
        print(f"P{k+1}:")
        print(P)
    print("A matriz de caminhos é:")
    return P  


warshall(A)

warshall2(A)


# encontrar o melhor caminho
# matriz de pesos do exemplo2 da ficha

W = np.array([[7,5,0,0],[7,0,0,2],[0,3,0,0],[4,0,1,0]])



def warshall_min(W):
    [a,b] = np.shape(W)
    
    
    #construção das matrizes Q e M inicial
    Q = W.astype(float)
    M = np.empty((a,b))
    M = M.astype(str)
    
    for i in range(a):
        for j in range (b):
            if(Q[i,j] == 0.0):
                Q[i,j] = np.inf
                M[i,j] = '-'
            else:
                M[i,j] = str(i+1) + str(j+1) # indexação matematica dos vertices na matriz M
    
    for k in range(0,a):
        for i in range(0,a):
            for j in range(0,a):
                if(Q[i,j] > Q[i,k] + Q[k,j]):
                    Q[i,j] = Q[i,k] + Q[k,j]
                    M[i,j] = M[i,k] + M[k,j][1:]
                # ou
                '''
                Q[i,j] = min(Q[i,j], Q[i,k] + Q[k,j])
                '''
        #print(f"Q{k+1}")
        #print(Q)
    return M

warshall_min(W)


    

