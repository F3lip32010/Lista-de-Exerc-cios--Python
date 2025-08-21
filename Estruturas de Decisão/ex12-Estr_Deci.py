V_hora = float(input("Digite o valor das suas horas trabalhadas: R$"))
H_trabalhadas = int(input("Informe a quantidade de horas trabalhadas no mês: "))

Sal_Bruto = V_hora * H_trabalhadas

if Sal_Bruto <= 900:
    IR = 0
elif Sal_Bruto <= 1500:
    IR = 0.05 * Sal_Bruto
elif Sal_Bruto <= 2500:
    IR = 0.10 * Sal_Bruto
else:
    IR = 0.20 * Sal_Bruto

INSS = 0.10 * Sal_Bruto
FGTS = 0.11 * Sal_Bruto

T_desconto = IR + INSS
Sal_Liq = Sal_Bruto - T_desconto

print(f"Salário Bruto: R${Sal_Bruto:.2f}")
print(f"(-) IR: R${IR:.2f}")
print(f"(-) INSS: R${INSS:.2f}")
print(f"FGTS: R${FGTS:.2f}")
print(f"Total de descontos: R${T_desconto:.2f}")
print(F"Salário Líquido: R${Sal_Liq:.2f}")