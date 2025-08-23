n = int(input("Quantas notas você vai digitar? "))

notas = []
for i in range(n):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"Média aritmética: {media:.2f}")