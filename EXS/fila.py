qtd = int(input())
for _ in range(qtd):
    m = int(input())
    entrada = input().split()
    notas = []
    for i in range(m):
        notas.append(int(entrada[i]))
    ordem = sorted(notas, reverse = True)
    cont = 0
    for i in range(m):
        if notas[i] == ordem[i]:
            cont += 1
    print(cont)