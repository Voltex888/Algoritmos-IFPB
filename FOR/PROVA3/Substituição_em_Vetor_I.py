# Timelimit: 1
# Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.
lista = []
for i in range(10):
    x = int(input())
    if x <= 0:
        x = 1
    lista.append(x)
for j in range(10):
    print(f"X[{j}] = {lista[j]}")