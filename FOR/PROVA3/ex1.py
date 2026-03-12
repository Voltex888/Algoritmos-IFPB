lista = []
pares = []
for i in range(10):
    x = int(input())
    lista.append(x)
    if x % 2 == 0:
        pares.append(x)
for j in range(len(pares)):
    print(f"Pares[{j}] = {pares[j]}")
for k in range(len(lista)):
    print(f"Lista[{k}] = {lista[k]}")