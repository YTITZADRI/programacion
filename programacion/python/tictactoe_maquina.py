import random
import sys
import numpy as np 


playerFicha = ""
compFicha = ""
posPlayer = 0
posComp = 0
row = 0
col = 0
siz = 0
tablero = []
turno = 0
win = False
playerWin = 0
colinp = 0
rowinp = 0
win2 = ""
listaplayer = []
listacompt = []
numJugadores = 0
nombreJugador = ""
nombreJugador2 = ""
turno1 = 0
win1 = 0
win2 = 0


def jugadores():
	global numJugadores
	global nombreJugador
	global nombreJugador2
	print("ESCOJE UNA DE LAS SIGUIENTES OPCIONES:")
	print("1. JUGADOR VS MAQUINA")
	print("2. JUGADOR VS JUGADOR")

	es_valido = False
	while es_valido == False:
		opcion = int(input("ESCOJE UNA OPCION (1-2): "))
		if opcion == 1 or opcion == 2:
			es_valido = True
	if opcion == 1:
		numJugadores = 1
		nombreJugador = input("Como te quieres llamar Jugador 1?: ")
		nombreJugador2 = input("Como quieres llamar a la maquina?: ")
	else:
		numJugadores = 2
		nombreJugador = input("Como te quieres llamar Jugador 1?: ")
		nombreJugador2 = input("Como te quieres llamar Jugador 2?: ")
def limpiar():
	a = 0
	while a <= 50:
		print(" ")
		a += 1

def primerTurno():
	global turno1
	global turno
	global nombreJugador
	global nombreJugador2

	i = random.randint(0,1)

	if i == 0:
		turno = 0
		print("Empieza "+nombreJugador)

	else:
		turno = 1
		print("Empieza "+nombreJugador2)



def ficha():
	global playerFicha
	global compFicha
	global turno
	global nombreJugador
	global nombreJugador2
	es_valido = False
	if turno == 0:
		while es_valido == False:
			if playerFicha != "x" or playerFicha != "o":
				playerFicha = input("Escoje una ficha "+nombreJugador+"(x - o): ")
			else:
				es_valido = True

			if playerFicha == "x" or playerFicha == "o":
				if playerFicha == "x":
					compFicha = "o"
					print("Ficha "+nombreJugador+": "+playerFicha)
					print("Ficha "+nombreJugador2+": "+compFicha)
				else:
					compFicha = "x"
					print("Ficha "+nombreJugador+": "+playerFicha)
					print("Ficha "+nombreJugador2+": "+compFicha)
				es_valido = True
	else:
		while es_valido == False:
			if compFicha != "x" or compFicha != "o":
				compFicha = input("Escoje una ficha "+nombreJugador2+"(x - o): ")
			else:
				es_valido = True
			if compFicha == "x" or compFicha == "o":
				if compFicha == "x":
					playerFicha = "o"
					print("Ficha "+nombreJugador2+": "+compFicha)
					print("Ficha "+nombreJugador+": "+playerFicha)
				else:
					playerFicha = "x"
					print("Ficha "+nombreJugador2+": "+compFicha)
					print("Ficha "+nombreJugador+": "+playerFicha)
				es_valido = True

def size():
	global row
	global col
	global siz
	global tablero
	global rowinp
	global colinp
	es_valido = False

	while es_valido == False:
		print("Los dos valores deben ser iguales")
		row = int(input("Escoje el alto: "))
		col = int(input("Escoje el ancho: "))

		if row == col:
			print("Has elejido un tablero de "+str(row)+"x"+str(col))
			es_valido = True
		else:
			print("Debes elejir en los dos campos el mismo numero")

	tablero = np.array([[" "] * col] * row, dtype=object)
	print(tablero)
	

def imprimir():
	global row
	global col
	global siz
	global tablero
	i = 0
	b = 0
	a = 0
	while i < col:
		while a < col:
			sys.stdout.write("|"+str(tablero[b][a]))
			a += 1
		sys.stdout.write("|\n")
		b += 1
		i += 1
		a = 0




def escribir():
	global playerFicha
	global compFicha
	global posComp
	global posPlayer
	global turno
	global win
	global playerWin
	global colinp
	global rowinp
	global col
	global row
	global tablero
	global numJugadores
	global nombreJugador
	global nombreJugador2
	colinp = 0
	rowinp = 0
	es_valido = False
	if turno%2 == 0:
		while es_valido == False:
				print("Turno de "+nombreJugador)
				colinp = random.randint(0,col-1)
				rowinp = random.randint(0,row-1)
				if tablero[rowinp][colinp] == " ":
					tablero[rowinp][colinp] = playerFicha
					es_valido = True
				else:
					print("La casilla esta ocupada")
					colinp = random.randint(0,col-1)
					rowinp = random.randint(0,row-1)
	else:
		while es_valido == False:
				print("Turno de "+nombreJugador2)
				colinp = random.randint(0,col-1)
				rowinp = random.randint(0,row-1)
				if tablero[rowinp][colinp] == " ":
					tablero[rowinp][colinp] = compFicha
					es_valido = True
				else:
					print("La casilla esta ocupada")
					colinp = random.randint(0,col-1)
					rowinp = random.randint(0,row-1)
		



def ganar():
	global tablero
	global win
	global col
	global win2
	global compFicha
	global playerFicha
	global listaplayer
	global listacompt
	listaplayer = []
	listacompt = []
	i = 0
	a = 0
	valido = False
	while a < col:
		while i < col:
			if tablero[a][i] == playerFicha:
				valido = True
				listaplayer.append(1)
				i += 1
			else:
				listaplayer.append(0)
				valido = False
				i += 1
		a += 1
		i = 0
	i = 0
	a = 0
	valido = False
	while i < col:
		while a < col:
			if tablero[a][i] == playerFicha:
				valido = True
				listaplayer.append(1)
				a += 1
			else:
				valido = False
				listaplayer.append(0)
				a += 1
		a = 0
		i += 1

	i = 0
	a = 0
	valido = False
	while a < col:
		if tablero[a][i] == playerFicha:
			valido = True
			listaplayer.append(1)
			a += 1
			i += 1
		else:
			valido = False
			listaplayer.append(0)
			a += 1
			i += 1
	i = col-1
	a = 0
	while i >= 0:
		if tablero[a][i] == playerFicha:
			valido = True
			listaplayer.append(1)
			a += 1
			i -= 1
		else:
			valido = False
			listaplayer.append(0)
			a += 1
			i -= 1
	c = 0
	while c <= 5:
		c += 1


	i = 0
	a = 0
	valido = False
	while a < col:
		while i < col:
			if tablero[a][i] == compFicha:
				valido = True
				listacompt.append(1)
				i += 1
			else:
				listacompt.append(0)
				valido = False
				i += 1
		a += 1
		i = 0
	i = 0
	a = 0
	valido = False
	while i < col:
		while a < col:
			if tablero[a][i] == compFicha:
				valido = True
				listacompt.append(1)
				a += 1
			else:
				valido = False
				listacompt.append(0)
				a += 1
		a = 0
		i += 1

	i = 0
	a = 0
	valido = False
	while a < col:
		if tablero[a][i] == compFicha:
			valido = True
			listacompt.append(1)
			a += 1
			i += 1
		else:
			valido = False
			listacompt.append(0)
			a += 1
			i += 1
	i = col-1
	a = 0
	while i >= 0:
		if tablero[a][i] == compFicha:
			valido = True
			listacompt.append(1)
			a += 1
			i -= 1
		else:
			valido = False
			listacompt.append(0)
			a += 1
			i -= 1


def detectarwin():

	global listaplayer
	global listacompt
	global nombreJugador
	global nombreJugador2
	global win
	global win1
	global win2
	i = 0
	fichasPlayer = 0
	while i < len(listaplayer):
		a = 0
		while a < col:
			if listaplayer[i] == 1:
				fichasPlayer += 1
				i += 1
				a += 1
			else:
				fichasPlayer = 0
				i += 1
				a += 1
		if fichasPlayer >= col:
				limpiar()
				imprimir()
				win = True
				win1 += 1
				return("Gana "+nombreJugador)
		else:
			fichasPlayer = 0


	n = 0
	fichasComputadora = 0
	while n < len(listacompt):
		x = 0
		while x < col:
			if listacompt[n] == 1:
				fichasComputadora += 1
				n += 1
				x += 1
			else:
				fichasComputadora = 0
				n += 1
				x += 1
		if fichasComputadora >= col:
				limpiar()
				imprimir()
				win = True
				win2 += 1
				return("Gana "+nombreJugador2)
		else:
			fichasComputadora = 0
	return(" ")

def detectarempate():
	global tablero
	global win

	empate = True
	b = np.array(tablero)
	c = np.array([" "])
	result = np.equal(b,c)
	result2 = result.any()
	return(result2)

jugadores()
primerTurno()
ficha()
size()
limpiar()
while win == False:
	limpiar()
	imprimir()
	escribir()
	ganar()
	print(detectarwin())
	print(detectarempate())
	turno += 1

opcion = ""

volver = False
valido = False
while valido == False:
	opcion =input("Quieres volver a jugar? (y-n): ")
	if opcion == "y" or opcion == "n":
		valido = True
	while opcion == "y":
		volver = True
		posPlayer = 0
		posComp = 0
		tablero = []
		turno = 0
		win = False
		playerWin = 0
		colinp = 0
		rowinp = 0
		win2 = ""
		listaplayer = []
		listacompt = []
		numJugadores = 0
		turno1 = 0
		size()
		limpiar()
		while win == False:
			limpiar()
			imprimir()
			escribir()
			ganar()
			print(detectarwin())
			print(detectarempate())
			if detectarempate() == False:
				limpiar()
				imprimir()
				print("EMPATE")
				win = True
			turno += 1
		volver = False
		valido = False
	if opcion == "n":
		limpriar()
		print(nombreJugador+" Ha ganado "+str(win1)+" veces")
		print(nombreJugador2+" Ha ganado "+str(win2)+" veces")
