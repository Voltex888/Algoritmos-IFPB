def juntar(letras, i=0):
    if i == len(letras):
        return ""
    return letras[i] + juntar(letras, i+1)
qtd = int(input("Quantas letras vc quer digitar: "))
lista = []
for i in range(qtd):
    letra = input(f"Digite a {i+1}° letra: ")
    lista.append(letra)
resultado = juntar(lista)
print(f"O resultado é {resultado}")