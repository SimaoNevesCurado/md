# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:19:56 2024

@author: ruben
"""

import math as mt
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power as mpower
import pandas as pd

''' 
1 -

a) 

'''

def P(t):
    """

    onde k È um parãmetro real positivo e t é o tempo discreto, em segundos.
    função p(t)= 300 / (3 + 2 * math.cos(t / 14400) * math.exp((0.2 * t) / 3600))
    considerando k = 0.2 temos que :
    """
    return 300 / (3 + 2 * mt.cos(t / 14400) * mt.exp(-(0.2 * t) / 3600))



'''b) '''

''' valores de t a cada hora até 75 horas em segundos '''
valores_t = np.arange(0, 75*3600, 3600)

''' cálculo dos valores de P(t) nessas 75 horas '''

valores_P = [P(t) for t in valores_t]

''' Gráfico '''
plt.figure(figsize=(10, 6))
plt.plot(valores_t, valores_P, color='blue')
plt.title('Número de Bactérias ao Longo do Tempo')
plt.xlabel('Tempo (segundos)')
plt.ylabel('Número de Bactérias')
plt.grid(True)
plt.show()


''' c) '''
#Valor inicial e Valor com mais 1 segundo 

t = 0

Pt = P(t)
P_t_mais_1 = P(t + 1)

while (abs(Pt - P_t_mais_1) >= 1e-7):
    t = t + 1
    Pt = P_t_mais_1
    P_t_mais_1 = P(t + 1)


'''
Convertendo o tempo decorrido para horas e minutos
'''

horas = int(t / 3600)
minutos = int((t % 3600) / 60)

print(f"Valor aproximado de L: {Pt:.8f}")
print(f"Tempo decorrido necessário: {horas} horas e {minutos} minutos")



# EX - 2

ficheiro = pd.ExcelFile(r'D:\ESTG Stuff\Matematica Discreta Workspace\TrabalhoGrupo4\Excel\Base_Dados.xlsx')

# a) 

def aniversario(x, y): 
    aniversario_x = x[:5]
    aniversario_y = y[:5]

    if aniversario_x == aniversario_y:
        return True 
    else:
        return False


'''
b) - JustiÖque porque È que a relaÁ„o R È uma relaÁ„o de equivalÍncia. Sendo BD a matriz linha que contÈm
a base de dados da empresa (array bidimensional com as identiÖcaÁıes dos trabalhadores de acordo com o formato
indicado) e x a string de um dado trabalhador, construa uma funÁ„o com o nome classe(BD,x) que devolva a
classe de equivalÍncia de x. Indique o que È que esta funÁ„o permite determinar, no contexto do problema.
'''

def is_reflexiva(MR):
    [a,b] = np.shape(MR)
    diagonalPrinc = np.diag(MR)
    diagIdent = np.diag(np.eye(a))
    if(diagonalPrinc.all() == diagIdent.all()):
        return True
    else:
        return False

def is_simetrica(M):
    [a,b] = np.shape(M) # [linhas , colunas]
    for i in range(0,a):
        for j in range(0,b):
            if (M[i,j] != M[j,i]):
               return False
    return True

def is_transitiva(M):
    [a,b] = np.shape(M) # [linhas , colunas]
    # verificar se a Matriz original != Matriz Original + matriz de r apos r, n vezes em que n é o numero de elementos da relação porque temos de verificar até dar 0 novos elementos
    McomposM = mpower(M,2)
    MTrans = McomposM + M
    MTrans[MTrans != 0] = 1
    return np.array_equal(M,MTrans)

def equival(MR):
    if is_reflexiva(MR) and is_simetrica(MR) and is_transitiva(MR):
        print("A relação R é uma relação de equivaleência")
    else:
        print("A relação R não é uma relação de equivaleência")
        
dados = []
    
for folha in ficheiro.sheet_names:
    df = pd.read_excel(ficheiro, folha, header=None)
    primeira_linha = df.iloc[0]
    string_dados = "/".join(primeira_linha.astype(str).tolist())
    dados.append(string_dados)
    
def classe(BD, x):
    
    dia_mes_x = x[:5]
    equivalencia = []
  
    for trabalhador in BD:
        dia_mes_trabalhador = trabalhador[:5]
        if dia_mes_x == dia_mes_trabalhador:
            equivalencia.append(trabalhador)
    
    return equivalencia

    
'''
R: R é uma relação de equivalência visto que comprova os 3 requesitos, ser reflexiva, simetrica, e transitiva
'''

'''
C
'''

ficheiro = pd.ExcelFile(r'D:\ESTG Stuff\Matematica Discreta Workspace\TrabalhoGrupo4\Excel\Base_Dados.xlsx')
F1 = pd.read_excel(ficheiro, 'Folha4', header=None)
A = F1.to_numpy()

a=len(A)
niver = 0

for i in range(a):
    if '10/9' in A[i, a]:
        niver += 1

print(niver)


'''
D - 
'''

def prémio(Ano,BD):
    if Ano < 1956:
        print("Ano inválido")
    else:
        if Ano%10 == 6:
            print(f"Existe entrega no ano {Ano}")
        elif Ano%10 > 6:
            Ano = ((Ano//10)+1)*10+6
            print(f"A entrega será no ano {Ano}")
        elif Ano%10 < 6:
            Ano = ((Ano//10)+1)*10+6
            print(f"A entrega será no ano {Ano}")
        c=set()
        l = len(BD)
        for i in range(0,l):
            x=int(BD[i][11:])
            if x-Ano >= 8:
                c.add(BD[i])

# EX - 3 


ficheiro = pd.ExcelFile(r'D:\ESTG Stuff\Matematica Discreta Workspace\TrabalhoGrupo4\Excel\Grafo.xlsx')
folha1 = pd.read_excel(ficheiro, 'Folha1', header=None)
A = folha1.to_numpy()

'''

A) A partir da Golegã é possÌvel seguir diretamente para quantos locais?

'''
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
    


graus(A,7)

'''

R: É possivel seguir diretamente para 1 local, Damaia visto que na posição da matriz de adjacências [6,4], está um 1, e com a função "graus" podemos ver que o output do 
"grauSaida" é 1.


'''

'''

B) Existe alguma localidade da qual não parta qualquer transporte? Em caso aÖrmativo, indique qual.
    
'''

def poco(A):
    [a,b] = np.shape(A)
    pocos = []
    for i in range(0,a):
        if graus(A,i+1)[0] == 0:
            pocos.append(i+1)
    if(pocos == set()):
        print("G Não tem Poços")
    else:
        print("G tem Poços")
        
    return pocos
            
poco(A)

'''

R: Sim Faro Visto que ao analisarmos a matriz de adjacências na linha de Faro (6) - vemos que não tem um 1, logo é um poço.

Tambem podemos verificar isso pela função "poco" que nos devolve o indice da linha caso tenha um poço

'''


'''
C - É possível estabelecer uma rota da Golegã para Espinho?

'''

   
[a,b] = np.shape(A)
B = np.zeros((a,a))
for i in range(0,a+1):
    if(B[6,4] == 0) and i<=6:
        B = B+mpower(A,i)
    elif B[6,4] == 0 and i==6:
        print(f"É Possivel ir até Espinho a partir de Golegã com: {i} conexões")
        #B[B!=0]=1
        #P = B
        break;
    else:
        print("Não é possivel ir de Galegã até Espinho")
        #B[B!=0]=1
       # P = B
        break;

    

'''

R: Não é possivel ir de Galegã até Espinho, comprovada pelo código anterior, onde fazendo a matriz P, matriz de caminhos, na posição [6,4] 
(interseção da posição de Galegã e de Espinho) encontramos um 0
    
'''

'''
D - O motorista que Özer a rota que tem como local de partida Alcochete e local de chegada Faro beber no mÌnimo, quantos cafés?

'''

def bebeCafes(A,v,u): # Matriz, vertice partida, vertice chegada
    [a,b] = np.shape(A)
    B = np.zeros((a,a))
    for i in range(0,a+1):
        B += mpower(A, i)
      
    return B[v-1,u-1] + 1 # o +1 é para o café que ele bebe no inicio
       
bebeCafes(A,1,6)

# NOTA -> PODE NAO SER ASSIM PORQUE TOU A VERIFICAR COM A B TODA ATÉ AO FIM ASK BRUNO MAYBE SO TENHO DE IR ATÉ ONDE VAI DE 0 PARA UM NUMERO?
'''

R: No minimo o motorista vai ter de beber no minimo 5 cafés 

'''


'''

E) É possÌvel um motorista ir de Damaia a Alcochete bebendo exatamente 5 cafÈs? Em caso aÖrmativo, de quantas formas diferentes? 

'''

def caminho_compK(A,k,v,u):
    ak = mpower(A,k-1)
    print(f"Existe {ak[v-1,u-1]} caminhos de comprimento {k} do vertice {v} para o vertice {u}")
    


caminho_compK(A,5,4,1)

'''
R: Sim é possível visto que ao fazermos a matriz de comprimentos 5, com a função caminho_compK, obtemos na posição dos vertices
[4,1] ou seja, na posição Damaia -> Alcochete um valor diferente de 0, o número deste valor indica-nos quantas formas diferentes
há de beber exatamente 5 cafés. Sendo este número = 2, indica-nos que há 2 formas diferentes de beber exatamente 5 cafés.
'''

'''
F - Como classiÖca este grafo quanto á conectividade? Justifique a sua resposta tendo em atenção ocontexto do problema.

'''

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
    # ou 
    
    if 0 in P:
        print("Grafo é Fortemente Conexo")
        return True
    else:
        print("Grafo não é Fortemente Conexo")
        return False
    
    if forteCon:
        print("Grafo é Fortemente Conexo")
    else:
        print("Grafo não é Fortemente Conexo")
    return forteCon 

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

def isFracamenteConexo(A):
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
        print("Grafo é Fracamente Conexo")
    else:
        print("Grafo não é Fracamente Conexo")
    return fraCon

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

conectividade(A)

'''
R - O Grafo é fortemente conexo, e no contexto deste problema, significa que não dentro deste conjunto de locais de entrega
há sempre pelo menos, 1 caminho para lá chegar, ou seja, não há nenhuma localidade ao qual não se consiga chegar.
'''



''' 4 '''
def is_reflexiva(M):
    [a,b]=M.shape
    return np.trace(M)==a

def is_transitiva(M):
    [a,b]=M.shape
    R=M
    for i in range(1,a):
        R=R+mpower(M, i+1)
    R[R!=0]=1
    return np.array_equal(M, R)

def is_antissimetrica(M):
    [a,b]=M.shape
    for i in range(a):
        for j in range(b):
            if i!=j and M[i,j]==1 and M[j,i]==1:
                return False
    return True

def caminho(M):
    [a,b]=np.shape(M)
    P=np.zeros((a,a))
    for i in range(1,a+1):
        P=P+mpower(M, i)
    P[P!=0]=1
    return P

''' 4a '''
def not_comp(M,i):
    if is_reflexiva(M) & is_antissimetrica(M) & is_transitiva(M):
        C=set()
        [a,b]=np.shape(M)
        P=caminho(M)
        for j in range(0,a):
            if P[i-1,j]==0:
                C.add(j+1)
        return C
    else:
        print(f"A relação {M} não é uma relação de ordem parcial.")

''' 4b ''' 
def Full_order(S):
    a=len(S)
    M=np.zeros((a,a))
    for i in range(0,a):
        for j in range(i,a):
            M[i,j]=1
    return M
