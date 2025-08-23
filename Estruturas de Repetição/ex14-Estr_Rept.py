n = int(input("Digite quantos termos da sequência Fibonacci deseja ver: "))

if n > 0:
    a, b = 1, 1
    print("Sequência de Fibonacci:")
    
    if n >= 1:
        print(a, end=" ")
    if n >= 2:
        print(b, end=" ")
    
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()
else:
    print("Digite um número positivo!")