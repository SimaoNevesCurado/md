# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:36:34 2024

@author: ruben
"""

'''

Teste Prático 1

1.º Sem. 2021/2022 

'''

import math as mt
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power as mpower

'''
12-23 = 150

24-35 = 300

36-47 = 450

48-59 = 600

por cada duzia (12) + 150
'''

def teste(x):
    return (x // 12) * 150

# // faz a divisão inteira com floor, logo dividimos o numero de pessoas pelo numero de 1 grupo (12) e o floor
# disso vai nos dar a quantidade de grupos que existem, multiplicando por 150 para dar-nos o valor final


'''
Seja U o conjunto universo que cont´em todos os n´umeros inteiros positivos menores que
5500 e sejam U1, U2 e U3 subconjuntos do universo U definidos por:

U1 = {n ∈ U : n é múltiplo de 24};
U2 = {n ∈ U : (n − 3) ≡7 2} ; # congruente 2 modulo 7
U3 = {n^2 − 3n + 1 : 10 < n < 75 ∧ n ∈ N}.
'''

'''
Preencha os seguintes campos de modo a obter condic¸ ˜oes verdadeiras:
i. n (U1) =

ii. ___ é o número de elementos que pertencem a U e que não pertencem a qualquer
um dos subconjuntos Ui, para i = 1, 2, 3.


iii. n ((U1 ∪ U2) ⊕ U3) =
'''

U1 = set()

for i in range(1,5500):
    if(i % 24 == 0):
        U1.add(i)
        
len(U1)

'''
n(u1) = len(u1) = 229
'''    

'''
U2 = {n ∈ U : (n − 3) ≡7 2} ; # congruente 2 modulo 7
'''

U2 = set()

for i in range(1,5500):
    if(((i-3) % 7) == (2 % 7)):
        U2.add(i)
        
'''
U3 = {n^2 − 3n + 1 : 10 < n < 75 ∧ n ∈ N}.
'''

U3 = set()

for i in range(11,75):
   U3.add((i**2) - ((3*i)+1))
   
U4 = set()

for i in range (1,5500):
    if(not(i in U1 or i in U2 or i in U3)):
        U4.add(i)
        
len(U4)

'''
len(U4) = 4454 e o n´umero de elementos que pertencem a U e que n˜ao pertencem a qualquer
um dos subconjuntos Ui, para i = 1, 2, 3.
'''


'''
n ((U1 ∪ U2) ⊕ U3) =
'''

# (+) = A ∪ B \ A ∩ B
# logo: (U1 ∪ U2) ⊕ U3) = U1 ∪ U2 ∪ U3 \ U1 ∩ U2 ∩ U3


# b)

intersection = set()

for i in range(1,5500):
    if (i in U1 and i in U2) or (i in U1 and i in U3) or (i in U2 and i in U3):
        intersection.add(i)

B1 = (U1|U2|U3)-(U2&(U1|U3))
B2 = (U1|U2|U3)-((U1&U2)&U3)

uniao = U1 | U2 | U3

for i in B1:
    if i in uniao and i in intersection:
        print(i)
        
for i in B2:
    if i in uniao and i in intersection:
        print(i)
        
'''
resposta certa = B1 = (U1|U2|U3)-(U2&(U1|U3))
'''

# 3-

'''
liga-se as 08:00 = instante (0,0,0)

desliga-se as 23:00

'''

def reclame(h,m,s):
    H = h * 60 * 60
    M = m * 60
    S = H+M+s
    
    r = S % 90 # 90 Segundos porque ele fica aceso 45 segundos depois desligado 45 segundos, então se o modulo for entre 0-44 está aceso se for 45+ está desligado
    
    if r<45:
        print("Aceso")
    else:
        print("Desligado")


reclame(12,37,10)


# 4
'''
n1 == 2 

n2 == 6

Un == 2* U(n-1) + 4*U(n-2)
'''

#a
def u(n):
    if n==1:
        return 2
    elif n==2:
        return 6
    elif n>=3:
        return 2*u(n-1) + 4*u(n-2)
    else:
        print("INSIRA UM VALOR VALIDO NENGUE")

#b)

for i in range (1,100000000):
    if u(i) > 10**8:
        print(i)
        break
    
# Resposta: 17

#c

y = list()
for i in range(1,21):
    y.append(u(i+1) / u(i))
    
x = list()  
x = np.arange(1,21)  

plt.plot(x,y,'*')

'''
resposta : b
'''

'''
5
'''

def fecho_sim(M):
    [a,b] = np.shape(M)
    for i in range(0,a):
        for j in range(0,b):
            if M[i,j] == 0:
                M[j,i] = 0
    return M

def fecho_trans(M):
    [a,b] = np.shape(M)
    
    MT = np.zeros((a,b))
    
    for i in range(1,a+1):
        MT = MT+np.linalg.matrix_power(M,i)
    return MT

A = [[0,1,0],[1,1,1],[0,0,0]]

fecho_sim(A)
fecho_trans(A)

'''
resposta: D 

porque o fecho_sim vai apenas transformar a matriz toda em 0's
e a fecho_trans nao aplica o filtro
'''

#b)

# fixing fecho_trans

# aplicar-lhe o filtro antes do return

def fecho_transFixed(M):
    [a,b] = np.shape(M)
    
    MT = np.zeros((a,b))
    
    for i in range(1,a+1):
        MT = MT+np.linalg.matrix_power(M,i)
        MT[MT!=0] = 1
    return MT

fecho_transFixed(A)
