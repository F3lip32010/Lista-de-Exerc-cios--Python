p1 = float(input("Qual é o preço do primeiro produto?: R$"))
p2 = float(input("Qual é o preço do segundo produto?: R$"))
p3 = float(input("Qual é o preço do terceiro produto?: R$"))

produto_mais_barato = min(p1, p2, p3)

print(f"É recomendado que você compre o produto de R${produto_mais_barato:.2f}")
