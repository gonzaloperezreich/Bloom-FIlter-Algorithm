import time
import bitarray
import numpy as np

# Crear un bitarray con valores de 0 y 1
bit_array = bitarray.bitarray([0, 1] * 100000)

# Crear un ndarray de NumPy con valores de 0 y 1
nd_array = np.array([0, 1] * 100000)

# Medir el tiempo de recorrido del bitarray
start_time = time.time()
for bit in bit_array:
    pass
bitarray_time = time.time() - start_time

# Medir el tiempo de recorrido del ndarray de NumPy
start_time = time.time()
for element in nd_array:
    pass
ndarray_time = time.time() - start_time

# Imprimir los tiempos de recorrido
print("Tiempo de recorrido del bitarray:", bitarray_time)
print("Tiempo de recorrido del ndarray de NumPy:", ndarray_time)
