num_turmas = int(input("Digite o número de turmas: "))

total_alunos = 0
for i in range(num_turmas):
    while True:
        alunos = int(input(f"Quantos alunos na turma {i+1}? "))
        if 0 <= alunos <= 40:
            total_alunos += alunos
            break
        print("Turma não pode ter mais de 40 alunos!")

media = total_alunos / num_turmas
print(f"Média de alunos por turma: {media:.2f}")