sal = float(input("Informe o seu salário atual: R$"))

if sal <= 280:
    aumento=0.20
elif sal <= 700:
    aumento = 0.15
elif sal <= 1500:
    aumento = 0.10
else:
    aumento = 0.05

v_aumento=sal*aumento
percentual = aumento * 100
sal_final=sal+v_aumento

print("O seu salário antes do reajuste, era de: R$", sal)
print("O percentual de aumento aplicado é de: ", percentual, "%")
print("O valor do aumento foi de: R$", v_aumento)
print("O seu novo salário, após o aumento ficou em: R$", sal_final)