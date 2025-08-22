pop_A = 80000
pop_B = 200000
taxa_A = 0.03
taxa_B = 0.015

anos = 0

while pop_A <= pop_B:
    pop_A += pop_A * taxa_A
    pop_B += pop_B * taxa_B
    anos += 1

print(f"Serão necessários {anos} anos para que a população de A ultrapasse ou iguale a população de B.")
