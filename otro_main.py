import csv
import sys
import numpy as np
import random as rd
import pandas as pd
import math
import time
from complement import genera_arreglo_b, genera_matriz_a, sacar_porcentaje_de_datos

#films tiene 3700 filas
#hay 93890 names
def hash(string, a, b, m): #funcion de hash
    ascii_lista = [ord(caracter) for caracter in str(string)]
    x = 0
    for i in range(len(ascii_lista)):
        x += ascii_lista[i]*a[i]
    x += b
    x = (x % primo) % m
    return int(x)


ns=[100,1000,10000,20000,60000,100000]
for n in ns:
    # create a dataframe after reading .csv file
    dataframe = pd.read_csv('Popular-Baby-Names-Final.csv') 
    D = dataframe.shape[0] #tamaño del csv
    print("trabajando con n= ", n)
    print("---------------------------------------------------------------------------")
    maxlen = 50 #solo dejamos los strings hasta con 50 caracteres
    primo= 10000019

    for e in [0.25, 0.1, 0.05, 0.01]: #probabilidades de error
        print("Empezando test con error " + str(e))
        # Calcular el tamaño del arregglo m y la cantidad de funciones k
        m = math.ceil(-D*math.log(e) / (math.log(2)**2))
        k = round(m/D * math.log(2))
        print("Se usara un arreglo de tamaño " + str(m) + " con " + str(k) + " funciones de hash")

        M = np.zeros(m)
        a = genera_matriz_a(k, maxlen)
        b = genera_arreglo_b(k)

        print("Inicio de ingresar Popular-Baby-Names-Final.csv")
        #read csv, and split on "," the line
        csv_file = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        #loop through the csv list
        for row in csv_file:
            nombre = row[0]
            for i in range(k):
                r = hash(nombre, a[i], b[i], m)
                M[r] = 1
        print("Se ingreso Popular-Baby-Names-Final.csv al filtro")
            
        for p in [80, 60, 40, 20]:
            buscar = sacar_porcentaje_de_datos('Popular-Baby-Names-Final.csv', 'Films-Actualizado.csv', p, n)
            print("Se genero una busqueda con " + str(p) + "%" + " de exito en busquedas")
            print("Inicio de busqueda con filtro")
            inicio = time.time()
            c = 0
            for s in buscar:
                #revisar filtro
                entrar = True
                for i in range(k):
                    r = hash(s, a[i], b[i], m)
                    if(M[r] != 1):
                        entrar = False
                        break
                if entrar == False:
                    c+= 1
                if entrar:       
                    for row in csv_file:
                        if s == row[0]:
                            pass
            fin = time.time()
            print("La busqueda demoro " + str(fin-inicio) + "s " + str(c))
            #print("Inicio de busqueda sin filtro")