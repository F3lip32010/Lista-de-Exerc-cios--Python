total_eleitores = int(input("Digite o número total de eleitores: "))

votos = [0, 0, 0]

for i in range(total_eleitores):
    while True:
        voto = int(input(f"Eleitor {i+1}, vote (1, 2 ou 3): "))
        if voto in [1, 2, 3]:
            votos[voto-1] += 1
            break
        print("Vote apenas em 1, 2 ou 3!")

print("\nResultado da eleição:")
for i in range(3):
    print(f"Candidato {i+1}: {votos[i]} votos")