testes = int(input())
for i in range(testes):
    qtd = int(input())
    nota = input().split()
    notas = []
    for j in range(qtd):
        notas.append(int(nota[j]))
    ordem = sorted(notas, reverse=True)
    contador = 0
    for i in range(qtd):
        if ordem[i] == notas[i]:
            contador+=1
    print(contador)