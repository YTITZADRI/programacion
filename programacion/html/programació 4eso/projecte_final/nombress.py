import os


html = open('/home/cabreraluqueadria/programacion/html/programació 4eso/projecte_final/html.txt', 'w')
archivo = "/home/cabreraluqueadria/programacion/html/programació 4eso/projecte_final/habilidades.txt"

tipos = {"normal":"Normal","poison":"Veneno","grass":"Hierba","fire":"Fuego","rock":"Roca","steel":"Metal","flying":"Volador","water":"Agua","bug":"Bicho","electric":"Electrico","ground": "Tierra","fairy":"Hada","fighting": "Lucha","dark":"Oscuro","ice":"Hielo","psychic":"Psíquico"}
matriz = []
with open(archivo, 'r') as file:
    for line in file:
    	elemento = line.split("-")
    	cadena = ""
    	tipo = elemento[2].split(" ")
    	for element in tipo:
    		for b in tipos.items():
    			if element == b[0]:
    				cadena += b[1]+" "
    	elemento[2] = cadena
    	matriz.append(elemento)


matriz_ordenada = []
i = 1
for element in matriz:
	
	for b in range(len(matriz)):
		try:

			if i == int(matriz[b][1]):
				lista = []
				for c in range(len(element)):
					parte = ""	
					if c >= 3:
						try:
							m = element[c].split(":")
							parte = m[1]
						except IndexError:
							pass
					else:
						try:
							parte = element[c]
						except IndexError:
							pass
					lista.append(parte)
				matriz_ordenada.append(lista)
		except ValueError:
			pass
	i += 1

for element in matriz_ordenada:
	print(element)
# Imprimir los archivos ordenados
for a in range(len(matriz_ordenada)):
	with open("/home/cabreraluqueadria/programacion/html/programació 4eso/projecte_final/html.txt", 'a') as html:
		try:
			html.write("<tr>\n")
			html.write("<td>"+"<img src='lista_pokemons/"+str(matriz_ordenada[a][0])+".png'></td>\n")
			html.write("<td>"+matriz_ordenada[a][0]+"<br> nº"+matriz_ordenada[a][1]+"<br>\n")
			html.write(matriz_ordenada[a][2]+"</td>\n")
			html.write("<td>"+matriz_ordenada[a][3]+"</td>\n")
			html.write("<td>"+matriz_ordenada[a][4]+"</td>\n")
			html.write("<td>"+matriz_ordenada[a][5]+"</td>\n")
			html.write("<td>"+matriz_ordenada[a][7]+"</td>\n")
			html.write("<td>"+matriz_ordenada[a][9]+"</td>\n")


			html.write("<td>"+matriz_ordenada[a][10]+"</td>\n")
			html.write("</tr>\n")
		except IndexError:
			pass
