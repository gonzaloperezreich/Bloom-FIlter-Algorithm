import csv
import sys
import numpy as np
import random as rd
import pandas as pd
import math
import time
from complement import genera_arreglo_b, genera_matriz_a, sacar_porcentaje_de_datos
import bitarray
from sympy import Integer


def hash(string, a, b, m): #funcion de hash
    ascii_lista = [ord(caracter) for caracter in str(string)]
    x = 0
    for i in range(len(ascii_lista)):
        x += ascii_lista[i]*a[i]
    x += b
    x = (x % primo) % m
    return int(x)

'''
def hash(string, a, b, m):
    x = b
    for caracter in str(string):
        x += (ord(caracter)) * (a)
    x %= primo
    x %= m
    return int(x)
'''

# create a dataframe after reading .csv file
dataframe = pd.read_csv('Popular-Baby-Names-Final.csv') 
n = 5000 #tamaño de los test
D = dataframe.shape[0] #tamaño del csv
maxlen = 50 #solo dejamos los strings hasta con 50 caracteres
# primo= 10000019,10000003, 100003, 
primo = 100019

'''
print("Probando m óptimo")
for e in [0.25, 0.1, 0.05, 0.01, 0.001]: #probabilidades de error
    print("\n\nEmpezando test con error " + str(e))
    # Calcular el tamaño del arregglo m y la cantidad de funciones k
    mopt = math.ceil(-D*math.log(e) / (math.log(2)**2))
    print("el m óptimo es ", mopt)
    m = max(mopt-200000, 1)
    for m in range(m, mopt+300000, 100000):
        k = math.ceil( (m/D) * math.log(2))
        print("Se usara un arreglo de tamaño " + str(m) + " con " + str(k) + " funciones de hash")

        M = bitarray.bitarray(m)
        M.extend([0] * m)
        #M = np.zeros(m)
        a = genera_matriz_a(k)
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
            print("\nSe genero una busqueda con " + str(p) + "%" + " de exito en busquedas")
            print("Inicio de busqueda con filtro")
            inicio1 = time.time()
            for s in buscar:
                for i in range(k):
                    r = hash(s, a[i], b[i], m)
                    if M[r] == 0:
                        break
                #Si nunca hizo break, el algoritmo dice que lo encontró (podría ser FP)
            fin1 = time.time()
            print("La busqueda con filtro demoro " + str(fin1-inicio1) + "s ")
'''

'''
for e in [0.25, 0.1, 0.05, 0.01, 0.001]: #probabilidades de error
    print("\n\nEmpezando test con error " + str(e))
    # Calcular el tamaño del arregglo m y la cantidad de funciones k
    m = math.ceil(-D*math.log(e) / (math.log(2)**2))
    k = round( (m/D) * math.log(2))
    print("Se usara un arreglo de tamaño " + str(m) + " con " + str(k) + " funciones de hash")

    M = bitarray.bitarray(m)
    M.extend([0] * m)
    #M = np.zeros(m)
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

    # for i in range(len(M)):
        #print(M[i])

    for p in [80, 60, 40, 20]:
        buscar = sacar_porcentaje_de_datos('Popular-Baby-Names-Final.csv', 'Films-Actualizado.csv', p, n)
        print("\nSe genero una busqueda con " + str(p) + "%" + " de exito en busquedas")
        print("Inicio de busqueda con filtro")
        inicio1 = time.time()
        for s in buscar:
            for i in range(k):
                r = hash(s, a[i], b[i], m)
                if M[r] != 1:
                    break
            #Si nunca hizo break, el algoritmo dice que lo encontró (podría ser FP)
        fin1 = time.time()
        print("La busqueda con filtro demoro " + str(fin1-inicio1) + "s ")
        print("Inicio de busqueda sin filtro")
        inicio2 = time.time()
        for s in buscar:
            for row in csv_file:
                print(s)
                print(row[0])
                if s == row[0]:
                    break #Si hace break, lo encontró
        fin2 = time.time()
        print("La busqueda sin filtro demoro " + str(fin2-inicio2) + "s ")
'''


for e in [0.25, 0.1, 0.05, 0.01, 0.001]: #probabilidades de error
    print("\n\nEmpezando test con error " + str(e))
    # Calcular el tamaño del arregglo m y la cantidad de funciones k
    m = math.ceil(-D*math.log(e) / (math.log(2)**2))
    k = round( (m/D) * math.log(2))
    print("Se usara un arreglo de tamaño " + str(m) + " con " + str(k) + " funciones de hash")

    M = bitarray.bitarray(m)
    M.setall(0)
    print(M.count(True))
    #M = np.zeros(m)
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
    print(M.count(True))
    print("Se ingreso Popular-Baby-Names-Final.csv al filtro")

    # for i in range(len(M)):
        #print(M[i])

    for p in [80, 60, 40, 20]:
        buscar = sacar_porcentaje_de_datos('Popular-Baby-Names-Final.csv', 'Films-Actualizado.csv', p, n)
        print("\nSe genero una busqueda con " + str(p) + "%" + " de exito en busquedas")
        print("Inicio de busqueda con filtro")
        c=0
        csv_file = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        inicio1 = time.time()
        for s in buscar:
            #revisar filtro
            entrar = True
            for i in range(k):
                r = hash(s, a[i], b[i], m)
                if(M[r] == 0):
                    entrar = False
                    c+= 1
                    break                
            if entrar:       
                for row in csv_file:
                    if s == row[0]:
                        print("Encontrado")
                        break
            #Si nunca hizo break, el algoritmo dice que lo encontró (podría ser FP)
        fin1 = time.time()
        print("La busqueda con filtro demoro " + str(fin1-inicio1) + "s " + str(c))
        print("Inicio de busqueda sin filtro")
        csv_file = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        inicio2 = time.time()
        for s in buscar:
            # print(s)
            for row in csv_file:
                if s == row[0]:
                    break #Si hace break, lo encontró
        fin2 = time.time()
        print("La busqueda sin filtro demoro " + str(fin2-inicio2) + "s ")


