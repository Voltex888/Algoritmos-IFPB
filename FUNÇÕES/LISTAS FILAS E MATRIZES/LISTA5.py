listanomes = []
for i in range(10):
    nome = input(f"Digite o {i+1}º nome: ")
    listanomes.append(nome)
listanomes.sort(reverse=True)
print("\nLista em ordem decrencente:")
print(listanomes, sep="\n")
for nome in listanomes:
    print(nome)