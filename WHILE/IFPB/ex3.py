soma = 0 
positivo = 0
for i in range(1,7):
    valor = float(input())
    if valor > 0:
        positivo += 1
        soma += valor
media = soma / positivo 
print(positivo)
print(media)