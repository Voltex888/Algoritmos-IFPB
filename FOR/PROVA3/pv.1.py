lista = []
x =int(input())
while x !=-1:
    lista.append(x)
    x = int(input())
print(f"Tem {len(lista)} números na lista")
for i in range(len(lista)):
    print(f"N{i} = {lista[i]}")
print(f"A soma da lista é {sum(lista)}")