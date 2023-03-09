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
ori = "up"
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
        sys.stdout.write("\n")
    
def ponerFicha():
    global tablero
    global ficha
    
    i = random.randrange(0,len(tablero),1)
    a = random.randrange(0,len(tablero[0]),1)
    tablero[i][a] = ficha



def limpiar(x):
    for i in range(x):
        print("")
        
        
def modificarPosiciones():
    global tablero
    global ficha
    global ori
    for i in range(len(tablero)):
        for a in range(len(tablero[i])):
            if tablero[i][a] == ficha:
                print(i,a)

    for i in range(len(tablero)):
        for a in range(len(tablero[i])):
            if ori == "up":
                if tablero[i-1][a] == " ":
                    tablero[i-1][a] = ficha


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
    
            
ficha = input("Ficha: ")  
crearTablero()
ponerFicha()
imprimirTablero()
limpiar(1)
modificarPosiciones()
continuar = True
#while continuar == True:
    #modificarPosiciones()
    #canviar()
    #limpiar(40)
    #print("Juego de la vida de Conway <3")
    #imprimirTablero()
    #print("Generacion: "+str(generacion))
    #generacion += 1
    #time.sleep(0.1)
    
    
    
    