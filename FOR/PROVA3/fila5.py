qtd = int(input())
lista = []
for i in range(qtd):
    x = int(input("Digite um número: "))
    lista.append(x)
maior = max(lista)
menor = min(lista)
print(f"O maior número é: {maior} e sua posiçao é {lista.index(maior)}")
print(f"O menor número é: {menor} e sua posiçao é {lista.index(menor)}")