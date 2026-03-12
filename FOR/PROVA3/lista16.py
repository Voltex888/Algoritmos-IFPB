x = int(input())
lista = [x]
for i in range(10):
    print(f"N[{i}] = {lista[i]}")
    x *=2
    lista.append(x)