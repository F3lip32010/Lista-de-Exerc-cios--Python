continuar = True
while continuar:
    try:
        n = int(input("Digite um número para calcular o fatorial (0-15): "))
        if 0 <= n < 16:
            fatorial = 1
            for i in range(1, n + 1):
                fatorial *= i
            print(f"{n}! = {fatorial}")
        else:
            print("Número deve estar entre 0 e 15!")
        
        resposta = input("Deseja calcular outro fatorial? (s/n): ").lower()
        if resposta != 's':
            continuar = False
    except ValueError:
        print("Digite apenas números inteiros!")