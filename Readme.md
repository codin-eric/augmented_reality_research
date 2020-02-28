# Realidad Aumentada - Re encontrar el amor por álgebra con Python

Esta es la investigación de la charla dada en el meetup de PyAr "ChoriPython".<br>
Basado fuertemente en el blogpost "Augmented reality with Python and OpenCV" de Bites of Code<br>
https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/
<br>

# Contenido.
En el notebook [marked](notebooks/marked.ipynb) vas a encontrar todo el código que utilicé para la parte de marked AR<br>
En el notebook [render](notebooks/render.ipynb) vas a encontrar todo el cóigo que utilicé para la parte de crear tu propio motor de render

# Investigación
## Marked AR vs Markerless AR
- Marked AR se basa en una imagen de referencia para encontrar en un stream de video

![Alt text](img/aruco.jpg?raw=true "Aruco markers")

- Markerless AR utiliza algoritmos de Machine Learning para poder identificar modelos en el stream de video
![Alt text](img/hand.jpg?raw=true "Aruco markers" )
<br>
## Marked AR
Los pasos a seguir para poder realizar Marked AR son:
- Crear una referencia
- Encontrar nuestra referencia en el stream de video
- Identificar su posición y orientación en el espacio
- Rotrotransladar un objeto virtual a la posición
## Crear una referencia
Empecé creando un aruco marker en un post-it<br>
![Alt text](img/aruco_marker.jpg?raw=true "Aruco markers")
<br>
Opté por utilizar ORB (Oriented FAST and Rotated BRIEF) ya que los otros populares, SIFT y SURF son algoritmos con copyrights<br>
Al correr ORB detection en ambas imagenes conseguimos los key points que debemos localizar
![Alt text](img/aruco_marked.png?raw=true "Aruco markers")
![Alt text](img/stream_key_points.png?raw=true "Aruco markers")
<br>
Luego para identificar cada uno de los keypoints de la referencia en el stream de video utilizo Brute-force descriptor matcher. Esto da como resultado el siguiente set de matches. Lo que se puede ver es que de un set de 100 matches hay muchisimos falsos positivos.

![Alt text](img/aruco_referenced.png?raw=true "Aruco markers")
<br>
Al cambiar la referencia podemos ver que de 100 matches solo 3 son falsos positivos
![Alt text](img/saint_referenced.png?raw=true "Aruco markers")
<br>
Una vez que tenemos la referencia de cada punto podemos calcular como fue que se movieron, esto se logra con algo llamado la matriz homografica
![Alt text](img/homograpy_matrix.png?raw=true "Aruco markers")

Si aplicamos esta matriz a cualquier plano 2D obtendremos la posición que debera tener en referencia a la imagen que estamos buscando. Por lo tanto obtendremos lo siguiente.
<br>
![Alt text](img/final_result.png?raw=true "Aruco markers")

## Renderizar cualquier objeto de blender en nuestro proyecto.
Esta parte del proyecto esta altamente basada en la serie de videos "Code-It-Yourself! 3D Graphics Engine" de javidx9<br>

[![Code-It-Yourself! 3D Graphics Engine](https://www.youtube.com/watch?v=ih20l3pJoeU)]

## Todo
- [ ] Poner mas lindas las imágenes
- [ ] Implementar el motor de render a la lógica de AR
- [ ] Implementar una lógica de markerless AR