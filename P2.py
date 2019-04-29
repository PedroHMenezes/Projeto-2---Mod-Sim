# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:55:23 2019

@author: User
"""
#Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#lista tempo
delta_t=0.001
tempo=np.arange(0,2700,delta_t)

#constantes
m=152
e=0.95
sigma=5.67e-8
A1 = 106.56e-4
A2 = (0.0079 * 0.069)*2 + (0.0079 * 0.142) * 2
c = 0.7
km = 1.68
h=10
d=2.5e-2
Tsol=5778
P=3.94
Tamb=283
I = 4640/24 * A1

#lista condição inicial
lista_condicao=[300]

#funcao_dTdt
def var_T(lis_cond,t,Tamb):
    #Pega o primeiro termo da lista condições
    Tcel=lis_cond[0]    
    #Numerador da Resistência equivalente
    Q = ((d/(km * A1)) + (1/(h * A1)) * (1/(h*A2)))
    #Denominador da Resistência equivalente
    divQ = (d/(km * A1)) + (1/(h * A1)) + (1/(h * A2))
    #Resistência equivalente
    Req = Q/divQ
    #dQ/dt
    Qsaida = 1/Req
    #dT/dt total(com entradas e saídas)
    dTdt = (1/(m*c)) * (I+P-(Qsaida*(Tcel - Tamb)))
    return dTdt

# Criando lista de potencias
lista_Tamb=[]
z=283
while z<313:
    lista_Tamb.append(z)
    z+=1
#Lista que identifica o tempo máximo para plotar junto a Temp ambiente
tempo_maximo=[]
# Criando lista Tamb por tempo
for i in lista_Tamb:
    #Contador para não guardar mais que um tempo de alcance
    #por lista de temperatura(nas diferentes temp ambientes)
    j=0
    #Odeint nas diferentes temp ambientes 
    grafico_Tamb= odeint (var_T,lista_condicao,tempo,args=(i,))
    #For utilizado para guardar o valor em que chega em 50°C
    for g in range(0,len(grafico_Tamb)):
        if grafico_Tamb[g]>=323 and j==0:
            tempo_maximo.append(tempo[g])
            j+=1
#Ajustando para plotar no gráfico
#K em C
lista_C=[]
for i in lista_Tamb:
    lista_C.append(i-273)
#Segundos em minutos
lista_minutos=[]
for i in tempo_maximo:
    lista_minutos.append(i/60)
#Plotando 
plt.plot(lista_C,lista_minutos,'ro')
plt.xlabel("Temperatura ambiente")
plt.ylabel("Tempo para superaquecimento")
plt.grid(True)
plt.show()
