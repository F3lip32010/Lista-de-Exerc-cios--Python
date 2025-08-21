n1 = float(input("Insira a primeira nota do aluno: "))
n2 = float(input("Insira a segunda nota do aluno: "))

média = (n1 + n2)/2

if média >= 7:
    print("Aprovado")
elif média == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")