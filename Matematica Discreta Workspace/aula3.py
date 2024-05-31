# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:10:31 2024

@author: ruben
"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt

# 4-

def z(n):
    soma = 0
    for i in range(1,n+1,1):
        soma += (1/2)**i
    return soma


X = np.arange(1,21)

Y = np.array([])

for k in range(1,21,1):
    Y = np.append(Y,z(k))
    
plt.plot(X,Y,"*")

i=2 # começar a dois porque nao faz sentido calcular o termo de 0
while((abs(z(i) - z(i-1))) >= 10**-10):
    i+=1
    
print(i)

# 5- 

def s(n):
    if(n % 3 == 0):
        return 2**-(n / 10) * (n / 3)
    else:
        return 3**-(n / 10) * n
    
X = np.arange(1,71)
Y = np.array([])

for x in range(1,71,1):
    Y = np.append(Y,s(x))


plt.plot(X,Y, "*")


###########
#         #
# FICHA 3 #
#         #
###########


# 1 -

# SET

A = {1,2,3,4}

# OU

A = set({1,2,3,4})

V = set() # Conjunto vazio

V = {} # não usar para fazer conjunto vazio

# Connjunto de impares de 1 - 30

impares = set(range(1,31,2))

#listas

L = list({1,2,3,4})

L2 =  ["mesa", 1,{1,34}]

L2[0] # devolver o indice 0

L3 = list(range(2,40,2))


# partição

P = list({1,2},{4,5,6},{9})

P1 = list({1,2}, {6,9}) # Não é partição de A porque 1,2 Unido com 6,9 não dá o A 

P2 = list({1,2},{4,5,6},{2,9}) # Não é partição de A porque a interçeção entre os elementos não é nulo, 1,2 & 2,9 === 2


L2[2] = 5 # redefinir o elemento da posição 2, para 5

L[1:3] #Devolve a sublista de L, do (i+1)-Èsimo item atÈ ao (j)-Èsimo



# 1

A = set({1,2,3,4})
B = set({3,4,5,6,7})
C = set({1,5,9,10})

U = set()

U = A|B|C

# Cardinalidade de U

len(U)

# Complementar de A:
    
compA = U-A

#diff de a por b

diff = A-B


# DIFF SIMETRICA

diffSim = A ^ B



# 2




# 3

def simdiff(A,B):
    return (A|B) - (A&B)

print(simdiff(A,B))

# 4


# 5

A = set(range(3,101,3))
B = set(range(70,141,7))
C = A^B

#A


# b)

len((A|C)&B)

# ex 6

pares = set(range(2,411,2))
multiplos7 = set(range(7,411,7))

resposta = pares - multiplos7
len(resposta)


# b

quadradosPerfeitos = set();

for i in range(1,411,1): # tem de ser 411 para tambem verificarmos o 410
    if(mt.sqrt(i)==int(mt.sqrt(i))):
        quadradosPerfeitos.add(i)

# ou

i=0

while(i <= 410 and (mt.sqrt(i)==int(mt.sqrt(i)))):
    quadradosPerfeitos.add(i)
    i+=1
    
# OU

n = 1
QP=set()

while n**2<=410:
    QP.add(n)
    n+=1    
    
# C

mult3 = set(range(3,411,3))

resposta = mult3-QP
    

# 7


Lista_Atividades=["Futebol", "Ioga", "Cinema", "Futebol", "Concertos", "Cinema", "Concertos"]

# aplicar um set á lista para remover os dupes

listaAtiv = set(Lista_Atividades)

# 8

b = {1,2,3,4}
p=[{1},{2},{3,4}]

uniao = set()
for i in range(0,len(p)):
    uniao = uniao | p[i] # o | faz a uniao
        
# ou 

uniao = set()
for c in p:
    uniao = uniao|c
    
if uniao == b:
    condicao1 = True
else:
    condicao1 = False
    print("P não é partição de b porque a união dos subconjuntos de P != b")


# assumir que a interseção é o vazio, caso contrario entra e mete false

condicao2 = True
for i in range(0,len(p)):
    for j in range(0,len(p)):
        if i != j and p[i] & p[j] != set():
            print("P não é particao de B uma vez que a sua interseção não é o conjunto nulo")
            condicao2 = False
            break
        
if condicao1 and condicao2:
    print("É partição")
else:
    print("Não é particao kekw")
    
    
# 9 

# assumir que a interseção é o vazio, caso contrario entra e mete false

condicao = True
for i in range(0,len(p)):
    for j in range(0,len(p)):
        if i != j and p[i] & p[j] != set():
            print("P não é particao de nenhum conjunto, porque a interseção é diferente do nulo")
            condicao = False
            break
        
if condicao:
    uniao = set()
    for c in p:
        uniao = uniao|c
        
    
import matrix_power as mpower
A = np.array([0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0])

A2 = mpower(A,2)
A3 = mpower(A,3)
A4 = mpower(A,4)