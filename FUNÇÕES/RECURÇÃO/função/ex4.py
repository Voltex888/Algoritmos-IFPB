def media_lista(valores):
    soma = 0
    for item in valores:
        soma += item
    return soma / len(valores)

lista = []
x = int(input("Digite a quantidade da itens na lista: "))
for i in range(x):
    a = int(input(f"Digite o {i+1}° da lista: "))
    lista.append(a)
resultado = media_lista(lista)
print(f"O resultado da média da lista é {resultado}")