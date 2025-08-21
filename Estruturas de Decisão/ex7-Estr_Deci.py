n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

if n1 == n2 == n3:
    print("Todos os números são iguais:", maior)
else:
    print("O maior número é:", maior)
    print("O menor número é:", menor)
