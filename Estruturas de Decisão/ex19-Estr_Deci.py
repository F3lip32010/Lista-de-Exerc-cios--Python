p1 = input("Telefonou para a vítima? (s/n): ").strip().lower() == "s"
p2 = input("Esteve no local do crime? (s/n): ").strip().lower() == "s"
p3 = input("Mora perto da vítima? (s/n): ").strip().lower() == "s"
p4 = input("Devia para a vítima? (s/n): ").strip().lower() == "s"
p5 = input("Já trabalhou com a vítima? (s/n): ").strip().lower() == "s"

respostas_positivas = sum([p1, p2, p3, p4, p5])

# Classificação
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"\nClassificação: {classificacao}")