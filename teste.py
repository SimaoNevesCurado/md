# -*- coding: utf-8 -*-
"""
Created on Thu May 30 22:38:44 2024

@author: simao
"""

import math as mt
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power as mpower

#1

#(a) [1,5 val.] Determine o conjunto A por extensao

"""Definir o conjuto"""

U = set(range(-2500,1500))

A=set()

for x in U:
    if x % -4 ==0:
        A.add(x)
        
        
print(A)


#b
  
B = set(x for x in U if (5*x - 3) % 143 == (3 % 143))

C= set(U-(A|B) | (U-(A^B)))
len(C)        


#2
#a


# Função para calcular S(n)
def S(n):
    soma = 0
    for i in range(1, n+1):
        termo = (-1)**(i+1) / (i * 2**i)
        soma += termo
    return soma

n_valores = range(0,15)

for n in n_valores:
    sv=list()
    sv.append(S(n))
    
       
plt.plot(n_valores,sv,"*")

     
#b

sucessor = mt.log(1.5)

n=1

   while True:
    Sn = S(n)
    if abs(Sn - sucessor) < 10**-8:
        break
    n += 1


print(f"O menor valor de n para o qual |S(n) - ln(1.5)| < 10^-8 é: {n}")


#3

#a

def verifica_piriquito(numero):
    if (len(numero) != 13):
        return print("numero invalido")
    num_gerais= int(numero[:10])
    num_controlo = int(numero[10:])
    
    if(num_gerais % 511 == num_controlo):
        return print("nice")

#b

numero=3023218782213
numero=str(numero)

verifica_piriquito(numero)

"""
é frances..porque o resto da divisao dos 10 primeiros numeros por 511 dá os igual aos 3 ultimos numeros
"""

#4
#a 
import pandas as pd

FICHEIRO = pd.ExcelFile(r'C:\Users\simao\md\Material\Dados.xlsx')
F1 = pd.read_excel(FICHEIRO, 'Folha1', header=None)
MR=F1.to_numpy()
 
#b

def funcao3(M):
    [L,C]=M.shape
    A=M
    for i in range(2,L+1):
        A=A+np.linalg.matrix_power(M,i)
    A[A!=0]=1
    return A

#c
MS = MR + MR.T
MS[MS!=0]=1
print(MS)
     