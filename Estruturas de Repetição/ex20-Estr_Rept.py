n = int(input("Digite um número para verificar se é primo: "))

if n < 2:
    print(f"{n} não é primo.")
else:
    eh_primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(f"{n} é primo.")
    else:
        print(f"{n} não é primo.")