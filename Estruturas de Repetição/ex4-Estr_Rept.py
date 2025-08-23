continuar = True
while continuar:
    try:
        pop_a = float(input("Digite a população inicial do país A: "))
        taxa_a = float(input("Digite a taxa de crescimento do país A (%): ")) / 100
        pop_b = float(input("Digite a população inicial do país B: "))
        taxa_b = float(input("Digite a taxa de crescimento do país B (%): ")) / 100
        
        if pop_a <= 0 or pop_b <= 0 or taxa_a < 0 or taxa_b < 0:
            print("Valores devem ser positivos!")
            continue
        
        if pop_a >= pop_b and taxa_a >= taxa_b:
            print("O país A já tem população maior ou igual e crescimento maior/igual!")
            break
        
        anos = 0
        pop_a_temp = pop_a
        pop_b_temp = pop_b
        
        while pop_a_temp < pop_b_temp:
            pop_a_temp *= (1 + taxa_a)
            pop_b_temp *= (1 + taxa_b)
            anos += 1
        
        print(f"Número de anos necessários: {anos}")
        
        resposta = input("Deseja fazer novo cálculo? (s/n): ").lower()
        if resposta != 's':
            continuar = False
            
    except ValueError:
        print("Digite apenas números válidos!")