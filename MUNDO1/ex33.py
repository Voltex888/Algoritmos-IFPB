x = float(input())
maior = x
menor = x
for i in range(2):
    x = float(input())
    if x > maior:
        maior = x
    if x < menor:
        menor = x
print(f"O maior número é {maior} o menor é {menor}")