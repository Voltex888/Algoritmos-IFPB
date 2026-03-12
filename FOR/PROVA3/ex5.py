lista = []
for i in range(10):
    x = int(input())
    lista.append(x)
qtd = len(lista)
soma = sum(lista)
media = soma / qtd
for i in range(10):
    if lista[i] > media:
        print(f"O número {lista[i]} é maior que a média que é {media:.2f}")