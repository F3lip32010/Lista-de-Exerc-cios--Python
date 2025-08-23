n = int(input("Quantos números você vai digitar? "))

numeros = []
for i in range(n):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print(f"Menor valor: {min(numeros)}")
print(f"Maior valor: {max(numeros)}")
print(f"Soma dos valores: {sum(numeros)}")