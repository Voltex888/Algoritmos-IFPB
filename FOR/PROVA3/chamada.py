testes, posicao = map(int, input().split())
chamada = []
for i in range(testes):
    nome = input()
    chamada.append(nome)
    chamada.sort()
print(f"O aluno da posicao {posicao}° é: {chamada[posicao-1]}")