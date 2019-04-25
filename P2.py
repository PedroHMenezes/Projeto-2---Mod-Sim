# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:55:23 2019

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#lista tempo
delta_t=0.01
tempo=np.arange(0,30,delta_t)
#variáveis
m=152
e=0.95
sigma=5.67e-8
A=106.56e-4
c=0.22
k=205
h=10
d=2.5e-2
Tsol=5778
#lista_condição_inicial
lista_condicao=[293]
#funcao_dUdt
def Var_T(listaT,t):
    T=listaT[0]
    P=3.94*t
    U=m*c*T
    I=e*sigma*A*Tsol**4
    Cond=U*k*A/d
    Conv=U*h*A
    dTdt=(P+I-(Cond+Conv))/(m*c)
    T=T+dTdt
    return T
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