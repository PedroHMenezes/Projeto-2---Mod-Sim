# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:55:23 2019

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#lista tempo
delta_t=0.001
tempo=np.arange(0,1800,delta_t)

#variáveis
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
Tamb=293
I = 4640/24 * A1
#lista_condição_inicial
lista_condicao=[300]
#funcao_dTdt

def var_T(lis_cond,t,P):
    Tcel=lis_cond[0]    
    Q = ((d/(km * A1)) + (1/(h * A1)) * (1/(h*A2)))
    divQ = (d/(km * A1)) + (1/(h * A1)) + (1/(h * A2))
    Req = Q/divQ
    Qsaida = 1/Req
    dTdt = (1/(m*c)) * (I+P-(Qsaida*(Tcel - Tamb)))
    return dTdt


#grafico_temperatura
lista_grafico= odeint(var_T,lista_condicao,tempo,args=(P,))

#Ajuste do gráfico
lista_C=[]
for i in lista_grafico:
    lista_C.append(i-273)
lista_minutos=[]
for i in tempo:
    lista_minutos.append(i/60)
#Atingindo temperatura de superaquecimento
for i in range(0,len(lista_C)):
    if lista_C[i]>=50:
        print(lista_minutos[i])
        break
        
# Criando lista de potencias
Pot=[2,3,4,5,6]
tempo_maximo=[]
# Plotando potencia por tempo
for i in Pot:
    i=0
    grafico_pot= odeint (var_T,lista_condicao,tempo,args=(i,))
    for j in range(0,len(grafico_pot)):
        if grafico_pot[j]>=323 and j==0:
            tempo_maximo.append(tempo[j])
            j+=1
plt.plot(Pot,tempo_maximo,'ro')
plt.xlabel("Potência do processor (W)")
plt.ylabel("Tempo para superaquecimento")
plt.grid(True)
plt.show()
            
            
    
    
#plotando gráfico
#plt.plot(lista_minutos,lista_C,color='red',label='Temperatura')
#plt.xlabel("Tempo em segundos")
#plt.ylabel("Temperatura em °C")
#plt.title("Temperatura por tempo")
#plt.grid(True)
#plt.legend()
#plt.show()