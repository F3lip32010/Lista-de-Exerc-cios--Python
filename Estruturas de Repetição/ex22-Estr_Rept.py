n = int(input("Digite N para encontrar todos os primos até N: "))

primos = []
divisoes = 0

for num in range(2, n + 1):
    eh_primo = True
    for i in range(2, int(num**0.5) + 1):
        divisoes += 1
        if num % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        primos.append(num)

print(f"Números primos até {n}: {primos}")
print(f"Número de divisões executadas: {divisoes}")