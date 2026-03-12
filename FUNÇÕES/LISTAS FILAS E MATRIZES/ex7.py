n = int(input())
for _ in range(n):
    m = int(input())
    entrada = input().split()
    notas = []
    for i in range(m):
        notas.append(int(entrada[i]))
    ordenada = sorted(notas, reverse=True)
    contador = 0
    for i in range(m):
        if notas[i] == ordenada[i]:
            contador += 1
    print(contador)