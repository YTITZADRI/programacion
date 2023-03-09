operacion = ""
operacion_enlistada = []
resultado = 0
num1 = ""
num = ""
simboloprimero = ""
simbolo = ""
i = 0
def enlistar():
	global operacion_enlistada
	global operacion

	operacion = input("Escribe la operacion con los simbolos ('+','-','*','/': ): ")
	operacion_enlistada = list(operacion)

	return(operacion_enlistada)

def calcularprimero():
	global operacion_enlistada
	global resultado
	global num1
	global simboloprimero
	global i
	continuar = True
	while continuar == True:
		if operacion_enlistada[i] in "1234567890":
			num1 += operacion_enlistada[i]
			i += 1
		else:
			simboloprimero = str(operacion_enlistada[i])
			continuar = False
	return(simboloprimero,num1)

def calcular():	
	global i
	global simboloprimero
	global simbolo
	global num1
	global num
	global resultado
	resultado = num1
	simbolo = simboloprimero
	i = i+1
	continuar = True
	siguiente = False
	while continuar == True:
		if operacion_enlistada[i] != "+" and operacion_enlistada[i] != "-" and operacion_enlistada[i] != "*" and operacion_enlistada[i] != "/":
			num1 += str(operacion_enlistada[i])
			i += 1
		else:
			simbolo += str(operacion_enlistada[i])
			i += 1
			continuar = False


	if simbolo == "+":
		resultado = int(resultado)+int(num1)
	elif simbolo == "-":
		resultado = int(resultado)-int(num1)
	elif simbolo == "*":
		resultado = int(resultado)*int(num1)
	elif simbolo == "/":
		resultado = int(resultado)/int(num1)
	return(resultado)
print(enlistar())
print(calcularprimero())
print(calcular())
print(calcular())