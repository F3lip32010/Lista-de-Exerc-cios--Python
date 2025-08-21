n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terçeiro número: "))

lista = [n1, n2, n3]
lista.sort(reverse=True)

print("Ordem decrescente: ", lista)