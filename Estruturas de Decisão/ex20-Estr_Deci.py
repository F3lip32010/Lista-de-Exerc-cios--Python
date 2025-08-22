print(" A - Álcool ")
print(" G - Gasolina ")
print("")

Q_litro = float(input("Qual foi o número de litros vendidos?: "))
T_comb = input("Qual é o tipo de combustível? (A/G): ").strip().upper()

if T_comb == 'A':
    p_alcool = 1.90
    if Q_litro <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_pagar = Q_litro * p_alcool
    valor_final = valor_pagar - (valor_pagar * desconto)

elif T_comb == 'G':
    p_gasolina = 2.50
    if Q_litro <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_pagar = Q_litro * p_gasolina
    valor_final = valor_pagar - (valor_pagar * desconto)

else:
    print("Tipo de combustível inválido!")
    valor_final = None

if valor_final is not None:
    print(f"O valor a ser pago será de: R${valor_final:.2f}")
