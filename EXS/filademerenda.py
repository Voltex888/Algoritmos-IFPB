testes = int(input())
for i in range(testes):
    qtd = int(input())
    nota = input().split()
    notas = []
    for i in range(qtd):
        notas.append(int(nota[i]))
    ordem = sorted(notas, reverse=True)
    contador = 0
    for i in range(qtd):
        if notas[i] == ordem[i]:
            contador += 1
    print(contador)