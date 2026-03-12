lista = []
for i in range(5):
    nome = input()
    lista.append(nome)
    lista.sort()
print("-=-"*20)
print("Ordem alfabetica")
print("-=-"*20)
for j in range(5):
    print(f"Nome {j+1}°: {lista[j]}")