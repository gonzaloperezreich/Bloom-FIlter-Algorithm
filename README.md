# Bloom-FIlter-Algorithm
## Español:
El filtro de bloom es una herramienta que facilita la búsqueda de elementos en grandes repositorios de datos.
En este caso en particular se creó esta estructura y se sometió a la busqueda de diferentes nombres de bebés que se encuentran registrados en el archivo Popular-Baby-Names-Final.csv para evaluar su utilidad y tiempo de acción.
Claramente no solo se deberían buscar únicamente elementos de dicha base de datos sino que deberían buscarse elementos que no formaran parte de dicha base. Para esto se utilizó el archivo Film-Names.csv, el cual valga la redundancia poseía 3809 nombres de películas diferentes y serían mezcladas con la data de bebés para hacer búsquedas tanto fructuosas como infructuosas usando el filtro.

## English:
The Bloom Filter is a tool that facilitates the search for elements in large data repositories. In this particular case, this structure was created and subjected to the search for different baby names registered in the Popular-Baby-Names-Final.csv file to evaluate its usefulness and performance time.

Clearly, it should not only search for elements exclusively from that database, but also search for elements that are not part of that base. For this purpose, the Film-Names.csv file was used, which, redundantly, contained 3809 different movie names that would be mixed with the baby data to perform both successful and unsuccessful searches using the filter.

The Bloom Filter is an efficient data structure that uses a bit array and hash functions to determine if an element is possibly in a set. It offers probabilistic results, meaning it can tell if an element is definitely not in the set or it might be in the set. This makes it useful for quick membership queries in large datasets.

# Limpieza de datos
## Español:
En particular se podrá observar que la data de peliculas no es la unica que posee el repositorio, esto se debe a que se decidió pre-procesar la data, lo cual se puede observar en limpieza.ipynb.

Esto primeramente pues parte del desarrollo del filtro dependería del largo máximo que pudiese haber en la base y el registro de peliculas poseía casos de largos extremadamente largos en comparación con el promedio. Es por ello que se decidió cortar a largo maximo 50.

Adicional a aquello, se puede observar que los últimos registros de peliculas están acompañados de (;;;;;), lo cual tambien fue eliminado. 

Finalmente se borraron los nombres de películas que coincidían con los de los bebés con la finalidad de no tener ese tipo de falsos positivos.

## English:
In particular, it can be observed that the movie data is not the only one present in the repository. This is because it was decided to preprocess the data, which can be seen in the cleaning.ipynb file.

Firstly, since the development of the filter would depend on the maximum length that could be found in the database, the movie records had extremely long lengths compared to the average. Therefore, it was decided to truncate them to a maximum length of 50 characters.

Additionally, it can be noticed that the last movie records are accompanied by (;;;;;), which were also removed.

Finally, movie names that coincided with baby names were deleted in order to avoid such false positives.

# Creación de arreglo de búsqueda
El archivo filtro.ipynb posee una función que permite dado dos datasets, un porcentaje y una cantidad "n" generar un arreglo de largo n con un porcentaje de elementos del primer dataset y el procentaje restante de n con elementos del segundo dataset. 

Esto es útil para el testeo pues podemos mezclar diferentes datas para hacer búsquedas infructuosas.


## English:
The filtro.ipynb file contains a function that, given two datasets, a percentage, and a quantity "n," generates an array of length n with a percentage of elements from the first dataset and the remaining percentage from the second dataset.

This is useful for testing as we can mix different data to perform unsuccessful searches.


# Ejecución

Existen dos archivos, main.py y main2.py el primero según la teoría itera sobre probabiliades de tener un falso positivo y en base a ello calcula el m y k óptimo. 
La variable n corresponde a el tamaño del arreglo de búsqueda que se desea utilizar.

main2.py es un archivo experimental, donde se prueba con diferentes valores de m y k para poder encontrar el óptimo y esperar que dichos ejemplares coincidan con aquellos que main.py arroja como output.

## English:
There are two files, main.py and main2.py. The former iterates over probabilities of having a false positive and calculates the optimal m and k based on that. The variable n corresponds to the size of the search array desired to be used.

main2.py is an experimental file where different values of m and k are tested to find the optimal values and see if they match those output by main.py.