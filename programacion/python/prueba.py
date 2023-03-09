num = 0
while True:

    i = ""
    a = 0
    b = 0
    while b <= 50:
        while a <= 150:
            i += str(num)
            a += 1
        print(i)
        b += 1
    if num > 9:
        num = 0
    else:
        num += 1
    