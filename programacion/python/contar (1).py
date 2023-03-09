def contar():
	num1 = 52
	numerosabsolutos = 0

	intervalos = 8
	numeros = [60,52,78,73,76,54,68,62,67,64,90,92,75,83,75,70,71,73,75,80,77,71,86,65]
	end = False

	while end == False:
		maximo = num1+8
		resultado = []
		for element in numeros:
			if element > num1 and element <= maximo:
					resultado.append(element)
		frequencia = len(resultado)/len(numeros)
		porcentaje = frequencia*100
		print(resultado)
		print(len(resultado))
		numerosabsolutos += len(resultado)
		print("freqüencia relativa: "+str(frequencia))
		print("porcentaje: "+str(porcentaje))
		i = 1
		while i <= 5:
			print(" ")
			i += 1
		num1 += intervalos

		if num1 == max(numeros):
			end = True
			print("Total numeros absolutos: "+str(numerosabsolutos))
			print("Total numeros: "+str(len(numeros)))

contar()