lista = []
qtd = int(input("Quantos números vc quer colocar na lista: "))
for i in range(qtd):
    x = int(input(f"Número {i+1}° da lista: "))
    while x in lista:
        x = int(input(f"O número {x} já está na lista, digite outro: "))
    lista.append(x)
    lista.sort(reverse=True)
print("-=-"*20)
print(f"O segundo maior número é: {lista[1]}")
print("-=-"*20)