n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    print("O maior número é:", n1)
elif n2 >= n1 and n2 >= n3:
    print("O maior número é:", n2)
elif n3 >= n1 and n3 >= n2:
    print("O maior número é:", n3)
else:
    print("Os números são iguais.")
