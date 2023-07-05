import pandas as pd
import time
from complement import sacar_porcentaje_de_datos

dataframe = pd.read_csv('Popular-Baby-Names-Final.csv')


D = dataframe.shape[0]  # Tamaño del csv
ns=[100,1000,10000,20000,60000,100000]
for n in ns:
    print("trabajando con n= ", n)
    print("---------------------------------------------------------------------------")
    for p in [80, 60, 40, 20]:
        buscar = sacar_porcentaje_de_datos('Popular-Baby-Names-Final.csv', 'Films-Actualizado.csv', p, n)
        print("Se generó una búsqueda con " + str(p) + "%" + " de éxito en búsquedas")
        inicio = time.time()
        c = 0
        for nombre in buscar:
            if nombre in dataframe['Name'].values:
                c += 1
        print("Se encontraron " + str(c) + " nombres en el archivo CSV.")
        fin = time.time()
        print("La búsqueda demoró " + str(fin - inicio) + "s " + str(c))
        # print("Inicio de busqueda sin filtro")
