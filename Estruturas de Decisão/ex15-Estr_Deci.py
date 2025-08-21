l1 = float(input("Insira o primeiro lado do triângulo: "))
l2 = float(input("Insira o segundo lado do triângulo: "))
l3 = float(input("Insira o terceiro lado do triângulo: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 and l1 > 0 and l2 > 0 and l3 > 0:
    print("Os valores formam um triângulo!")

    if l1 == l2 == l3:
        print("O tipo do triângulo é Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O tipo do triângulo é Isósceles")
    else:
        print("O tipo do triângulo é Escaleno")
else:
    print("Os valores NÃO formam um triângulo!")
