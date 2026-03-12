def maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior
x = int(input("Digite a quantidade da lista: "))
lista = []
for i in range(x):
    a = int(input(f"Digite o valor do {i+1}° item: "))
    lista.append(a)
resultado = maior(lista)
print(f"O maior da lista é {resultado}")