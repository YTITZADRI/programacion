import os
import requests
import json
import sys
url_img = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/"
url = "http://pokeapi.co/api/v2/pokemon/"
habilidades = open("habilidades.txt", "w")

for i in range(1,891):
	c = ""
	if i < 10:
		c = "00"+str(i)
	if i < 100 and i >= 10:
		c = "0"+str(i)
	if i > 100:
		c = str(i)
	#os.system("wget "+url_img+c+".png")
	peticion = requests.get(url+str(i))
	respuesta = json.loads(peticion.content)
	tipos = ""
	try:
		tipo = respuesta["types"][0]["type"]["name"]
		tipos += tipo
	except IndexError:
		pass

	try:
		tipo = respuesta["types"][1]["type"]["name"]
		tipos += " "+tipo
	except IndexError:
		pass
	nombre = respuesta["name"]
	idd = respuesta["id"]
	stats = respuesta["stats"]

	with open("habilidades.txt","a") as contenido:
		contenido.write(nombre+"-"+str(idd)+"-"+tipos)
		for stat in stats:
			contenido.write(f"-{stat['stat']['name']}:{stat['base_stat']}")
		contenido.write("\n")
	#os.system("mv "+c+".png "+nombre+".png")
	#os.system("rm "+c+".png.1")
	#os.system("clear")
	sys.stdout.write(nombre+"-"+str(idd)+"-"+tipos+"\n")
	for stat in stats:
			sys.stdout.write(f"-{stat['stat']['name']}:{stat['base_stat']}\n")
	print(" ")
	print(" ")