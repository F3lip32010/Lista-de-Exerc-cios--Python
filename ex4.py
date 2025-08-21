sal_hora = float(input("Quanto você ganha por hora? R$: "))
horas_trabalhadas = int(input("Quantas horas você trabalhou neste mês?: "))

total_salario = sal_hora * horas_trabalhadas

print("O seu salário total este mês é de: R$ {:.2f}".format(total_salario))
