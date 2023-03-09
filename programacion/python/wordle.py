palabra = []
palabras_encertadas = []
palabra_imprimir = ""
def elegirPalabra():
	global palabra

	es_valido = False
	i = 0
	while es_valido == False:
		palabra = list(input("Escribe la palabra en minusculas: "))
		i = 0
		for element in palabra:
			if element in "qwertyuiopasdfghjklñzxcvbnm":
				i += 1
		if i == len(palabra):
			es_valido = True
		else:
			print("La palabra contiene mayusculas")
	return(palabra)

def generarPalabra():
	global palabra
	global palabras_encertadas

	i = 0
	while i < len(palabra):
		palabras_encertadas.append("")
		i += 1
	return(palabras_encertadas)

def esconderPalabra():
	global palabra
	global palabras_encertadas
	global palabra_imprimir
	i = 0
	palabra_imprimir = ""
	while i < len(palabra):
		if palabras_encertadas[i] == palabra[i]:
			palabra_imprimir += str(palabra[i])
			i += 1
		else:
			palabra_imprimir += "_"
			i += 1

	return(palabra_imprimir)


def escojerPalabra():
	global palabra
	global palabras_encertadas
	global palabra_imprimir

	es_valido = False
	i = 0
	while es_valido == False:
		palabra_escojida = input("Escribe una letra en minusculas: ")
		if palabra_escojida in "qwertyuiopasdfghjklñzxcvbnm":			
				es_valido = True
		else:
			print("La letra no es valida")
	esta = False
	for element in palabra:
		if element == palabra_escojida:
			palabras_encertadas[i] = palabra_escojida
			esta = True
			i += 1
		else:
			esta = False
			i += 1
	if esta == False:
		print("La letra '"+str(palabra_escojida)+"' no esta en la palabra")
	return(palabra_escojida)

def borrarPalabra():
	i = 0
	while i <= 50:
		print(" ")
		i += 1


print(elegirPalabra())
print(generarPalabra())
borrarPalabra()
win = False
while win == False:
	print(esconderPalabra())
	print(escojerPalabra())
	if palabras_encertadas == palabra:
		win = True
print(esconderPalabra())
print("Has ganado")