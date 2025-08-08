# ACLARACIÓN IMPORTANTE, el archivo .jpg debe estar en el mismo directorio (carpeta) en donde está el archivo .py


import cv2
import numpy as np
import os

# Mostrar la ruta desde donde se ejecuta el script
print("Ruta actual:", os.getcwd())

# Nombre de la imagen (asegurate de que esté en la misma carpeta que este archivo .py)
ruta_imagen = 'Carti.jpg'  # Cambia esto si la imagen tiene otro nombre o extensión

# Intentar cargar la imagen
imagen = cv2.imread(ruta_imagen)

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print(f"No se pudo cargar la imagen '{ruta_imagen}'. Verifica que el archivo exista en la ruta mostrada arriba.")
    exit()

# Redimensionar imagen para visualización más manejable
imagen = cv2.resize(imagen, (600, 400))

# -------------------- FILTROS --------------------

# 1. Desenfoque promedio (Blur)
blur = cv2.blur(imagen, (5, 5))

# 2. Desenfoque Gaussiano
gauss = cv2.GaussianBlur(imagen, (5, 5), 0)

# 3. Desenfoque por mediana
mediana = cv2.medianBlur(imagen, 5)

# 4. Detección de bordes Canny
canny = cv2.Canny(imagen, 100, 200)

# 5. Filtro bilateral (suaviza sin perder bordes)
bilateral = cv2.bilateralFilter(imagen, 9, 75, 75)

# 6. Filtro personalizado (detección de bordes horizontal)
kernel = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])
filtro_personalizado = cv2.filter2D(imagen, -1, kernel)

# -------------------- MOSTRAR RESULTADOS --------------------

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Desenfoque Promedio (Blur)', blur)
cv2.imshow('Desenfoque Gaussiano', gauss)
cv2.imshow('Desenfoque Mediana', mediana)
cv2.imshow('Detección de Bordes (Canny)', canny)
cv2.imshow('Filtro Bilateral', bilateral)
cv2.imshow('Filtro Personalizado (Convolución)', filtro_personalizado)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
