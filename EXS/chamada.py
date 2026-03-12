a, b = map(int, input().split())
chamada = [] 
for i in range(a):
    nome = input()
    chamada.append(nome)
    chamada.sort()
posicao = chamada[b-1]
print(posicao)