print("Regra: A senha deve ser diferente do nome de usuário.")

while True:
    
    usuario = input("Digite o nome de usuário: ").strip()
    
    senha = input("Digite a senha: ").strip()
    
    if senha.lower() == usuario.lower():
        print("\n ERRO: A senha não pode ser igual ao nome do usuário!")
        print("Por favor, escolha uma senha diferente.\n")
        continue
    
    print("\n Credenciais válidas!")
    print(f"Usuário '{usuario}' cadastrado com sucesso!")
    break

print("\nObrigado por usar nosso sistema!")