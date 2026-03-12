# Peça ao usuário 5 números e mostre a soma dos números que estão em índices pares.
lista = []
y = 0
for i in range(5):
    x = int(input())
    lista.append(x)
for j in range(5):
    if lista[j] % 2 == 0:
        y+= lista[j]    
print(f"A soma dos pares é {y}")
        