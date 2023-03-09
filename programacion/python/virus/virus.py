import os
carpetas = []
b = 0
for i in range(1000):
    os.system("mkdir a"+str(i))
    b += 1
    for a in range(1000):
        os.system("mkdir a"+str(i)+"/a"+str(a))
        ruta = "a"+str(i)+"/a"+str(a)+".txt"
        filename = "a"+str(a)
        with open(ruta, "w") as filename:
            for i in range(1000):
                filename.write(str(i))
        b += 1
        print("a"+str(i)+"/a"+str(a), "carpetas creadas: "+str(b))
    
    carpetas.append("a"+str(i))

