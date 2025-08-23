while True:
    num = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))
    if 1 <= num <= 100:
        break
    print("Número deve estar entre 1 e 10!")

print(f"\nTabuada de {num}:")
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")
