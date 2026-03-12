salario = float(input("Digite um salário e veja ele com bonús: R$ "))
if salario > 1250:
    bonus = salario + salario * 0.1
else:
    bonus = salario + salario * 0.15
print(f"O seu salário é de R$ {salario:.2f} e com bonús é de R$ {bonus:.2f}")