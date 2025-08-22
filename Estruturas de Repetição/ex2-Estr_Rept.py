nome = input("Digite seu nome: ").strip()
while len(nome) <= 3:
    print("Erro: o nome deve ter mais que 3 caracteres.")
    nome = input("Digite seu nome: ").strip()

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Erro: idade deve estar entre 0 e 150.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: R$"))
while salario <= 0:
    print("Erro: o salário deve ser maior que zero.")
    salario = float(input("Digite seu salário: R$"))

sexo = input("Digite seu sexo (f/m): ").lower()
while sexo not in ['f', 'm']:
    print("Erro: sexo deve ser 'f' ou 'm'.")
    sexo = input("Digite seu sexo (f/m): ").lower()

estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Erro: estado civil deve ser 's', 'c', 'v' ou 'd'.")
    estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()

print("\n Dados cadastrados com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
