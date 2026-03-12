# faça um progama que leia um salario de uma pessoa, e aplique um bonus por cada dias trabalhado
# por exemplo 1% ao dia
salario = float(input())
dias = int(input())
bonus = dias * (salario * 0.01)
total = salario + bonus
print(f"{total:.1f}")