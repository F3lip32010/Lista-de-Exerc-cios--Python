n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda notas: "))

média = (n1+n2)/2

if média >= 9:
    conceito = "A"
    mensagem = 'APROVADO!'
elif média >= 7.5:
    conceito = "B"
    mensagem = 'APROVADO!'
elif média >= 6:
    conceito = "C"
    mensagem = 'APROVADO!'
elif média >= 4:
    conceito = "D"
    mensagem = 'REPROVADO!'
else:
    conceito = "E"
    mensagem = 'REPROVADO!'

print(f"Nota 1: {n1:.2f}")
print(f"Nota 2: {n2:.2f}")
print(f"Média: {média}")
print(f"Conceito: {conceito}")
print(f"Status: {mensagem}")