import numpy as np
import random as rd
import csv
import pandas as pd
import sys

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

def sample_n_from_csv(filename:str, n:int=100, total_rows:int=None) -> pd.DataFrame:
    if total_rows==None:
        with open(filename,"r") as fh:
            total_rows = sum(1 for row in fh)
    if(n>total_rows):
        print("Error: n > total_rows", file=sys.stderr) 
    skip_rows =  rd.sample(range(1,total_rows+1), total_rows-n)
    return pd.read_csv(filename, skiprows=skip_rows)

# Funcion que enera un arreglo de largo n con un porcentaje de elementos que estan en el csv de a
# a = [0, 1]
def genera_arrelo_busqueda(n, a):
    #arr = np.empty(n, dtype=object)
    datos = []
    elementoscsv = int(n*a)
    print(elementoscsv)
    #read csv, and split on "," the line
    dft = pd.read_csv('Popular-Baby-Names-Final.csv')
    dff = pd.read_csv('Films-Actualizado.csv')

    names = sample_n_from_csv('Popular-Baby-Names-Final.csv', n=elementoscsv)
#    test = sample_n_from_csv('Films-Actualizado.csv', n=(n - elementoscsv))

    for name in names:
        datos.append(name[0])
#    for s in test:
#        datos.append(s)

    return datos

print(sample_n_from_csv('Popular-Baby-Names-Final.csv', n=5))
print(genera_arrelo_busqueda(10, 0.5))