n = int(input("Quantos números você vai digitar? "))

numeros = []
for i in range(n):
    while True:
        num = float(input(f"Digite o {i+1}º número (entre 0 e 1000): "))
        if 0 <= num <= 1000:
            numeros.append(num)
            break
        print("Número deve estar entre 0 e 1000!")

print(f"Menor valor: {min(numeros)}")
print(f"Maior valor: {max(numeros)}")
print(f"Soma dos valores: {sum(numeros)}")