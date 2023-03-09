import random

topic = ""
paraula = ""
paraula_correcio = []
p_encertades = []
paraula_listada = []
puntos = 0
turno = 1
imprimir = ""
letra = ""



def demanar_Paraula():
    global paraula
    global paraula_correcio
    topic = input("Player A, insert the topic of the secret panel: ")
    paraula = input("Player A, insert the secret panel: ")
    paraula_correcio = list(paraula)
    for element in paraula_correcio:
        if element != " ":
            paraula_listada.append(element)
            p_encertades.append(" ")
def imprimir():
    global paraula
    global paraula_correcio
    global p_encertades
    global paraula_listada
    global imprimir
    imprimir = ""
    i = 0
    print(paraula_correcio)
    print(p_encertades)
    print(paraula_listada)
    while i < len(p_encertades):
        if paraula_correcio[i] == p_encertades[i]:
            imprimir += str(paraula_correcio[i])
        else:
            if paraula_correcio[i] == " ":
                imprimir += " "
            else:
                imprimir += "_"
        i += 1
    print(imprimir)    
    
def detectar():
    global paraula
    global paraula_correcio
    global p_encertades
    global paraula_listada
    global puntos
    global turno
    global imprimir
    global letra



    puntos = random.randint(0,5)
    solve = ""
    if turno%2 != 0:
        print("Turn of player A")
        print("The play is worth "+str(puntos))
        print("The secret panel is: "+str(imprimir))
        es_valido = False
        while es_valido == False:
                solve = input("Want to solve the panel? (Y/N): ")
                if solve == "Y" or solve == "N":
                    es_valido = True
        if solve == "N":
            letra = input("Insert letter: ")
            i = 0
            for element in paraula_correcio:
                if element == letra:
                    p_encertades[i] == element
                    i += 1
                else:
                    i += 1







def limpiar():
    a = 0
    while a < 40:
        print(" ")
        a += 1


print("Welcome to the game of the Wheel Of Fortune")
demanar_Paraula()
limpiar()
imprimir()
detectar()
imprimir()