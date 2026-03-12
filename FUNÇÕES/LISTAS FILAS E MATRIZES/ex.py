matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elementos = int(input("Digite os elementos de uma matriz: "))
        linha.append(elementos)
    matriz.append(linha)
soma = 0
contador = 0
for i in range(2):
    for j in range(2):
        soma += matriz[i][j]
        contador += 1
print(f"A soma dos elementos é = {soma}")
print(f"A média dos elementos é = {soma/contador}")