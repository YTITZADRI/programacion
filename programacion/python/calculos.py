import math



opcion = 0
result_sum = 0
result_rest = 0
result_mult = 0
result_div = 0
result_m2 = 0
result_area = 0
result_m2 = 0
result_vol = 0
result_area = 0
def menu():
	global opcion

	print("MENU:")
	print("1.Suma")
	print("2.Resta")
	print("3.Multiplicacion")
	print("4.Division")
	print("5.Calcular m2")
	print("6.Volumen Cuerpo")
	print("7.Area figura")
	print("8.Exit")
	print(" ")
	ultimo = 8
	es_valido = False
	
	while es_valido == False:
		opcion = int(input("Escoje una opcion(1-"+str(ultimo)+"): "))
		if opcion >= 1 and opcion <= 8:
			es_valido == True
			break
		else:
			print("Escoje un numero correcto")


def sum():
	global result_sum
	num1 = int(input("Escoje el primer numero: "))
	num2 = int(input("Escoje el segundo numero: "))
	result_sum = num1+num2
	return(str(num1)+" + "+str(num2)+" = "+str(result_sum))
def rest():
	global result_rest
	num1 = int(input("Escoje el primer numero: "))
	num2 = int(input("Escoje el segundo numero: "))
	result_sum = num1-num2
	return(str(num1)+" - "+str(num2)+" = "+str(result_sum))
def div():
	global result_div
	num1 = int(input("Escoje el primer numero: "))
	num2 = int(input("Escoje el segundo numero: "))
	result_sum = num1/num2
	return(str(num1)+" / "+str(num2)+" = "+str(result_sum))
def mult():
	global result_mult
	num1 = int(input("Escoje el primer numero: "))
	num2 = int(input("Escoje el segundo numero: "))
	result_sum = num1*num2
	return(str(num1)+" x "+str(num2)+" = "+str(result_sum))

def m2():
	global result_m2
	num1 = int(input("Largada: "))
	num2 = int(input("Anchura: "))
	result_m2 = num1*num2
	return(str(num1)+" x "+str(num2)+" = "+str(result_m2)+"m2")

def vol():
	global result_vol
	pi = math.pi
	num1 = int(input("Ancho: "))
	num2 = int(input("Largo: "))
	num3 = int(input("Altura: "))
	result_sum = num1*num2*num3
	return(str(num1)+" x "+str(num2)+" x "+str(num3)+" = "+str(result_sum)+"m3")
def area():
	global result_area
	num1 = int(input("Ancho: "))
	num2 = int(input("Largo: "))
	return(str(num1)+" x "+str(num2)+" = "+str(result_area)+"m2")


end = False
while end == False:
	menu()
	if opcion == 1:
		print(sum())
	if opcion == 2:
		print(rest())
	if opcion == 3:
		print(mult())
	if opcion == 4:
		print(div())
	if opcion == 5:
		print(m2())
	if opcion == 6:
		print(vol())
	if opcion == 7:
		print(area())
	if opcion == 8:
		end = True

