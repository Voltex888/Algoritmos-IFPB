testes = int(input())
for i in range(testes):
    alunos = int(input())
    nota = input().split()
    notas = []
    for i in range(alunos):
        notas.append(int(nota[i]))
    ordem = sorted(notas, reverse=True)
    contador = 0
    for j in range(alunos):
        if notas[j] == ordem[j]:
            contador +=1
    print(contador)