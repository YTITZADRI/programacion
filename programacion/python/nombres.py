import os

path = '/home/cabreraluqueadria/programacion/html/programació 4eso/projecte_final/Pokedex/pokemons'
archivos = os.listdir(path)


archivos_ordenados = sorted(archivos)
pos = 0
suma = 50
print(list(archivos_ordenados))

html = open('/home/cabreraluqueadria/programacion/html/programació 4eso/projecte_final/html.txt', 'w')
archivo = "/home/cabreraluqueadria/programacion/html/programació 4eso/projecte_final/MP1/pokemon.txt"
archivos = {}
with open(archivo, 'r') as file:
    for line in file:
    	elemento = line.split(",")
    	
    	if elemento[0] != "#":
    		archivos[elemento[0]] = elemento[1]
print(archivos)

sorted_d = dict(sorted(archivos.items(), key=lambda x: int(x[0])))
nombres = []

for element in sorted_d:
	nombres.append(sorted_d[element])
print("")
print(nombres)
# Imprimir los archivos ordenados
a = 1
for i in range(len(archivos_ordenados)):
	with open("/home/cabreraluqueadria/programacion/html/programació 4eso/projecte_final/html.txt", 'a') as html:
		try:	
			if a == 1:
				html.write("<tr>\n")
				html.write("<td>\n")
				html.write("<figure>\n")
				html.write("    <img src='Pokedex/pokemons/"+str(i+1)+".png'>\n")
				html.write("    <figcaption>"+str(i+1)+"</figcaption>\n")
				html.write("</figure>\n")
				html.write("</td>\n")
			else:
				html.write("<td>\n")
				html.write("<figure>\n")
				html.write("    <img src='Pokedex/pokemons/"+str(i+1)+".png'>\n")
				html.write("    <figcaption>"+str(i+1)+"</figcaption>\n")
				html.write("</figure>\n")
				html.write("</td>\n")
			if a >= 3:
				html.write("</tr>\n")
				a = 0
			a += 1
		except IndexError:
			html.write("</figure>\n")
			html.write("</tr>\n")
			break

print(" ")
print(len(nombres))