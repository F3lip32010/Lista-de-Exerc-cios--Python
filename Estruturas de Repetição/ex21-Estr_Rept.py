n = int(input("Digite um número para verificar se é primo: "))

if n < 2:
    print(f"{n} não é primo.")
else:
    divisores = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisores.append(i)
            if i != n // i:
                divisores.append(n // i)
    
    if divisores:
        print(f"{n} não é primo.")
        print(f"É divisível por: {sorted(divisores)}")
    else:
        print(f"{n} é primo.")