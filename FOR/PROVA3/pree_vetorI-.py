# Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10].
# Em cada posição subsequente, coloque o dobro do valor da posição anterior.
# Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.
x = int(input())
N = [x]
for i in range(10):
    print(f"N[{i}] = {N[i]}")
    x *= 2
    N.append(x)