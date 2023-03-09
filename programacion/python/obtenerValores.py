vcriptos = [16216.0,1171.0,0.09494,0.9997,1.2]

def decimales():
    global vcriptos
    result = []
    for element in vcriptos:
        if element < 1:
            result.append(len(str(element))-2)
        else:
            result.append(len(str(element))-1)
    print(result)
decimales()