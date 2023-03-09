import time
import time
import numpy as np
import sys
import random

#dimensiones maximas ancho: 104, alto: 47

tablero = []
col = 0
fil = 0
cantidad = 0
generacion = 0

def crearTablero():
    global tablero
    global col
    global fil
    col = int(input("Escribe el ancho: "))
    fil = int(input("Escribe el alto: "))
    tablero = np.array([[" "] * col] * fil, dtype=object)
    
    
def imprimirTablero():
    global tablero
    global col
    global fil
    al = fil-1
    an = col-1
    for i in range(len(tablero)):
        for a in range(len(tablero[i])):
            sys.stdout.write(" "+str(tablero[i][a]))
        sys.stdout.write(" "+"\n")
    
def ponerFichas(tot):
    global tablero
    global ficha
    for i in range(tot):
        i = random.randrange(0,len(tablero),1)
        a = random.randrange(0,len(tablero[0]),1)
        tablero[i][a] = ficha



def limpiar(x):
    for i in range(x):
        print("")
        
        
def modificarPosiciones():
    global tablero
    global ficha
    for i in range(len(tablero)):
        for a in range(len(tablero[i])):
            celdas = 0
            try:
                if tablero[i][a-1] == ficha or tablero[i][a-1] == "·":
                    celdas += 1
            except IndexError:
                pass
            try:    
                if tablero[i][a+1] == ficha or tablero[i][a+1] == "·":
                    celdas += 1
            except IndexError:
                pass
                
            try:
                if tablero[i+1][a] == ficha or tablero[i+1][a] == "·":
                    celdas += 1
            except IndexError:
                pass
            try:
                if tablero[i+1][a+1] == ficha or tablero[i+1][a+1] == "·":
                    celdas += 1
            except IndexError:
                pass
            try:
                if tablero[i+1][a-1] == ficha or tablero[i+1][a-1] == "·":
                    celdas += 1
            except IndexError:
                pass
                        
            try:
                if tablero[i-1][a] == ficha or tablero[i-1][a] == "·":
                    celdas += 1
            except IndexError:
                pass
            try:    
                if tablero[i-1][a+1] == ficha or tablero[i-1][a+1] == "·":
                    celdas += 1
            except IndexError:
                pass
            try:    
                if tablero[i-1][a-1] == ficha or tablero[i-1][a-1] == "·":
                    celdas += 1
            except IndexError:
                pass
                
            if tablero[i][a] == ficha:
                if celdas == 2 or celdas == 3:
                    tablero[i][a] = ficha
                if celdas > 3:
                    tablero[i][a] = "·"
                if celdas < 2:
                    tablero[i][a] = "·"
            else:
                if celdas == 3:
                    tablero[i][a] = "-"

#Nacimientos: cada celda muerta adyacente a exactamente tres vecinos vivos se convertirá en vivo en la próxima generación.
#Muerte por aislamiento: cada célula viva con uno o menos vecinos vivos morirá en la próxima generación.
#Muerte por hacinamiento: cada celda viva con cuatro o más vecinos vivos morirá en la próxima generación.
#Supervivencia: cada célula viva con dos o tres vecinos vivos permanecerá viva durante la próxima generación.


def canviar():
    global tablero
    global ficha
    
    
    for i in range(len(tablero)):
        for a in range(len(tablero[i])):
            if tablero[i][a] == "-":
                tablero[i][a] = ficha
            if tablero[i][a] == "·":
                tablero[i][a] = " "
    
            
ficha = input("Escoje un simbolo: ")  
crearTablero()
cantidad = int((col*fil)/5)
ponerFichas(cantidad)
imprimirTablero()
limpiar(1)
continuar = True
while continuar == True:
    modificarPosiciones()
    canviar()
    limpiar(40)
    print("Juego de la vida de Conway <3")
    imprimirTablero()
    print("Generacion: "+str(generacion))
    generacion += 1
    time.sleep(0.1)
    
    
    
    