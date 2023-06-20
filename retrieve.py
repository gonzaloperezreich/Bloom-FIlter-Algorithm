#!/usr/bin/python

# codigo editado de https://stackoverflow.com/questions/26082360/python-searching-csv-and-return-entire-row
# en C, aquí hay un tutorial https://www.geeksforgeeks.org/relational-database-from-csv-files-in-c/ 

import csv
import sys
import numpy as np
import random as rd
from complement import genera_arreglo_b, genera_matriz_a
#se definen variables globales para tamaño de arreglo (M)y cantidad de funciiones de hash (k)
a=[[ 57694,  62380,  55325,  71664, 102439,  12384,  22558, 102654,  97353,
    78160,  95264,  12818,  52121,  20383,  73561,  19422,  24245,   2586,
    8562,  84487,  17714,  97924,  28253,  14684,  27247,  26144,  51883,
    101733,  76850,  95339, 100924,  82647,   9001,  43662,  91764,  33243,
    2156,  37152,  92572,  58804,  80159,  81471,  57302,  20240,  94880,
    57794,  54329, 100862,  38487,  29940,],
    [ 30320,  35090,  11357,  14874,  26470,  83530,  14174,   3942,  24877,
    22115,  44426,  75830,  12249,  95374,  87713,   7762,   4462,  16605,
    11991,  91468,  70457,  64981,  58513,  65278,  82249,  17765,  27028,
    39695,    865,  23254,  17000,  42669,  58260,  47186,  97951,  48410,
    17553,  21892,  85689,  71318,  47331,  14657,   6359,  43636,  59739,
    92442,   2401,  57348,  51700,  91481,],
    [ 24320,  38003,  34741,  94038,  75319,  44109,  39953,  16217,  80907,
    87547,  95127, 102475,  74893,  37319,  20852,  29729,  12776,  67996,
    33612,  94789,  69317,  23354,  50356,  68197,  29494,  55864,  96390,
    3887,  52529,  20727,  42437,  28133,  79941,  50968,  94407,  92317,
    102638,  82931,  29351,  76416,   6167,  62201,  29450,  45484,  69761,
    97191,  97056,  37225,  89044,  98226]]

b= [20895,  6654, 34532]

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