import numpy as np
import random as rd
import pandas as pd

primo= 100019

#Definiremos Una matriz de tamañp k x max_length con k arrreglos de tamño max_length con valores aleatorios en [1,p-1]

def genera_matriz_a(k, max_length):
    a= np.zeros((k,max_length))
    for i in range(k):
        for j in range(max_length):
            a[i][j]= rd.randint(1, primo-1)
    
    return a

    
'''
def genera_matriz_a(k):
    a= np.zeros(k, dtype=np.int32)
    for i in range(k):
        a[i]= rd.randint(1, primo-1)
    return a
'''

#Definiremos un arreglo b de largo k que posee valores aleatorios entre [0,p-1]
def genera_arreglo_b(k):
    b=np.zeros(k, dtype=np.int32)
    for i in range(len(b)):
        b[i]=rd.randint(0,primo-1)
    
    return b


def sacar_porcentaje_de_datos(data1,data2, porcentaje,total_datos):
    df1 = pd.read_csv(str(data1))
    df2 = pd.read_csv(str(data2))
    cantidad_a_sacar = int((total_datos * porcentaje) // 100)
    cantidad_restante = total_datos-cantidad_a_sacar
    filas_aleatorias_df1 = df1.sample(cantidad_a_sacar, replace=True)
    filas_aleatorias_df2 = df2.sample(cantidad_restante, replace=True)
    filas_aleatorias = pd.concat([filas_aleatorias_df1, filas_aleatorias_df2])
    data_final = filas_aleatorias["Name"].to_numpy()
    np.random.shuffle(data_final)
    return(data_final)