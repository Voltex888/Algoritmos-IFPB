op = input().strip().upper()
matriz = []
for i in range(12):
    linha =[]
    for j in range(12):
        elemento = float(input())
        linha.append(elemento)
    matriz.append(linha)
soma = 0.0
contador = 0
for i in range(12):
    for j in range(i + 1, 12):
        soma += matriz[i][j]
        contador += 1
if op == "M":
    soma /= contador
    print(f"{soma:.1f}")