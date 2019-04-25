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
tempo=np.arange(0,1,delta_t)
#variáveis
m=152
e=0.95
sigma=5.67e-8
A=106.56e-4
c=0.72
k=0.8
h=10
d=2.5e-2
Tsol=5778
P=3.94
#lista_condição_inicial
lista_condicao=[300,293]
#funcao_dUdt
def Var_T(listaT,t):
    Tcel=listaT[0]
    Tamb=listaT[1]
    I=e*sigma*A*Tsol**4
    Qdis=P*delta_t
    Conv=h*A*(Tamb-Tcel)
    CondConv= (Tamb-Tcel)/((1/(h*A))+(d/(k*A)))
    dTdt=((I+Qdis-Conv-CondConv)/(m*c))*delta_t
    Tcel=Tcel+dTdt
    return Tcel,Tamb

#grafico_temperatura
lista_grafico=odeint(Var_T,lista_condicao,tempo)
print(lista_grafico[:])
#plotando gráfico
plt.plot(tempo,lista_grafico[:,0],color='red',label='Temperatura')
plt.xlabel("Tempo em minutos")
plt.ylabel("Temperatura em K")
plt.grid(True)
plt.legend()
plt.show()