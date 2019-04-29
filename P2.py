# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:55:23 2019

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#lista tempo
<<<<<<< HEAD
delta_t=0.0001
tempo=np.arange(0,1800,delta_t)
=======
delta_t=0.001
tempo=np.arange(0,3600,delta_t)
>>>>>>> 2a7c0330896f0fa86933540df54bbc80209b8f82
#variáveis
m=152
e=0.95
sigma=5.67e-8
<<<<<<< HEAD
A1 = 106.56e-4
A2 = (0.0079 * 0.069)*2 + (0.0079 * 0.142) * 2
c = 0.7
km = 1.68
h=10
=======
A=106.56e-4
c=0.88
k=0.8
h=60
>>>>>>> 2a7c0330896f0fa86933540df54bbc80209b8f82
d=2.5e-2
Tsol=5778
P=3.94
Tamb=293
I = 4640/24 * A1
 


#lista_condição_inicial
lista_condicao=[300]
#funcao_dUdt
<<<<<<< HEAD



def var_T(lis_cond,t):
    Tcel=lis_cond[0]    
    Q = ((d/(km * A1)) + (1/(h * A1)) * (1/(h*A2)))
    divQ = (d/(km * A1)) + (1/(h * A1)) + (1/(h * A2))
    Req = Q/divQ
    Qsaida = 1/Req
    dTdt = (1/(m*c)) * (I+P-(Qsaida*(Tcel - Tamb)))
=======
def Var_T(listaT,t):
    Tcel=listaT[0]
    I=6.5*1000*A**3600
    Qdis=P*delta_t
    Conv=h*A*(Tamb-Tcel)
    CondConv= (Tamb-Tcel)/((1/(h*A))+(d/(k*A)))
    dTdt=((I+Qdis-Conv-CondConv)/(m*c))*delta_t
>>>>>>> 2a7c0330896f0fa86933540df54bbc80209b8f82
    return dTdt


#grafico_temperatura
<<<<<<< HEAD
lista_grafico= odeint(var_T,lista_condicao,tempo)

=======
lista_grafico=odeint(Var_T,lista_condicao,tempo)
>>>>>>> 2a7c0330896f0fa86933540df54bbc80209b8f82
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