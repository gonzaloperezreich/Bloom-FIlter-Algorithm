import numpy as np
import random as rd
max_length=50
k=3
primo= 104723

#Definiremos Una matriz de tamañp k x max_length con k arrreglos de tamño max_length con valores aleatorios en [1,p-1]
def genera_matriz_a():
    a= np.zeros((k,max_length))
    for i in range(k):
        for j in range(max_length):
            a[i][j]= rd.randint(1, primo-1)
    
    return a


#Definiremos un arreglo b de largo max_lenght que posee valores aleatorios entre [0,p-1]
def genera_arreglo_b():
    b=np.zeros(k)
    for i in range(len(b)):
        b[i]=rd.randint(0,primo-1)
    
    return b


a= genera_matriz_a()
b=genera_arreglo_b()
print(a)
print(b)
