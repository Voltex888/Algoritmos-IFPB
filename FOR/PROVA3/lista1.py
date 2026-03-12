# Leia uma lista com 10 números e crie uma nova lista contendo apenas os valores sem repetição, em ordem crescente
lista = []
for i in range(10):
    x = int(input("Digite um número: "))
    while x in lista:
        x = int(input("Esse número já está na lista, digite outro número: "))
    lista.append(x)
    lista.sort()
for lista in range(10):
    print(f"lista[{i+1}] = {lista[i]}")