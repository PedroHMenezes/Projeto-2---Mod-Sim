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
tempo=np.arange(0,30,delta_t)
#variáveis
m=152
e=0.95
sigma=5.67e-8
A=106.56e-4
c=0.88
k=0.8
h=10
d=2.5e-2
Tsol=5778
P=3.94
Tamb=293
#lista_condição_inicial
lista_condicao=[300]
#funcao_dUdt
def Var_T(listaT,t):
    Tcel=listaT[0]
    I=e*sigma*A*Tsol**4
    Qdis=P*delta_t
    Conv=h*A*(Tamb-Tcel)
    CondConv= (Tamb-Tcel)/((1/(h*A))+(d/(k*A)))
    dTdt=((I+Qdis-Conv-CondConv)/(m*c))*delta_t
    return dTdt

#grafico_temperatura
lista_grafico=odeint(Var_T,lista_condicao,tempo)
print(lista_grafico[:])
lista_C=[]
for i in lista_grafico:
    lista_C.append(i-293)
#plotando gráfico
plt.plot(tempo,lista_C,color='red',label='Temperatura')
plt.xlabel("Tempo em minutos")
plt.ylabel("Temperatura em °C")
plt.grid(True)
plt.legend()
plt.show()