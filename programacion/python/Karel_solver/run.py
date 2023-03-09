# Cargar OpenCV
import cv2
import sys
# Sirve para operar con cualquier dato numérico
import numpy as np


#La solucion es rescalar la imagen a un divisible de la largada de la matriz para evitar los decimales


tablero = np.array([[" "] * 18] * 19, dtype=object)
posh = len(tablero)*4
posx = (len(tablero[0])*4)-(len(tablero)*4/19)
a = 0
r = 0

# Leer las imágenes que vamos a comparar
# Imagen sobre la que vamos a detectar si existe otra imagen
img = cv2.imread('img.png')
img_rgb = cv2.resize(img,(len(tablero[0])*4,len(tablero)*4), interpolation=cv2.INTER_CUBIC)
# Imagen que comprobamos si existe en la imagen Todo
karel = cv2.imread('karel.png')

beeper = cv2.imread("beeper.png")
exit = cv2.imread("exit.png")
muro = cv2.imread("muro.png") 
suelo = cv2.imread("suelo.png") 
# Tamaño de la imagen 1.jpg
w, h = karel.shape[:-1]
 
# Función que sirve para detectar si una imagen está contenida en otra
res = cv2.matchTemplate(img_rgb, karel, cv2.TM_CCOEFF_NORMED)

# Umbral admitido
threshold = .7
 
# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
	a =	pt[0]*18/posx
	r = pt[1]*19/posh
	tablero[round(r)][round(a)] = "V"
	print("player: ","posicion_h", round(r),"posicion_x", round(a), r,a)
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 1)

# Función que sirve para detectar si una imagen está contenida en otra
w, h = beeper.shape[:-1]
res = cv2.matchTemplate(img_rgb, beeper, cv2.TM_CCOEFF_NORMED)
print(" ")
# Umbral admitido
threshold = .7
 
# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
	a =	pt[0]*18/posx
	r = pt[1]*19/posh
	tablero[round(r)][round(a)] = "C"
	print("beepers: ","posicion_h", round(r),"posicion_x", round(a), r,a)
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 1)

# Función que sirve para detectar si una imagen está contenida en otra
w, h = exit.shape[:-1]
res = cv2.matchTemplate(img_rgb, exit, cv2.TM_CCOEFF_NORMED)

# Umbral admitido
threshold = .7
print(" ")
# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
	a =	pt[0]*18/posx
	r = pt[1]*19/posh
	tablero[round(r)][round(a)] = "Z"
	print("exit: ","posicion_h", round(r),"posicion_x", round(a), r,a)
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 1)

# Función que sirve para detectar si una imagen está contenida en otra
w, h = muro.shape[:-1]
res = cv2.matchTemplate(img_rgb, muro, cv2.TM_CCOEFF_NORMED)

# Umbral admitido
threshold = .7
 
# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
loc = np.where(res >= threshold)
a = 0
c = 0
print(" ")
for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 1)
    a =	pt[0]*18/posx
    r = pt[1]*19/posh
    print("muros: ","posicion_h", round(r),"posicion_x", round(a), r,a)
    tablero[round(r)][round(a)] = "O"

# Umbral admitido
threshold = .7
res = cv2.matchTemplate(img_rgb, suelo, cv2.TM_CCOEFF_NORMED)
# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
loc = np.where(res >= threshold)
print(" ")
for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
    a =	pt[0]*18/posx
    r = pt[1]*19/posh
    tablero[round(r)][round(a)] = "S"
    print("suelos: ","posicion_h", round(r),"posicion_x", round(a), r,a)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 1)
        
def imprimir():
	global tablero
	sys.stdout.write("   ")
	sys.stdout.write("\n")
	for i in range(len(tablero)):
		for a in range(len(tablero[i])):
			sys.stdout.write(" "+str(tablero[i][a]))
		sys.stdout.write("\n")
imprimir()
# Guardar el resultado
cv2.imshow('result.png', img_rgb)
cv2.waitKey(0)




