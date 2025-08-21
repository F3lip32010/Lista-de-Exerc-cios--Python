print(" M - Matutino")
print(" V - Vespertino")
print(" N - Noturno")

turno = str(input("Informe qual é o seu turno de estudo: "))

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Turno inválido!")