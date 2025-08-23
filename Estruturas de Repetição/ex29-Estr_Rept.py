preco_pao = float(input("Preço do pão: R$ "))

print(f"Panificadora Pão de Ontem - Tabela de preços")

for i in range(1, 51):
    preco_total = i * preco_pao
    print(f"{i} - R$ {preco_total:.2f}")