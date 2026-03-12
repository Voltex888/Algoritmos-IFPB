lista = []
for i in range(5):
    numero = int(input())
    lista.append(numero)
lista.sort(reverse=True)
meio = (len(lista)//2)
print(lista[meio])