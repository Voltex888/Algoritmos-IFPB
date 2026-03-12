# Leia uma lista com 10 números e crie uma nova lista contendo apenas os valores sem repetição
lista = []
for i in range(10):
    x = input(f"Digite o {i+1}° número: ")
    while x in lista:
        x = input("Esse número já está na lista. Digite outro: ")
    lista.append(x)
lista.sort()
print("-=-" * 20)
print("Lista em ordem crescente:")
print("-=-" * 20)
for i, num in enumerate(lista, start=1):
    print(f"{i}° número: {num}")