import math

a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau, pois a = 0.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("A equação não possui raízes reais, pois delta é negativo.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui uma raiz real: x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: x1 = {x1:.2f}, x2 = {x2:.2f}")