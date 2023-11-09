# ScrapperLS4T
Herramientas para la extracción de corpus de LS de conferencias matutinas:
- (download.py) script para descargar los archivos desde youtube en MP4 a una resolución de 720. Este script al ejecutarlo descargará los archivos que se encuentren en la lista de reproducción de las conferencias mañaneras, del canal de gobierno de México.
- (LSS.py) script para recortar los vídeos y extraer la sección del señante. Este script identifica la sección del señante mediante el análisis de un frame, el algoritmo busca los rostros presentes de la imagen e identifica de forma morfológica la figura de un cuadrado y selecciona el que contenga un rostro dentro de sus vértices, en el script se especifica la ubicación del video (1280x720) en caso de cambiar la resolución del video, se debe introducir un frame de ese tamaño, esto para segmentar de forma correcta el vídeo. 


