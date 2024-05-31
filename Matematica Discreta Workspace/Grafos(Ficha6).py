# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:28:19 2024

@author: ruben
"""

'''

# GRAFOS

'''

# LER FICHEIRO EXCEL PARA CONSEGUIR AS MATRIZES

import pandas as pd
import numpy as np

ficheiro = pd.ExcelFile(r'D:\ESTG Stuff\Matematica Discreta Workspace\Fich Excel\MAdj_ex1.xlsx')

folha1 = pd.read_excel(ficheiro, 'MAdj', header=None)

A = folha1.to_numpy()


# 

ficheiro = pd.ExcelFile('MAdj_ex1.xlsx') # posso so por assim mas tenho de ter a diretoria onde ele está selecionada no topo direito (em cima do vairable explorer, hard to miss)


# Ex 1 C)

# Por observação do grafo: G é unilateralmente conexo.

#Ex 2

# a) 
# i)

ficheiro = pd.ExcelFile(r'D:\ESTG Stuff\Matematica Discreta Workspace\Fich Excel\A_ex2_f6.xlsx')
folha1 = pd.read_excel(ficheiro, 'Folha1', header=None)
A = folha1.to_numpy()

# II)

# IMPORTANTE: 
    
    # Para ver o numero de caminhos 2 = mpower(A,2) (A^2)
from numpy.linalg import matrix_power as mpower
    
A2 = mpower(A,2) # Matriz A^2, dá informação sobre o numero de caminhos de comprimento 2
A3 = mpower(A,3) # Matriz A^2, dá informação sobre o numero de caminhos de comprimento 3

# II)

import numpy as np

B = np.zeros((8,8))

#para ir até ao 8 se nao vai so ate ao 7

for i in range(1,8+1):
    B = B+mpower(A,i)

# III) aplicar o filtro ao B

B[B!=0]=1
P = B

# P = B[B!=0]=1
    
# B)


def isFortementeConexo(A):
    [a,b] = np.shape(A)
    B = np.zeros((a,b))

    for i in range(1,b+1):
        B = B+mpower(A,i)
   
    B[B!=0]=1
    P = B
    forteCon = True
    
    for i in range(0,a):
        for j in range(0,b):
            if(P[i,j] == 0):
                forteCon = False
                break
  
    if forteCon:
        print("Grafo é Fortemente Conexo")
    else:
        print("Grafo não é Fortemente Conexo")
    return forteCon 

    # ou 
    
    if 0 in P:
        print("Grafo é Fortemente Conexo")
        return True
    else:
        print("Grafo não é Fortemente Conexo")
        return False
  
    # Exemplo:
        
A = np.array([[0,1,0],[0,0,1],[0,0,0]])
isFortementeConexo(A)

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
    if(isFortementeConexo(A)):
        print()
    elif isUniConexo(A):
        print()
    elif isFracamenteConexo(A):
        print()
    else:
        print("Grafo é Desconexo")
    return


#ex 3

def graus(A,v): # matriz, vertice
    [a,b] = np.shape(A)
    
    v=v-1 #ajustar o indice por causa da indexação
    
    grauSaida = 0
    grauEntrada = 0
    
    for i in range(0,a):
        grauSaida += A[v,i];
        grauEntrada += A[i,v]
    
    return [grauSaida,grauEntrada]
    
    print(f"O Grau de Entrada de {v+1} é {grauEntrada} e o Grau de Saida de {v+1} é {grauSaida}")


graus(A,4)


# ex 4

def poco(A):
    [a,b] = np.shape(A)
    pocos = []
    for i in range(0,a):
        if graus(A,i+1)[0] == 0:
            pocos.add(i+1)
    if(pocos == set()):
        print("G Não tem Poços")
    else:
        print("G tem Poços")
            
poco(A)

# EX 5

def caminho_compK(A,k,v,u):
    ak = mpower(A,k)
    print(f"Existe {ak[v-1,u-1]} caminhos de comprimento {k} do vertice {v} para o vertice {u}")
    


caminho_compK(A,3,2,4)
        


# EX 6 

# a)

ficheiro = pd.ExcelFile(r'D:\ESTG Stuff\Matematica Discreta Workspace\Fich Excel\MAdj_ex6.xlsx')
folha1 = pd.read_excel(ficheiro, 'Folha1', header=None)
A = folha1.to_numpy()

# b)
'''

i) é possÌvel apanhar um voo direto de Miami para Chicago?

Não, porque na matriz A[6,3] está um 0, ou seja não há uma aresta entre Miami e Chicago

'''

# ii)

B = np.zeros((7,7))
#para ir até ao 8 se nao vai so ate ao 7
for i in range(1,7+1):
    B = B+mpower(A,i)
# III) aplicar o filtro ao B
B[B!=0]=1
P = B

'''
É possÌvel voar de Boston para Atlanta?

Não porque na matriz P[2,1] há um 0.
'''

# iii)

'''
É possÌvel voar de Miami para Chicago? 

é possivel porque na matriz P[6,3] há um 0

Fazendo um mÌnimo de quantas escalas?

como A^2 na posição [6,3] já tem um "1" o minimo de escalas a fazer é, uma escala (N-1 onde N = expoente de A)

'''


# IV)

'''
É PossÌvel voar de Denver para Miami fazendo duas escalas? 
De quantas formas diferentes?

A3 = mpower(A,3)

R: É possivel porque na matriz A3 ou seja com duas escalas, temos um valor diferente de 0 na posição [4,6], sendo esse valor '2', indica-nos que haja '2' maneiras de lá chegar com duas escalas
'''

'''
TPC -

SUGESTAO CUIDADO COM O FILTRO.

Existe(m) pares origem -> destino que exijam uma viagem com o mÌnimo de 3 escalas?

A4 = mpower(A,4) 
  
'''