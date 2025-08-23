num_cds = int(input("Quantos CDs você tem? "))

valores = []
for i in range(num_cds):
    valor = float(input(f"Valor do {i+1}º CD: R$ "))
    valores.append(valor)

total_investido = sum(valores)
valor_medio = total_investido / num_cds

print(f"Valor total investido: R$ {total_investido:.2f}")
print(f"Valor médio por CD: R$ {valor_medio:.2f}")