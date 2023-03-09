import time
import random
import datetime
import math


#Menu Invertir
def menuoperacion():
	global operacionInv
	valido = False

	print("1.Invertir en una moneda")
	print("2.Retirar dinero")
	print("3.Actualizar los valores")
	print("4.Volver atras")
	print(" ")
	operacionInv = int(input("Escoje una opcion(1-4): "))

	
	if operacionInv == 1:
		invertir()
	if operacionInv == 2:
		retirarDinero()
	if operacionInv == 3:
		actualizarMonedas()
	if operacionInv == 4:
		inGame()


#Modificar Inversiones segun el valor de la criptomoneda
def modificarInversiones():
	global inversion
	global vcriptos
	global criptos
	global inversion
	global montoInversiones
	global saldo

	print(montoInversiones)
	print(vcriptos)
	print(inversion)


	i = 0
	for element in inversion:
		if element != 0:
			if montoInversiones[i] > vcriptos[i]:
				inversion[i] -= montoInversiones[i] - vcriptos[i]
	
			else:
				inversion[i] += montoInversiones[i] - vcriptos[i]
			i += 1
		else:
			i += 1
	

#Retirar Inversion
def retirarDinero():
	global inversion
	global vcriptos
	global criptos
	global inversion
	global saldo
	global montoInversiones


	i = 0
	espacios()
	print("CRIPTOMONEDAS:")
	for element in criptos:
		print(str(i+1)+"."+str(element)+": "+str(round(vcriptos[i],2))+"€")
		i += 1
	print(" ")
	i = 0
	modificarInversiones()
	print("INVERSIONES:")
	print("SALDO ACTUAL: "+str(saldo)+"€")
	for element in criptos:
		print(str(i+1)+"."+str(element)+": "+str(round(inversion[i],2))+"€")
		i += 1

	escojer = 0
	qescojer = input("Quieres retirar la inversion de alguna moneda?(y-n): ")
	if qescojer == "y":
		escojer = int(input("Escoje una moneda para retirar el dinero: "))-1
		todo = input("Quieres retirar todo el dinero?(y-n): ")
		if todo == "y":
			saldo += inversion[escojer]
			montoInversiones[escojer] = vcriptos[escojer]
			inversion[escojer] = 0
			retirarDinero()
		else:
			monto = float(input("Quanto quieres retirar?: "))
			saldo += monto
			montoInversiones[escojer] = vcriptos[escojer]
			inversion[escojer] = inversion[escojer]- monto			
			retirarDinero()
	else:
		espacios()
		menuoperacion()

#Inversion moneda
def invertir():
	global inversion
	global vcriptos
	global criptos
	global inversion
	global saldo
	global montoInversiones

	i = 0
	espacios()
	print("CRIPTOMONEDAS:")
	for element in criptos:
		print(str(i+1)+"."+str(element)+": "+str(round(vcriptos[i],2))+"€")
		i += 1
	print(" ")
	i = 0
	modificarInversiones()
	print("INVERSIONES:")
	print("SALDO ACTUAL: "+str(saldo)+"€")
	for element in criptos:
		print(str(i+1)+"."+str(element)+": "+str(round(inversion[i],2))+"€")
		i += 1
	escojer = 0
	qescojer = input("Quieres invertir en alguna moneda?(y-n): ")
	if qescojer == "y":
		escojer = int(input("Escoje una moneda para invertir: "))-1
		monto = int(input("Quanto quieres invertir?: "))
		saldo -= monto
		montoInversiones[escojer] = vcriptos[escojer]
		inversion[escojer] = monto
		modificarInversiones()
		invertir()
		
	else:
		espacios()
		menuoperacion()


#Funciones utiles/importantes

#Imprimir Monedas
def imprimirMonedas():
	global vcriptos
	global criptos
	global inversion
	i = 0
	print("CRIPTOMONEDAS:")
	for element in criptos:
		print(str(i+1)+"."+str(element)+": "+str(round(vcriptos[i],2))+"€")
		i += 1


#Actualizar Monedas
def actualizarMonedas():
	global saldo
	global criptos
	global vcriptos
	global modif
	global invertirop
	global actualizar
	global tactualizacion


	tactualizacion = int(input("Cuantos segundos quieres que pase?: "))
	modifinvertir()


#Obtener largadas monedas
def largadas():
	global vcriptos
	global modif
	modif = []
	for element in vcriptos:
	        if element >= 1:
	            modif.append(len(str(element))-1)
	        else:
	            modif.append((len(str(element))-2)*-1)


#Limpiar Pantalla
def espacios():
	i = 0
	while i <= 30:
		print(" ")
		i += 1

#Modificar Valores Criptomonedas
def modifinvertir():
	global saldo
	global criptos
	global vcriptos
	global modif
	global invertirop
	global tactualizacion


	print(" ")
	modificarInversiones()
	print("5.Actualizar Valor")
	b = 1
	while b <= tactualizacion:
		printceros = []
		i = 0
		for element in modif:
			if element >=1:
				printceros.append(random.uniform(3,-3))
				i += 1
			elif element < 1:
				sumaOresta = random.randint(1,2)
				if vcriptos[i] >= 0.1:
					printceros.append(random.uniform(1,-0.1))
				else:
					printceros.append(0)
					vcriptos[i] = 0.1
				i += 1
		a = 0
		for element in vcriptos:
			vcriptos[a] += printceros[a]
			vcriptos[a] = round(vcriptos[a],2)
			a += 1
		espacios()
		imprimirMonedas()
		largadas()
		time.sleep(1)
		b += 1
	print(" ")
	menuoperacion()

