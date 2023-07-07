# Bloom-FIlter-Algorithm
El filtro de bloom es una herramienta que facilita la búsqueda de elementos en grandes repositorios de datos.
En este caso en particular se creó esta estructura y se sometió a la busqueda de diferentes nombres de bebés que se encuentran registrados en el archivo Popular-Baby-Names-Final.csv para evaluar su utilidad y tiempo de acción.
Claramente no solo se deberían buscar únicamente elementos de dicha base de datos sino que deberían buscarse elementos que no formaran parte de dicha base. Para esto se utilizó el archivo Film-Names.csv, el cual valga la redundancia poseía 3809 nombres de películas diferentes y serían mezcladas con la data de bebés para hacer búsquedas tanto fructuosas como infructuosas usando el filtro.

#Limpieza de datos
En particular se podrá observar que la data de peliculas no es la unica que posee el repositorio, esto se debe a que se decidió pre-procesar la data, lo cual se puede observar en filtro.ipynb.
Esto primeramente pues parte del desarrollo del filtro dependería del largo máximo que pudiese haber en la base y el registro de peliculas poseía casos de largos extremadamente largos en comparación con el promedio. Es por ello que se decidió cortar a largo maximo 50.
Adicional a aquello, se puede observar que los últimos registros de peliculas están acompañados de (;;;;;), lo cual tambien fue eliminado. 
Finalmente se borraron los nombres de películas 

