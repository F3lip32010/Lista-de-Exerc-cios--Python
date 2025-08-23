n = int(input("Digite um número para calcular o fatorial: "))

if n < 0:
    print("Fatorial não existe para números negativos!")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    
    print(f"{n}! = {fatorial}")