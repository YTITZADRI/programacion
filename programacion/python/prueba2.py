import random

num1 = 0
num2 = 0
simbolo = ""
respuestaJugador = 0
respuesta = 0
errores = 0
aciertos = 0
operaciones = 1


def generarNum():
	global num1
	global num2
	global simbolo
	global respuestaJugador
	global respuesta
	i = random.randint(1,4)

	if i == 1:
		simbolo = "+"
	elif i == 2:
		simbolo = "-"
	elif i == 3:
		simbolo = "*"


	if simbolo == "+" or simbolo == "-":
		num1 = random.randint(1,1000)
		num2 = random.randint(1,1000)
	if simbolo == "*":
		num1 = random.randint(1,10)
		num2 = random.randint(1,10)

	if simbolo == "+":
		respuesta = num1+num2
		print(str(num1)+"+"+str(num2))
	if simbolo == "-":
		respuesta = num1-num2
		print(str(num1)+"-"+str(num2))
	if simbolo == "*":
		respuesta = num1*num2
		print(str(num1)+"*"+str(num2))


def calcular():
	global num1
	global num2
	global simbolo
	global respuesta
	global respuestaJugador
	global errores
	global aciertos

	es_correcto = False

	while es_correcto == False:
		respuestaJugador = int(input("Escribe tu respuesta: "))
		if respuestaJugador == respuesta:
			es_correcto = True
			aciertos += 1
		if respuestaJugador != respuesta:
			errores += 1


while operaciones <= 10:
	generarNum()
	calcular()
	operaciones += 1

print("aciertos: "+str(aciertos))
print("errores: "+str(errores))