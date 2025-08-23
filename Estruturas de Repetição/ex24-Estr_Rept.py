n = int(input("Quantas pessoas? "))

idades = []
for i in range(n):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    idades.append(idade)

media_idade = sum(idades) / len(idades)

if 0 <= media_idade <= 25:
    classificacao = "jovem"
elif 26 <= media_idade <= 60:
    classificacao = "adulta"
else:
    classificacao = "idosa"

print(f"Média de idade: {media_idade:.1f} anos")
print(f"A turma é {classificacao}.")