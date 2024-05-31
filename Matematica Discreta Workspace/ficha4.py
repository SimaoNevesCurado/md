# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:02:10 2024

@author: ruben
"""

import math as mt

# funcao floor

mt.floor(2.6)
mt.floor(-2.6)

# funcao ceiling

mt.ceil(3.7)
mt.ceil(-3.7)

# funcao inteiro

int(8.9)

# funcao resto

235 % 3

# 456 é divisivel por 43?

456 % 43 == 0


#funcao fatorial

mt.factorial(5)

# operacoes com strings

"Quadro"

# ir buscar o 1º elemento 

"Quadro"[0]


# ir buscar o "dro" elemento 

"Quadro"[3:6] # ir do D até ao o porque funciona de 3 até 6-1

"Quadro"[3:] # ir do D até ao fim da string

# nao interromper o texto

x=3;y=6

print("O valor de x é ", x ,"e o valor de y é ", y) # interrompendo

print(f"o valor de x e {x} e o valor de é {y}") # nao interrompido



# EXERCICIOS 

# EX 1

# O armazenamento de dados em mem´oria ou a transmiss˜ao de dados atrav´es de uma rede s˜ao
# representados atrav´es de uma ”string” de bytes (1 byte = 8 bits). Crie um script em Python que:

#a) determine quantos bytes s˜ao necess´arios para codificar 100 bits de dados.

mt.ceil(100/8) # arrendondamos para cima com o ceiling para caso N não seja divisivel por J darmos mais 1 para compensar

# (b) construa uma func¸ ˜ao, designada por conversor, que devolva quantos bytes s˜ao necess´arios para codificar x bits de dados


def convversor(nBits):
    return mt.ceil(nBits/8)

convversor(100)

# 2 Fazendo uso dos comandos floor e ceil, construa uma func¸ ˜ao chamada inteiro que de-volva a parte inteira do n´umero real x

def inteiro(numRecebido):
    if(numRecebido > 0):
        return mt.floor(numRecebido)
    else:
        return mt.ceil(numRecebido)
    
    
inteiro(3.64)
inteiro(-4.3)


# 3- Um ano bissexto possui 366 dias e ´e sempre m´ultiplo de 4. Por´em, h´a casos especiais de anos que,
# apesar de m´ultiplos de 4, n˜ao s˜ao bissextos: s˜ao aqueles que tamb´em s˜ao m´ultiplos de 100 e n˜ao
# s˜ao m´ultiplos de 400. Construa uma func¸ ˜ao com o nome bissexto que permita determinar se
# um dado ano X ´e um ano bissexto.


def bisexto(ano):
    if ((ano % 4 != 0) or (ano % 100 == 0 and ano % 400 != 0)):
        print("not bisexto")
    else:
        print("bisexto")
        

bisexto(2024)
bisexto(2103)
bisexto(2100)

# 4 Construa uma func¸ ˜ao com o nome F que permita obter o termo de ordem n da sucess˜ao de Fi-
# bonacci, para n ≥ 1. Recorde que os n´umeros de Fibonacci Fn s˜ao os n´umeros que comp˜oe a
# seguinte sucess˜ao de n´umeros inteiros: 1, 1, 2, 3, 5, 8, 13, ....
# Em termos matem´aticos, a sucess˜ao de Fibonacci Fn ´e definida recursivamente por:

def fibonnaci(x):
    if x == 1 or x == 2:
        return 1
    
    return fibonnaci(x-1) + fibonnaci(x-2)

fibonnaci(7)

# sem recursividade cuz better

def fib(n):
    if n ==1 or n ==2:
        return 1
    n1 = 1
    n2 = 1
    for i in range(3,n+1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n3

fib(50)
fib(4)
# 5 Construa uma func¸ ˜ao designada por soma Fib que receba um inteiro k e devolva a soma dos primeiros k termos da sucess˜ao de Fibonacci.

def somaFib(x):
    soma=0
    for i in range(1,x+1):
        soma += fib(i)
    return soma

somaFib(5)

# 6 
import numpy as np

def termosFib(s):
    vetorTermos = np.array([])
    i=1
    while somaFib(i)<=s:
        vetorTermos = np.append(vetorTermos, fib(i))
        i+=1
    #for i in range (1,s+1):
     #   if somaFib(i)<=s:
      #      vetorTermos.append(i)
    return vetorTermos

termosFib(23)
        
#7 - O n´umero de ouro, geralmente denotado por φ (phi), ´e dado por φ = (1 + √5) / 2 .

phi = (1 + mt.sqrt(5)) / 2

aprox = 10 ** -10

num = 2

while (abs(fib(num) / fib(num - 1) - phi)) > aprox:
    num+=1
    
print(fib(num) / fib (num-1)) # para mostrar a aproximação 


# b-

import matplotlib.pyplot as plt
y = np.array([])

for i in range(2,num+1):
    y=np.append(y, fib(i) / fib (i-1))
    
plt.plot(y, "*")


#9 - 

ANO = 2024
A = ANO % 100 #para ter o ZW

#ou 

ANO = 2024

ANO = input("indique o ano: ")
ANO = int(ANO)
A = ANO % 100 #para ter o ZW

# A = ANO[2:4] # OU ANO[2:] PARA TER OS ULTIMOS 2 CARACTERES "ZW"

seculo = mt.ceil(ANO / 100)

TOTAL = 50 + A + ((seculo - 1)//4) + (A//4) - 2 * (seculo - 1)

D = TOTAL % 7

SEMANA = ["DOMINGO", "SEGUNDA-FEIRA", "TERÇA-FEIRA", "QUARTA-FEIRA", "QUINTA-FEIRA","SEXTA-FEIRA", "SABADO"]

print(f"No ano {ANO} o Natal será num(a) {SEMANA[D]}")


# 10-

numeroSerie = "M50027558701"

letra = numeroSerie[0]

letrasPais = ["R","S","T","U","M","N"]

beta = letrasPais.index(letra) + 1

# or

for i in range(0, len(letrasPais)):
    if(letra == letrasPais[i]):
        beta = i+1

for n in range(1, len(numeroSerie)):
    beta += int(numeroSerie[n])
    
if (beta % 9 == 0 % 9): # if(beta % 9 == 0)
    print(f"Nota: {numeroSerie} é válida");
else:
    print(f"Nota: {numeroSerie} não é válida");


#11 AND 12- tpc



