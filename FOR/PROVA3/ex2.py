nome = input()
lista = [nome]
maior = nome
for i in range(4):
    nome = input()
    if len(nome) > len(maior):
        maior = nome
        lista.insert(0, maior)
print(lista[0])