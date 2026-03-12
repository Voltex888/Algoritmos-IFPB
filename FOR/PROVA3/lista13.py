lista = []
qtd, posicao = map(int, input().split())
for i in range(qtd):
    nome = input()
    lista.append(nome)
    lista.sort()
print(f"O aluno escolhido foi {lista[posicao-1]}")