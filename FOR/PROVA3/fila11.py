testes = int(input())
for i in range(testes):
    qtd = int(input())
    nota = input().split()
    notas = []
    for j in range(qtd):
        notas.append(int(nota[j]))
    ordem = sorted(notas, reverse=True)
    certos = 0
    for j in range(qtd):
        if notas[j] == ordem[j]:
            certos += 1
    print(certos)