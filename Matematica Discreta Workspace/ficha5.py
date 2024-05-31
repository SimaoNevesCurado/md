# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:20:37 2024

@author: ruben
"""

# FICHA 5

# EXEMPLOS

import numpy as np;

A = np.array([[1,2,3,4],[5,6,7,8]])
# ou
A = np.array([[1,2,3,4],
              [5,6,7,8]]) # para vermos melhor a matriz

# tirar a dimensão de A

np.shape(A)
#(linhas,colunas)

# OU 
A.shape
#(linhas,colunas)

# contar os elementos

A.size # quase nunca é usado 

# elemento da matriz A na posição 2,4
A[1,3] # porque a indexação começa como 0 # ATENÇÃO AOS INDICES

# reatribuição

A[1,3] = 3


####

B = np.array([[1,7,1,4],
              [5,6,4,8]]) # para vermos melhor a matriz

# verificar se A é igual a B

A == B # Devolve uma matriz de booleans que verifica elemento a elemento a igualdade

# Para verficiar mesmo se são iguais.

np.array_equal(A,B)

# OUUUU

(A == B).all()


# criar matrizes rapidamente, so para estas 3  porque são usadas bastante vezes

np.identity(4)

# OU

np.eye(4)


# matriz nula

np.zeros((3,6)) # (linhas,colunas)


# matriz toda só com 1's

np.ones((2,4)) # (linhas,colunas)


# FUNÇÕES MATRICIAIS

# Transposta (de A)

A.T

# Multiplicação de matrizes

A * B # faz a multiplicação de CADA elemento 1 a 1

# Como fazer? 

A @ B

# neste caso é uma operação impossivel porque o numero de colunas de A é diferente do Número de linhas da B

C = A.T # transpor a A para que C seja uma matriz 4 por 2 e dê para multiplicar pela matriz B

C @ B # multiplicar as matrizes

# como fazer o traço da matriz (soma dos elementos da diagonal principal)

np.trace(A)

# potência de matrizes A ^ K

np.linalg.matrix_power(C@B,2) #Calcula (C * B) * (C * B)

from numpy.linalg import matrix_power as mpower

mpower(A,3) # Calcula A * A * A 
# NÃO DÁ PORQUE "A" TEM DE SER QUADRADO

A ** 3 # potencia elemento a elemento

# Exercicios

# EX 1 

# a) matriz que representa R
A = {1,2,3,4}
R = {(1,1),(1,3),(2,1),(2,3),(3,1),(3,2),(4,4)}

MatrizR = np.array([[1,0,1,0]
                    ,[1,0,1,0]
                   ,[1,1,0,0]
                   ,[0,0,0,1]])

# feita a olho


# ex 1 - b

# matriz inversa de R = matriz tranpsposta de Mr

MatrizInversa = MatrizR.T


# c)

MatrizRoR = MatrizR @ MatrizR # falta o filtro de que tudo != 0 passa a 1 # mas os "número" dizem o numero de maneiras diferentes de chegar aquele ponto

# para fazer o filtro / fazer matriz binaria:

def binaria(M):
    [a,b] = np.shape(M) # [linhas , colunas]
    for i in range(0,a):
        for j in range(0,b):
            if (M[i,j] > 1):
                M[i,j] = 1    
    return M


# função binaria será então

binaria(MatrizRoR)

# ou com comando (mais rapido)

MatrizRoR[MatrizRoR != 0 ] = 1

# Matriz de RoRoR (R^3)


binaria(mpower(MatrizRoR,3))

# OUUUU

MR3 = mpower(MatrizRoR,3)

MR3[MR3!=0] = 1


# d)

# i, não é simetrica por que não é igual a transposta, ou porque tem o elemento 2,1 e não tem o elemento 1,2

# iii, não é transitiva porque temos o par 2,3 e o par 3,2 mas nao temos o par 2,2, ou seja, aRb e bRc mas nao temos aRc




# 2-


MatrizR = np.array([[0,1,0]
                    ,[1,1,1]
                   ,[1,0,0]])

MatrizS = np.array([[0,1,0]
                    ,[0,1,1]
                   ,[1,1,1]])

# Matriz R em composição com S


MatrizRS = MatrizR @ MatrizS

MatrizRS[MatrizRS != 0] =1


# B) Indique, justificando, se 'c' é R em composição com S está relacionado com a.

'''
    Resposta:
    C não esta R apos S relacionado com a uma vez que na MatrizRS (matriz da relação R após S) na posição (3,1), encontramos um 0
    
    Extra:
    Porque de C estar RoS relacionado com B
    
    Sim: Porque na MatrizR temos (C,A) e na MatrizS temos (A,B), como o A liga as duas, C tera relacionado com B
'''


# 3- 
 
def relcomp(MR,MS):
    MRoS = MR @ MS
    MRoS[MRoS != 0] =1
    
    return MRoS


relcomp(MatrizR,MatrizS)


# ex 4- A partir da matriz MR de uma relaÁ„o R, construa uma funÁ„o:

    
# (a) com o nome is_reflexiva(MR) que veriÖque se a relaÁ„o R È uma relaÁ„o reáexiva;

def is_reflexiva(MR):
    [a,b] = np.shape(MR)
    
    #R = True
    for i in range(0,a):
        if(MR[i,i] == 0):
            return False # R = False
    return True # R

    # OU
    
def is_reflexiva(MR):
    [a,b] = np.shape(MR)
    if(np.trace(MR) == a):
        return True
    else:
        return False
    
is_reflexiva(MatrizR)

    # OU
    
def is_reflexiva(MR):
    [a,b] = np.shape(MR)
    diagonalPrinc = np.diag(MR)
    diagIdent = np.diag(np.eye(a))
    if(diagonalPrinc.all() == diagIdent.all()):
        return True
    else:
        return False

is_reflexiva(A)


# (b) com o nome is_simetrica(MR) que veriÖque se a relaÁ„o R È uma relaÁ„o simÈtrica;

def is_simetrica(MR):
    # verifica se MR  == a sua transposta
    
    if (MR == MR.T).all(): # == np.array_equal(MR,MR.T)
        return True
    else:
        return False

is_simetrica(MatrizR)

# OU

def is_simetrica(M):
    [a,b] = np.shape(M) # [linhas , colunas]
    for i in range(0,a):
        for j in range(0,b):
            if (M[i,j] != M[j,i]):
               return False
    return True


MatrizR = np.array([[0,1,0]
                    ,[1,1,1]
                   ,[1,0,0]])

MatrizS = np.array([[0,1,0]
                    ,[0,1,1]
                   ,[1,1,1]])

is_simetrica(MatrizR)
is_simetrica(MatrizS)

# (c) com o nome is_transitiva(MR) que veriÖque se a relaÁ„o R È uma relaÁ„o transitiva.


def is_transitiva(M):
    [a,b] = np.shape(M) # [linhas , colunas]
    # verificar se a Matriz original != Matriz Original + matriz de r apos r, n vezes em que n é o numero de elementos da relação porque temos de verificar até dar 0 novos elementos
    McomposM = mpower(M,2)
    MTrans = McomposM + M
    MTrans[MTrans != 0] = 1
    return np.array_equal(M,MTrans)

# ex 8- 

'''
as funções 2 e 3 permitem verificar se R é reflexiva, a função 1 não permite uma vez que devolveria informação em fnução a cada elemento da diagonal 
'''

#


from numpy.linalg import matrix_power as mpower

A = np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])

A2 = mpower(A,2)
A3 = mpower(A,3)
A4 = mpower(A,4)

is_transitiva(A)

def makeTrans(M):
    [a,b] = np.shape(M) # [linhas , colunas]
    MFT = np.zeros((a,b))
    for i in range(1,a+1):
        MFT += mpower(M,i) #Matriz dofecho+ transitivo
    MFT[MFT!=0] = 1
    
    return MFT

makeTrans(A)

# juntando

def isTrans(M):
    [a,b] = np.shape(M) # [linhas , colunas]
    MFT = np.zeros((a,b))
    
    for i in range(1,a+1):
        MFT += mpower(M,i) #Matriz dofecho transitivo
    MFT[MFT!=0] = 1
    
    if(np.array_equal(M, MFT)):
        print("Relação inserida é transitiva")
        t=True
    else:
        print("Rekalação inserida não é transitiva: Seria transitiva se fosse = ") 
        print(MFT)
        t=False
        
    return t

isTrans(A)

########

# 5

def is_reflexiva(MR):
    [a,b] = np.shape(MR)
    diagonalPrinc = np.diag(MR)
    diagIdent = np.diag(np.eye(a))
    if(diagonalPrinc.all() == diagIdent.all()):
        print("R É Reflexiva")
        return True
        
    else:
        print("R não é Reflexiva")
        return False
    
def fechoReflexivo(M):
    [a,b] = np.shape(M)
    if not is_reflexiva(M):
        MFR = M+np.eye(a)
        MFR[MFR != 0] = 1
        return MFR
    
fechoReflexivo(A)
        
# OU



def fechoReflexivo(M):
    [a,b] = np.shape(M)
    if not is_reflexiva(M):
        for i in range (0,a):
            M[i,i] = 1
        return M
    
'''
as funcoes para o fecho simetrico são a 1 e a 3, a 2 nao permite porque nao aplicamos o filtro
'''


'''
 6
'''

def equival(MR):
    [a,b] = np.shape(MR)
    if is_reflexiva(MR) and is_simetrica(MR) and isTrans(MR):
        print("A relação R é uma relação de equivaleência")
    else:
        print("A relação R não é uma relação de equivaleência")
        A = MR+np.eye(a)+MR.T # garantir a reflexividade e a simetria
        
        # garatir a transitividade
        MFT = np.zeros((a,b))
        
        for i in range(1,a+1):
            MFT += mpower(A,i) #Matriz dofecho transitivo
        MFT[MFT!=0] = 1
        
        return MFT
    
equival(A)

'''
 7
'''
def is_AntiSimetrica(MR):
    [a,b] = np.shape(MR)
    antisim = True
    
    for i in range(a):
        for j in range(b):
            if i!=j and MR(i,j) == 1 and MR(j,i) == 0:
                antisim=False
                
    if(not antisim):
        print("Não é AntiSimetrica")
    else:
        print("É AntiSimetrica")
    
def ordemParcial(MR):
    [a,b] = np.shape(MR)
    if is_reflexiva(MR) and is_AntiSimetrica(MR) and isTrans(MR):
        print("A relação R é uma relação de ordem parcial")
    else:
        print("A relação R não é uma relação de ordem Parcial")

ordemParcial(A)
    











