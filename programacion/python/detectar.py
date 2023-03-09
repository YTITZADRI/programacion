def vocales(x):
	i = x.split(" ")
	frase = []
	for element in i:
		m = list(element)
		c = ""
		for a in range(len(m)):
			if m[a] != "," and m[a] != ".":
				c += m[a]
		frase.append(c)

	print(frase)
	for i in range(len(frase)):
		a = list(frase[i-1])
		m = list(frase[i])
		f = a[len(a)-1]
		g = m[0]
		if f in ["a","e","i","o","u"] and g in ["a","e","i","o","u"]:
			print(frase[i-1]+"-"+frase[i])

f = input("> ")
print(vocales(f))