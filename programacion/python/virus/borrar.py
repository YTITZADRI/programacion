import subprocess
import os
# ejecutar el comando ls
output = (subprocess.run(['ls'], capture_output=True, text=True))
output = output.stdout.split("\n")
result = []
for element in output:
    a = element
    try:
        if list(element)[0] == "a":
            result.append(a)
    except IndexError:
        pass
# imprimir el resultado
i = 0
for element in result:
    os.system("rm -r "+str(element))
    i += 1
    print("rm -r "+str(element), "carpetas borradas: ", str(i+1000))
