# Crie um programa que leia 7 números, armazene-os e mostre o segundo maior valor
lista = []
for i in range(7):
    x = int(input())
    lista.append(x)
    lista.sort(reverse=True)
print(f"O segundo maior número da lista é: {lista[1]}")