import csv
import sys
import numpy as np
import random as rd
import pandas as pd
import math
from complement import genera_arreglo_b, genera_matriz_a, genera_arrelo_busqueda

# create a dataframe after reading .csv file
dataframe = pd.read_csv('Popular-Baby-Names-Final.csv') 

n = 10000 #tamaño de los test
D = dataframe.shape[0] #tamaño del csv
maxlen = 50 #solo dejamos los strings hasta con 50 caracteres
primo= 104723

for e in [0.25, 0.1, 0.05, 0.01]: #probabilidades de error
    print("Empezando test con error " + str(e))
    # Calcular el tamaño del arregglo m y la cantidad de funciones k
    m = math.ceil(-D*math.log(e) / (math.log(2)**2))
    k = round(m/D * math.log(2))
    print("Se usara un arreglo de tamaño " + str(m) + " con " + str(k) + " funciones de hash")
    
