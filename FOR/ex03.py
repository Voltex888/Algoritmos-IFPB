soma = 0
positivo = 0
for i in range(6):
    valor = float(input())
    if valor > 0:
        positivo += 1
        soma += valor
media = soma / positivo
print(f"{positivo} valores positivos")
print(f"{media:.1f}")