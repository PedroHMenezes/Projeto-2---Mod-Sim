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

def var_T(lis_cond,t):
    Tcel=lis_cond[0]    
    Q = ((d/(km * A1)) + (1/(h * A1)) * (1/(h*A2)))
    divQ = (d/(km * A1)) + (1/(h * A1)) + (1/(h * A2))
    Req = Q/divQ
    Qsaida = 1/Req
    dTdt = (1/(m*c)) * (I+P-(Qsaida*(Tcel - Tamb)))
    return dTdt


#grafico_temperatura
lista_grafico= odeint(var_T,lista_condicao,tempo)

#Ajuste do gráfico
lista_C=[]
for i in lista_grafico:
    lista_C.append(i-273)
#plotando gráfico
plt.plot(tempo,lista_C,color='red',label='Temperatura')
plt.xlabel("Tempo em segundos")
plt.ylabel("Temperatura em °C")
plt.grid(True)
plt.legend()
plt.show()