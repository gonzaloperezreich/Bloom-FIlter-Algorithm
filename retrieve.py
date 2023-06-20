#!/usr/bin/python

# codigo editado de https://stackoverflow.com/questions/26082360/python-searching-csv-and-return-entire-row
# en C, aquí hay un tutorial https://www.geeksforgeeks.org/relational-database-from-csv-files-in-c/ 

import csv
import sys
import numpy as np
import random as rd
from complement import genera_arreglo_b, genera_matriz_a
#se definen variables globales para tamaño de arreglo (M)y cantidad de funciiones de hash (k)
a= [[ 54906,  57579,  63612,  78826,  44793,  55884,  60222,  16131,  69060, 19918,  77329,  89922,  56260,  14414,  19780] , 
    [ 77666,  20440,  67018,  96669,  42222,  30864,  73275,   1870,  13750, 16714,  52300,  39032,  53900,  31230,  75910], 
    [ 8873,  71890,   4479,  13988,  89665,  50746,  47527,  34049,  40523, 64386,  27614,  38983,   2967,  88976,  91313],
    [  6847,   1008,  68034,  58045,  58129,  46540,   9669,  29587,  37889, 37290,   5972,  54669,  83051,  47390,  48135],
    [ 70558,    359, 102407,  63911,  88290,  75300,  92803,   4401,   5615, 84275,  16449,   7356,  56178,  69438,  98757]]
b= [784, 15941, 27590, 49174, 89809]

matriz = np.array(a)
arreglo= np.array(b)
m=180000
k=1
M= np.zeros(m)
max_length= 15
primo= 104723

def hash(string, a, b):
    ascii_lista = [ord(caracter) for caracter in string]
    x=0
    for i in range(len(ascii_lista)):
        x+= ascii_lista[i]*a[i]
    x+=b
    x= (x%primo)%m
    return x



nombres=['CHARLES', 'GONZALO']
for nombre in nombres:
    for i in range(k):
        x= hash(nombre, a[i], b[i])
        M[x]=1
    






print(M)







# Nombre en mayúsculas a quien se desea buscar (se pasa desde la shell)
#name = input('¿Qué nombre desea buscar?\n')

#read csv, and split on "," the line
#csv_file = csv.reader(open('Film-Names.csv', "r"), delimiter=",")

# print(max)
# #loop through the csv list
# for row in csv_file:
#     #print(row[0])
#     # Si el elemento existe, se imprime lo siguiente
#     if name == row[0]:
#         print('Existe el elemento')
        
    
# print(".")