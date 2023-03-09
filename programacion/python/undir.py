import random
import numpy as np
import sys
tableroJugador = []
win = False
posicionEleccion = 0



def crearTableroPlayer():

	global tableroJugador

	tableroJugador = np.array([["-"] * 8] * 8, dtype=object)



def imprimir():

	global tableroJugador
	print(tableroJugador)
	i = 0
	letras = ["1","2","3","4","5","6","7","8"]
	sys.stdout.write("  ")
	while i < len(letras):
		sys.stdout.write(letras[i]+" ")
		i += 1
	sys.stdout.write("\n")

	numeros = [1,2,3,4,5,6,7,8]
	a = 0
	b = 0
	while b < len(letras):
		sys.stdout.write(letras[b])
		a = 0
		sys.stdout.write(" ")
		while a < len(letras):
			sys.stdout.write(tableroJugador[b][a])
			sys.stdout.write(" ")
			a += 1
		sys.stdout.write("\n")
		b += 1

def limpiar():
	i = 0
	while i <= 20:
		print(" ")
		i += 1


def generarMinas():

	global tableroJugador
	i = 0
	a = 0
	lenfila = len(tableroJugador[0])
	while i < lenfila:
		posicionRandom = random.randint(0,lenfila)

		tableroJugador[i][posicionRandom] = "X"
		i += 1

def generarNumeros():
	global tableroJugador

	i = 0
	a = 0
	bomba = False
	b = 0
	while b <= 9:
		if 


def escojer():
	global tableroJugador
	global posicionEleccion

	es_valido = False
	while es_valido == False:
		fil = int(input("Escoje la fila: "))
		col = int(input("Escoje la columna: "))
		if tableroJugador[fil][col] == "-":
			es_valido = True



crearTableroPlayer()
generarMinas()
imprimir()