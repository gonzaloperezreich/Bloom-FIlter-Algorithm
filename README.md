# Bloom-FIlter-Algorithm
El filtro de bloom es una herramienta que facilita la búsqueda de elementos en grandes repositorios de datos.
En este caso en particular se creó esta estructura y se sometió a la busqueda de diferentes nombres de bebés que se encuentran registrados en el archivo Popular-Baby-Names-Final.csv para evaluar su utilidad y tiempo de acción.
Claramente no solo se deberían buscar únicamente elementos de dicha base de datos sino que deberían buscarse elementos que no formaran parte de dicha base. Para esto se utilizó el archivo Film-Names.csv, el cual valga la redundancia poseía 3809 nombres de películas diferentes y serían mezcladas con la data de bebés para hacer búsquedas tanto fructuosas como infructuosas usando el filtro.

# Limpieza de datos
En particular se podrá observar que la data de peliculas no es la unica que posee el repositorio, esto se debe a que se decidió pre-procesar la data, lo cual se puede observar en limpieza.ipynb.

Esto primeramente pues parte del desarrollo del filtro dependería del largo máximo que pudiese haber en la base y el registro de peliculas poseía casos de largos extremadamente largos en comparación con el promedio. Es por ello que se decidió cortar a largo maximo 50.
Adicional a aquello, se puede observar que los últimos registros de peliculas están acompañados de (;;;;;), lo cual tambien fue eliminado. 
Finalmente se borraron los nombres de películas que coincidían con los de los bebés con la finalidad de no tener ese tipo de falsos positivos.


# Creación de arreglo de búsqueda
El archivo filtro.ipynb posee una función que permite dado dos datasets, un porcentaje y una cantidad "n" generar un arreglo de largo n con un porcentaje de elementos del primer dataset y el procentaje restante de n con elementos del segundo dataset. 

Esto es útil para el testeo pues podemos mezclar diferentes datas para hacer búsquedas infructuosas.

# Ejecución
Existen dos archivos, main.py y main2.py el primero según la teoría itera sobre probabiliades de tener un falso positivo y en base a ello calcula el m y k óptimo. 
La variable n corresponde a el tamaño del arreglo de búsqueda que se desea utilizar.

main2.py es un archivo experimental, donde se prueba con diferentes valores de m y k para poder encontrar el óptimo y esperar que dichos ejemplares coincidan con aquellos que main.py arroja como output.