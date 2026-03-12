# Leia uma lista de 10 números e mostre os números na ordem inversa à que foram digitados.
lista = []
for i in range(10):
    x = int(input())
    lista.insert(0, x)
    lista.sort(reverse=True)
print("-=-"*20)
print("lista em decrescente")
print("-=-"*20)
for j in range(10):
    print(f"Número {j+1}° da lista: {lista[j]}")