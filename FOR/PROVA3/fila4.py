lista = []
qtd = int(input())
for i in range(qtd):
    x = int(input("Digite um número: "))
    lista.append(x)
    lista.sort(reverse=True)
print(f"O segundo maior número é {lista[1]}")
print(f"O maior número é {lista[0]}")
print(f"O menor número é {lista[-1]}")
