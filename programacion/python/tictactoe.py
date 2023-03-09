import random
tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
fichaJugador = ""
fichaComputadora = ""
posJugador = 0
posComputadora = 0
turno = 0
end = False
win = 0


def escojerFicha():
    global fichaJugador
    global fichaComputadora

    es_valido = False
    while es_valido == False:
        fichaJugador = input("Escoje una ficha (X-0): ")
        if fichaJugador == "X" or fichaJugador == "0":
            if fichaJugador == "X":
                fichaComputadora = "0"
            else:
                fichaComputadora = "X"
            es_valido = True


def imprimirTablero():
    global tablero

    i = 0
    a = 0

    print("|"+tablero[0][0]+"|"+tablero[0][1]+"|"+tablero[0][2]+"|")
    print("|"+tablero[1][0]+"|"+tablero[1][1]+"|"+tablero[1][2]+"|")   
    print("|"+tablero[2][0]+"|"+tablero[2][1]+"|"+tablero[2][2]+"|")

def ponerFicha():
    global tablero
    global fichaJugador
    global fichaComputadora
    global turno


    fila = 0
    columna = 0



    if turno == 0:
        es_valido_fila = False
        es_valido_columna = False
        while es_valido_fila == False:
            fila = int(input("Escoje una fila (1-3): "))
            if fila >= 1 and fila <= 3:
                es_valido_fila = True
        while es_valido_columna == False:
            columna = int(input("Escoje una columna (1-3): "))
            if columna >= 1 and columna <= 3:
                es_valido_columna = True
        tablero[fila-1][columna-1] = fichaJugador
    if turno == 1:
        es_valido = False
        while es_valido == False:
            fila = random.randint(0,2)
            columna = random.randint(0,2)
            if tablero[fila][columna] == " ":
                es_valido = True
        tablero[fila][columna] = fichaComputadora

def ganar():
    global tablero
    global end
    global win


    
    if tablero[0][0] == fichaJugador and tablero[0][1] == fichaJugador and tablero[0][2] == fichaJugador:
        end = True
        win = 0
    if tablero[1][0] == fichaJugador and tablero[1][1] == fichaJugador and tablero[1][2] == fichaJugador:
        end = True
        win = 0
    if tablero[2][0] == fichaJugador and tablero[2][1] == fichaJugador and tablero[2][2] == fichaJugador:
        end = True
        win = 0
    
    
    if tablero[0][1] == fichaJugador and tablero[1][1] == fichaJugador and tablero[2][1] == fichaJugador:
        end = True
        win = 0
    if tablero[0][0] == fichaJugador and tablero[1][0] == fichaJugador and tablero[2][0] == fichaJugador:
        end = True
        win = 0
    if tablero[0][2] == fichaJugador and tablero[1][2] == fichaJugador and tablero[2][2] == fichaJugador:
        end = True
        win = 0
    

    if tablero[0][0] == fichaJugador and tablero[1][1] == fichaJugador and tablero[2][2] == fichaJugador:
        end = True
        win = 0
    if tablero[0][2] == fichaJugador and tablero[1][1] == fichaJugador and tablero[2][0] == fichaJugador:
        end = True
        win = 0





    if tablero[0][0] == fichaComputadora and tablero[0][1] == fichaComputadora and tablero[0][2] == fichaComputadora:
        end = True
        win = 1
    if tablero[1][0] == fichaComputadora and tablero[1][1] == fichaComputadora and tablero[1][2] == fichaComputadora:
        end = True
        win = 1
    if tablero[2][0] == fichaComputadora and tablero[2][1] == fichaComputadora and tablero[2][2] == fichaComputadora:
        end = True
        win = 1
    
    
    if tablero[0][1] == fichaComputadora and tablero[1][1] == fichaComputadora and tablero[2][1] == fichaComputadora:
        end = True
        win = 1
    if tablero[0][0] == fichaComputadora and tablero[1][0] == fichaComputadora and tablero[2][0] == fichaComputadora:
        end = True
        win = 1
    if tablero[0][2] == fichaComputadora and tablero[1][2] == fichaComputadora and tablero[2][2] == fichaComputadora:
        end = True
        win = 1
    

    if tablero[0][0] == fichaComputadora and tablero[1][1] == fichaComputadora and tablero[2][2] == fichaComputadora:
        end = True
        win = 1
    if tablero[0][2] == fichaComputadora and tablero[1][1] == fichaComputadora and tablero[2][0] == fichaComputadora:
        end = True
        win = 1



def limpiar():
    i = 0
    while i <= 50:
        print(" ")
        i += 1



escojerFicha()
while end == False:
    limpiar()
    imprimirTablero()
    ponerFicha()
    ganar()
    if turno == 1:
        turno = 0
    else:
        turno = 1
if win == 0:
    limpiar()
    imprimirTablero()
    print("Ha ganado el JUGADOR :D")
else:
    limpiar()
    imprimirTablero()
    print("Ha ganado la maquina :c")